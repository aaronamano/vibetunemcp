from fastmcp import FastMCP
from dotenv import load_dotenv
import requests
import os
from urllib.parse import urlencode
import base64
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

mcp = FastMCP(name="VibetuneMCP")

@mcp.prompt()
def suggest_songs_from_movies(movies: list):
    """
    Suggest songs based on the provided movie titles.
    Return format: Array of strings with song suggestions.
    Example: ["Song A from Movie 1", "Song B from Movie 2"]
    """
    suggestions = []
    for movie in movies:
        suggestions.append(f"Suggest a song from the movie '{movie}'")
    return suggestions

@mcp.prompt()
def suggest_songs_from_tv_shows(tv_shows: list):
    """
    Suggest songs based on the provided movie titles.
    Return format: Array of strings with song suggestions.
    Example: ["Song A from Movie 1", "Song B from Movie 2"]
    """
    suggestions = []
    for tv_show in tv_shows:
        suggestions.append(f"Suggest a song from the movie '{tv_show}'")
    return suggestions

@mcp.prompt()
def suggest_songs_from_books(books: list):
    """
    Suggest songs based on the provided movie titles.
    Return format: Array of strings with song suggestions.
    Example: ["Song A from Movie 1", "Song B from Movie 2"]
    """
    suggestions = []
    for book in books:
        suggestions.append(f"Suggest a song from the book '{book}'")
    return suggestions

@mcp.prompt()
def suggest_songs_from_video_games(video_games: list):
    """
    Suggest songs based on the provided movie titles.
    Return format: Array of strings with song suggestions.
    Example: ["Song A from Movie 1", "Song B from Movie 2"]
    """
    suggestions = []
    for video_game in video_games:
        suggestions.append(f"Suggest a song from the movie '{video_game}'")
    return suggestions

@mcp.prompt()
def suggest_songs_from_movies(albums: list):
    """
    Suggest songs based on the provided movie titles.
    Return format: Array of strings with song suggestions.
    Example: ["Song A from Movie 1", "Song B from Movie 2"]
    """
    suggestions = []
    for album in albums:
        suggestions.append(f"Suggest a song from the movie '{album}'")
    return suggestions

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
    movies = []
    for entity in data['results']['entities']:
        movies.append(entity['name'])

    return movies

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
    tv_shows = []
    for entity in data['results']['entities']:
        tv_shows.append(entity['name'])

    return tv_shows

@mcp.tool()
def get_book_recommendations(genre: str, min_year: int, max_year: int, keyword: str):
    '''
    genre options: "fiction", "science_fiction", "collections", "fantasy", "speculative_fiction", "classics", "science_fiction_fantasy", "criticism", "reference",
    "books_about_books", "literature", "literary_criticism", "short_stories", "anthologies", "horror", "cyberpunk", "time_travel", "post_apocalyptic", "adventure",
    "high_fantasy", "magic", "young_adult", "young_adult_fantasy", "theory"
    '''
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
    books = []
    for entity in data['results']['entities']:
        books.append(entity['name'])
    
    return books

@mcp.tool()
def get_video_game_recommendations(genre: str, min_year: int, max_year: int, keyword: str):
    '''
    genre options: "top_down_shoot_em_up", "action_rpg", "point_click", "fps", "linear_action_adventure", "open_world_action", "defense",
    "survival", "2d_platformer", "virtual_life", "moba", "vertical_shoot_em_up", "party"
    '''
    params = {
        "filter.type": "urn:entity:videogame",
        "filter.tags": f"urn:tag:genre:media:{genre},urn:tag:keyword:media:{keyword}",
        "filter.release_year.min": f"{min_year}",
        "filter.release_year.max": f"{max_year}"
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
    video_games = []
    for entity in data['results']['entities']:
        video_games.append(entity['name'])

    return video_games

@mcp.tool()
def get_albums_from_search(query: str, num_pages: int = 1):
    params = {
        "query": query,
        "types": "urn:entity:album",
        "operator.filter.tags": "union",
        "page": num_pages,
        "sort_by": "match",
    }

    response = requests.get(
        "https://hackathon.api.qloo.com/search",
        headers={
            "accept": "application/json",
            "X-Api-Key": os.getenv("QLOO_API_KEY")
        },
        params=params
    )

    data = response.json()
    albums = []
    for result in data['results']:
        albums.append(result['name'])

    return albums

@mcp.tool()
def get_token():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri='http://127.0.0.1:8000/callback',
        scope='playlist-modify-public playlist-modify-private'
    ))

    access_token = sp.auth_manager.get_access_token(as_dict=False)
    return access_token

@mcp.tool()
def create_playlist(access_token: str, name: str ="My New Playlist", description: str ="Created with VibetuneAI", public: bool = True):
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    data = {
        "name": name,
        "description": description,
        "public": public
    }
    
    response = requests.post(f"https://api.spotify.com/v1/users/6jvibgrfvek4sz1x85zdc9a9v/playlists", headers=headers, data=data)

    return response.json()

@mcp.tool()
def get_songs(access_token: str, q: str, type: str):
    headers = {
        "Authorization": "Bearer " + access_token,
    }
    response = requests.get(f"https://api.spotify.com/v1/search?q={q}&type={type}'", headers=headers)
    
    return response.json()

@mcp.tool()
def insert_songs(access_token: str, song_ids: list, playlist_id, position: int = 0):
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }
    data = {
        "uris": song_ids,
        "position": position
    }


if __name__ == "__main__":
    mcp.run()