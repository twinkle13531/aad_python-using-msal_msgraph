import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from project_name.auth_helper import *
from project_name.gragh_helper import *
from project_name.auth_helper import get_sign_in_flow, get_token_from_code
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def sign_in(request):
    flow = get_sign_in_flow() # Get the sign-in flow
    # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    return HttpResponseRedirect(flow['auth_uri']) # Redirect to the Azure sign-in page

def callback(request):
    result = get_token_from_code(request) # Make the token request
    user = get_user(result['access_token']) #Get the user's profile
    store_user(request, user) # Store user
    return HttpResponseRedirect(reverse('home'))

def sign_out(request):
    remove_user_and_token(request) # Clear out the user and token
    return HttpResponseRedirect(reverse('home'))
