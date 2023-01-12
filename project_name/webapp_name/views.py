from project_name.auth_helper import *
from project_name.gragh_helper import *
from project_name.auth_helper import get_sign_in_flow, get_token_from_code
from django.shortcuts import render

# Create your views here.
def sign_in(request):
# Get the sign-in flow
flow = get_sign_in_flow()
# Save the expected flow so we can use it in the callback
try:
request.session['auth_flow'] = flow
except Exception as e:
print(e)
# Redirect to the Azure sign-in page
return HttpResponseRedirect(flow['auth_uri'])

def callback(request):
# Make the token request
result = get_token_from_code(request)

#Get the user's profile
user = get_user(result['access_token'])

# Store user
store_user(request, user)
return HttpResponseRedirect(reverse('home'))

def sign_out(request):
# Clear out the user and token
remove_user_and_token(request)

return HttpResponseRedirect(reverse('home'))
