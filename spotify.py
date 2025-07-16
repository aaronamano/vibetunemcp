import requests
from dotenv import load_dotenv
import os

load_dotenv()

# API call to get the access token
token_response = requests.post("https://accounts.spotify.com/api/token", 
                            headers={"Content-Type": "application/x-www-form-urlencoded"}, 
                            data={
                                "grant_type": "client_credentials",
                                "client_id": os.getenv("SPOTIFY_CLIENT_ID"),
                                "client_secret": os.getenv("SPOTIFY_CLIENT_SECRET")
                            })

# Get the access token from the response
access_token = token_response.json()['access_token']

# Make the API call to get artist info
artist_id = "4Z8W4fKeB5YxbusRsdQVPb"
artist_info_response = requests.get(f"https://api.spotify.com/v1/artists/{artist_id}", headers={
    "Authorization": f"Bearer {access_token}"
})

## API call to get MY profile
my_profile_response = requests.get("https://api.spotify.com/v1/me", headers={
    "Authorization": f"Bearer {access_token}"
})