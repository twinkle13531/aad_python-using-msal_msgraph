from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import os
import sys

from webapp_name.auth_helper import get_sign_in_flow, get_token, get_token_from_code, remove_user_and_token, store_user
from webapp_name.graph_helper import get_user
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Create your views here.

def sign_in(request):
    flow = get_sign_in_flow()  # Get the sign-in flow
    # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(flow['auth_uri'])


def callback(request):
    result = get_token_from_code(request)  # Make the token request
    user = get_user(result['access_token'])  # Get the user's profile
    store_user(request, user)  # Store user
    return HttpResponseRedirect(reverse('home'))


def sign_out(request):
    remove_user_and_token(request)  # Clear out the user and token
    return HttpResponseRedirect(reverse('home'))


def home(request):
    return HttpResponse(get_token(request))
