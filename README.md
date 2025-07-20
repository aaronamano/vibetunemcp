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
VibetuneMCP is an MCP server that helps generate recommended media titles to the user based on their taste using Qloo’s API and suggesting songs related to the media titles. Afterwards, a new playlist is created and the suggested songs are added to that playlist using Spotify’s API.  Our MCP server will be reliant on using Claude Desktop so users can be able to query and prompt their own preferences.

## How we built it
- <b>FastMCP: </b> This is an Python-based, MCP server framework that I used to build my tools and prompts.
- <b>Qloo Taste AI API: </b> I implemented this API that recommends and generates media titles based from the user’s taste preferences such as genre, year-range, etc.
- <b>Spotify Web API: </b> I used this API to create a new playlist and add songs to that playlist.

## Challenges we ran into
<ol>
<li>Working with Qloo’s API documentation was a challenge since it was highly ambiguous, making it confusing. The list of parameters was overwhelming, and finding which parameters belonged to which primary category seemed tedious. Another challenge was finding what tags existed to help filter certain information since there’s no static list of tags to refer to. Ultimately, I was able to adapt to Qloo’s API documentation and experiment with it.</li>
<li>Another challenge was integrating the MCP tools altogether and executing the process seamlessly from recommending media titles to adding songs to the playlist without any flaws. I was able to embrace the process and overcome it by running multiple trials with Claude.</li>
</ol>

## Accomplishments that we're proud of
I’m proud that I was able to create a functional MCP server that leverages a couple APIs and helps access a third-party app.

## What we learned
I learned about how to implement API routes and call them using Python. More importantly, I learned how to use the FastMCP framework and use it in Claude Desktop.

## What's next for VibetuneMCP
- Developing more accurate search results
- Enhancing prompts
- Allowing users more freedom to control what they want for their playlists
- Creating a dashboard for users to interact with
