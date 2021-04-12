import json
import requests
from datetime import date
from spotify_tokens import spotify_token, spotify_user_id
from refresh import Refresh

class MonthlyFavorites:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.tracks = ""

    def find_songs(self):
        print ("Finding songs in saved tracks...")

        spotify_type = "tracks"
        time_range = "short_term"

        tracks_endpoint = f"https://api.spotify.com/v1/me/top/{spotify_type}?time_range={time_range}"

        response = requests.get(tracks_endpoint,
                                headers = {"Content-Type" : "application/json",
                                "Authorization": "Bearer {}".format(self.spotify_token)})
        
        response_json = response.json()

        # Loops through playlists tracks and add them to a list
        for i in response_json["items"]:
            # get the tracks and join them with commas
            self.tracks += (i["uri"] + ",")
        self.tracks = self.tracks[:-1]
        self.add_songs()

    def create_playlist(self):
        print ("Creating a playlist...")
        
        playlist_endpoint = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
        
        actual_month = date.today().strftime("%m")
        months_names = {"01" : "January", "02" : "February", "03" : "March", "04" : "April", "05" : "May",
                        "06" : "June", "07" : "July", "08" : "August", "09": "September", "10" : "October", "11" : "November", "12": "December"}

        request_body = json.dumps({"name": months_names[actual_month] + " Favorite Songs",
                                    "description": "Monthly generated playlist of my favorite songs",
                                    "public": True})
        
        response = requests.post(playlist_endpoint,
                                data = request_body,
                                headers = {"Content-Type" : "application/json",
                                "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()

        return response_json["id"]
    
    def add_songs(self):
        print ("Adding Songs...")

        self.playlist_id = self.create_playlist()

        tracks_endpoint = f"https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks?uris={self.tracks}"

        response = requests.post(tracks_endpoint,
                                headers = {"Content-Type" : "application/json",
                                "Authorization": "Bearer {}".format(self.spotify_token)})

    def start(self):
        # We have to refresh the token in order to send a new query
        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        self.find_songs()

a = MonthlyFavorites()
a.start()
