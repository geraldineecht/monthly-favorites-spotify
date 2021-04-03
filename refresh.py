from spotify_tokens import refresh_token, client_creds_b64
import requests
import json
import base64
from urllib.parse import urlencode

class Refresh:
    def __init__(self):
        self.refresh_token = refresh_token
        self.client_creds_b64 = client_creds_b64.decode()
    
    def refresh(self):
        
        refresh_endpoint = "https://accounts.spotify.com/api/token"
        response = requests.post(refresh_endpoint,
                                data = {"grant_type":"refresh_token", "refresh_token": refresh_token},
                                headers = {"Authorization": "Basic " + client_creds_b64.decode()})
        
        response_json = response.json()

        return response_json["access_token"]
