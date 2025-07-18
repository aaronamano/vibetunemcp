from fastmcp import FastMCP
from dotenv import load_dotenv
import requests
import os

load_dotenv()

mcp = FastMCP(name="VibetuneMCP")

@mcp.tool()
def get_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = { "grant_type": "client_credentials", "client_id": os.getenv("SPOTIFY_CLIENT_ID"), "client_secret": os.getenv("SPOTIFY_CLIENT_SECRET") }
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    
    access_token = response.json()['access_token']
    return access_token

@mcp.tool()
def create_playlist(access_token, name: str ="My New Playlist", description: str ="Created with VibetuneAI", public: bool = True):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "name": name,
        "description": description,
        "public": public
    }
    user_id = "6jvibgrfvek4sz1x85zdc9a9v"
    
    response = requests.post(f"https://api.spotify.com/v1/{user_id}/playlists", headers=headers, data=data)
    
    playlist_id = response.json()['id']
    return playlist_id

@mcp.tool()
def get_songs(access_token, q: str, type: str):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(f"https://api.spotify.com/v1/search?q={q}&type={type}'", headers=headers)
    
    if response.status_code == 200:
        song_ids = response.json()['tracks']['items']['id']
        return song_ids
    else:
        return {"error": "Failed to fetch songs"}


@mcp.tool()
def insert_songs(access_token, song_ids: list, playlist_id, position: int = 0):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "uris": song_ids,
        "position": position
    }


if __name__ == "__main__":
    mcp.run()