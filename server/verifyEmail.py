from google.oauth2 import id_token
from google.auth.transport import requests

"""
For more information: https://developers.google.com/identity/gsi/web/guides/verify-google-id-token
"""
def verifyEmail(credentialToken):
    try:
        idinfo = id_token.verify_oauth2_token(credentialToken, requests.Request(), "278499378190-1oeu5m9gukn5t9neb5psqqvlpsioaega.apps.googleusercontent.com")

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        return True
    except ValueError:
        return False