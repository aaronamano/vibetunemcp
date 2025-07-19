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
    movies = []
    for entity in data['results']['entities']:
        movies.append(entity['name'])

    return movies

@mcp.prompt()
def suggest_songs_from_movies(movies: list):
    """
    Suggest songs based on the provided movie titles.
    """
    suggestions = []
    for movie in movies:
        suggestions.append(f"Suggest a song from the movie '{movie}'")
    return suggestions

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
def get_qloo_search_results(query: str, num_pages: int = 1):
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