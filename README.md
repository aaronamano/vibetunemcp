## How to set up
1. git clone
2. run `uv venv`
3. run `source .venv/bin/activate`
4. run `uv pip install requests fastmcp python-dotenv spotipy`
5. to leave environment run `deactivate`
6. add an .env file under `vibetunemcp/` directory
7. in the .env file add `QLOO_API_KEY=""`, `SPOTIFY_CLIENT_ID=""`, `SPOTIFY_CLIENT_SECRET=""`

## Claude Desktop Integration
1. Open Claude Desktop
2. Go to `Settings` -> `developer` -> `Edit Config`
3. Open up the `claude_desktop_config.json` file
4. add this code and make sure to save it: 
```json
{
  "mcpServers": {
    "VibetuneMCP": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/<username>/Desktop/vibetunemcp", //the path where you git cloned the project
        "run",
        "server.py"
      ]
    }
  }
}
```
5. Quit Claude Desktop and reopen it
6. Voila!

## Inspiration
Music unites people from around the world—we listen, talk, share, debate, sing music. Thankfully we have Spotify that lets people express their music taste, connect with people, and collaborate together in making a playlist. Playlists, are more than just songs. They’re people’s personalities, preferences, moods, feelings, and importantly identities. What if I tell you I can take recommended media and interests (such as movies, TV shows, books, video games) from your taste preferences into a Spotify playlist? It’s a single playlist that portrays your entire life as music.

## What it does
VibetuneMCP is an MCP server that helps generate recommended media titles to the user based on their taste preferences using Qloo’s API and suggesting songs related to the media titles. Afterwards, a new playlist is created and the suggested songs are added to that playlist using Spotify’s API.  My MCP server will be reliant on using Claude Desktop so users can be able to query and prompt their own preferences.

## How we built it
I created my MCP server using FastMCP, a Python-based framework that—builds MCP servers. I built several MCP tools as well as a couple MCP prompt templates. In my MCP tools I leveraged Qloo’s Taste AI API, which generates media recommendations from the user’s taste preferences (favorite genre, year-range, keywords, etc.); I implemented Spotify’s Web API, which creates a new playlist, gets song URIs, and add songs into playlists.

<h4>MCP Tools</h4>
The first 5 tools use Qloo’s Taste AI API
- `get_movie_recommendations`: Generates movie recommendations based on the user’s preferred genre, keyword, year-range, and content rating.
- `get_tv_show_recommendations`: Generates tv show recommendations based on the user’s preferred genre, keyword, year-range, and content rating.
- `get_book_recommendations`: Generates book recommendations based on the user’s preferred genre, keyword, and year-range.
- `get_video_game_recommendations`: Generates video game recommendations based on the user’s preferred genre, keyword, and year-range.
- `get_albums_from_search`: Generates albums associated with the user’s specific-based search query (ex. Beyonce, Iron Man, Barbie Movie, etc.). The user can also control how much generated content they want to receive (number of pages in this case).

The last 4 tools use Spotify’s Web API
- `get_token`: Authenticates the Spotify user through a callback URI and generates a token that’ll be used for calling the Spotify API.
- `create_playlist`: Creates the playlist itself based on the user’s input (name of playlist, description of playlist, option to make it public or private) and returns the playlist id.
- `get_songs`: Gets recommended songs from the prompt template’s response and obtains the URI for each track.
- `insert_songs`: Inserts the list of URIs into the playlist. The playlist is accessed and obtained by passing the playlist id in this tool.

<h4>MCP Prompts</h4>
These are prompt templates that suggest songs related to recommended media from Qloo’s API
- `suggest_songs_from_books`: After getting a recommended list books, the user inputs the list into the prompt template. The LLM suggests a song related or associated with each book in the list.
- `suggest_songs_from_movies`: After getting a recommended list of movies, the user inputs the list into the prompt template. The LLM suggests a song related or associated with each movie in the list.
- `suggest_songs_from_tv_shows`: After getting a recommended list of tv shows, the user inputs the list into the prompt template. The LLM suggests a song related or associated with each tv show in the list.
- `suggest_songs_from_video_games`: After getting a recommended list of video games, the user inputs the list into the prompt template. The LLM suggests a song related or associated with each video game in the list.

## Challenges we ran into
<ol>
<li>Working with Qloo’s API documentation was a challenge since it was highly ambiguous, creating confusion. The list of parameters was overwhelming, and finding which parameters belonged to which category seemed tedious. Another challenge was finding what tags existed to help filter certain information since there’s no static list of tags to refer to. Ultimately, I was able to adapt to Qloo’s API documentation and experiment with it a lot.</li>
<li>Another challenge was integrating the MCP tools altogether and executing the process seamlessly from recommending media titles to adding songs to the playlist without any flaws. I was able to embrace the process and overcome it by running multiple trials with Claude.</li>
<li>A minor obstacle I was facing was that whenever the song URIs were being inserted into the playlist, it would be successful. However, when I look in my Spotify account, the playlist was created, but the songs are not there. At times, this can be annoying and problematic. I’m still investigating into it and refining my tools ensuring this doesn’t happen and that it’s consistent.</li>
</ol>

## Accomplishments that I'm proud of
I’m proud that I was able to create a functional MCP server that leverages a couple APIs and helps access a third-party app.

## What I learned
I learned about how to implement API routes and call them using Python. More importantly, I learned how to develop with the FastMCP framework and integrate it in Claude Desktop.

## What's next for VibetuneMCP
- Developing more accurate search results
- Enhancing prompts
- Allowing users more freedom to control what they want for their playlists (more input parameters)
- Creating a dashboard for users to interact with
