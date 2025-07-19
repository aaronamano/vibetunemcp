from fastmcp import FastMCP
from dotenv import load_dotenv
import requests
import os

load_dotenv()

mcp = FastMCP(name="VibetuneMCP")

@mcp.tool()
def get_movie_recommendations(genre: str, min_year: int, max_year: int, content_rating: str, keyword: str):
    params = {
        "filter.type": "urn:entity:movie",
        "filter.tags": f"urn:tag:genre:media:{genre},urn:tag:keyword:media:{keyword}",
        "filter.release_year.min": f"{min_year}",
        "filter.release_year.max": f"{max_year}",
        "filter.content_rating" : f"{content_rating}"
    }

    response = requests.get(
        "https://hackathon.api.qloo.com/v2/insights",
        headers={
            "accept": "application/json",
            "X-Api-Key": os.getenv("QLOO_API_KEY")
        },
        params=params
    )

    data = response.json()
    for entity in data['results']['entities']:
        return entity['name']

@mcp.tool()
def get_tv_show_recommendations(genres: str, min_year: int, max_year: int, content_rating: str, keyword: str):
    params = {
        "filter.type": "urn:entity:tv_show",
        "filter.tags": f"urn:tag:genre:media:{genres},urn:tag:keyword:media:{keyword}",
        "filter.release_year.min": f"{min_year}",
        "filter.release_year.max": f"{max_year}",
        "filter.content_rating" : f"{content_rating}"
    }

    response = requests.get(
        "https://hackathon.api.qloo.com/v2/insights",
        headers={
            "accept": "application/json",
            "X-Api-Key": os.getenv("QLOO_API_KEY")
        },
        params=params
    )

    data = response.json()
    for entity in data['results']['entities']:
        return entity['name']

@mcp.tool()
def get_book_recommendations(genre: str, min_year: int, max_year: int, keyword: str):
    params = {
        "filter.type": "urn:entity:book",
        "filter.tags": f"urn:tag:genre:media:{genre},urn:tag:keyword:media:{keyword}",
        "filter.publication_year.min": f"{min_year}",
        "filter.publication_year.max": f"{max_year}"
    }

    response = requests.get(
        "https://hackathon.api.qloo.com/v2/insights",
        headers={
            "accept": "application/json",
            "X-Api-Key": os.getenv("QLOO_API_KEY")
        },
        params=params
    )
    
    data = response.json()
    for entity in data['results']['entities']:
        return entity['name']

@mcp.tool()
def get_qloo_search_results(query: str, num_pages: int = 1):
    params = {
        "query": f"{query}",
        "types": "urn:entity:album",
        "operator.filter.tags": "union",
        "page": f"{num_pages}",
        "sort_by": "match",
    }

    response = requests.get(
        "https://hackathon.api.qloo.com/v2/search",
        headers={
            "accept": "application/json",
            "X-Api-Key": os.getenv("QLOO_API_KEY")
        },
        params=params
    )

    data = response.json()
    for result in data['results']:
        return result['name']

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

@mcp.tool()
def run_process():
    get_token()
    create_playlist()
    get_songs()
    insert_songs()


if __name__ == "__main__":
    mcp.run()