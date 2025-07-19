## Overview


## How to set up
1. git clone
2. run `uv venv`
3. run `source .venv/bin/activate`
4. run `uv pip install requests fastmcp python-dotenv`
5. run `python3 server.py`
6. to leave environment run `deactivate`
7. add an .env file under `vibetunemcp/` directory
8. in the .env file add `QLOO_API_KEY=""`, `SPOTIFY_CLIENT_ID=""`, `SPOTIFY_CLIENT_SECRET=""`

## Claude Desktop Integration
1. Open Claude Desktop
2. Go to `Settings` -> `developer` -> `Edit Config`
3. Open up the `claude_desktop_config.json` file
4. add this code: 
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

