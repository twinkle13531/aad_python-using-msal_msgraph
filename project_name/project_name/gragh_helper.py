import requests
import json

graph_url = 'https://graph.microsoft.com/v1.0'

# Send GET to /me
def get_user(token):
    user = requests.get(
        '{0}/me'.format(graph_url),
        headers={'Authorization': 'Bearer {0}'.format(token)},
        params={'$select': 'displayName,mail,mailboxSettings,userPrincipalName'})
    return user.json() # Return the JSON result
