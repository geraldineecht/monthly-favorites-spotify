import base64
from urllib.parse import urlencode

# 1. Go to Web API Spotify and create a new app in your dashboard
# 2. Add a redirect url in edit settings
# 3. Get Client_ID and Client_Secret
client_id = ""
client_secret = ""

# 4. Encode the ridirect url
url_encoded = ""

# 5. Create your client credentials and encode them in base 64
client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

# 6. Have your application request authorization; the user logs in and authorizes access. Print get_auth_code to get the url of th code
get_auth_code = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={url_encoded}&scope=user-library-read%20user-top-read%20playlist-modify-public%20playlist-modify-private"

# 7. Once you get the code, assign it to authorization_code
authorization_code = ""

# 8. Have your application request refresh and access tokens; Spotify returns access and refresh tokens. Print it and paste it in cmm to get the access_token and refresh_token
app_request = f' curl -H "Authorization: Basic {client_creds_b64.decode()}" -d grant_type=authorization_code -d code={authorization_code} -d redirect_uri={url_encoded} https://accounts.spotify.com/api/token --ssl-no-revoke'


spotify_user_id = ""
spotify_token = ""
refresh_token = ""

