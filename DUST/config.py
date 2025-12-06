import os, dotenv

dotenv.load_dotenv() ## Load enviroment variables.

### Bot Info
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
LINKTREE_URL = os.getenv("LINKTREE_URL")
INVITE_URL = os.getenv("INVITE_URL")
SUPPORT_SERVER_URL = os.getenv("SUPPORT_SERVER_URL")

###IEX CLoud Api INfo
IEX_TOKEN = os.getenv("IEX_TOKEN")

#### OpenChat Api Info
CHAT_GPT = os.getenv("CHATGPT")

### Lavalink Server Info
LAVALINK_HOST = os.getenv("LAVAHOST")
LAVALINK_PORT = os.getenv("LAVAPORT")
LAVALINK_PASS = os.getenv("LAVAPASS")

### Spotify Credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTCLIENT")
SPOTIFY_TRENDING_ID = os.getenv("SPOTIFY_TRENDING_ID") ## The playlist ID used to retrieve trending tracks.

### Genius Credentials
GENIUS_API_KEY = os.getenv("GENIUSKEY")

### Logging
LOGGING_CHANNEL_ID = os.getenv("LOGID")

### Imgur
IMGUR_CLIENT_ID =os.getenv("IMGUR_CLIENT_ID")
IMGUR_SECERT = os.getenv("IMGUR_SECERT")

#### Google
GOOGLE_API = os.getenv("GOOGLE_API")

### Search Engine ID
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")