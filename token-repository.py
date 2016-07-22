import requests
import os
import json

class TokenResponse(object):
    def __init__(self, dict):
        self.access_token = dict['access_token']
        self.expires_in = int(dict['expires_in'])
        self.refresh_token = dict['refresh_token']
        self.token_type = dict['token_type']

class Credentials:
    pass

class TokenRepository:
    global URL 
    URL = 'https://api.gettyimages.com/oauth2/token'

    def __init__(self, credentials):
        self.payload = {
            'client_id': credentials.api_key,
            'client_secret': credentials.api_secret,
            'username': credentials.username,
            'password': credentials.password,
            'grant_type': 'password'
        }
    def get_token(self):
        r = requests.post(URL, data = self.payload)
        dict = json.loads(r.text)
        return TokenResponse(dict)


creds = Credentials()
creds.api_key = os.environ['GettyImagesApi_ApiKey']
creds.api_secret = os.environ['GettyImagesApi_ApiSecret']
creds.username = os.environ['GettyImagesApi_UserName']
creds.password = os.environ['GettyImagesApi_UserPassword']

token_repo = TokenRepository(creds)
token = token_repo.get_token()
print 'access_token: ' + token.access_token
print 'expires_in: ' + str(token.expires_in)
print 'refresh_token: ' + token.refresh_token
print 'token_type: ' + token.token_type