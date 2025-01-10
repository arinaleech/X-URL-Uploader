import os
from pyrogram.types import BotCommand
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    BOT_COMMANDS = [
        BotCommand('start', 'start bot'),
        BotCommand('help', 'help message'),
        BotCommand('caption', 'custom caption'),
        BotCommand('thumbnail', 'custom thumbnail'),
        BotCommand('ban', 'ban user'),
        BotCommand('unban', 'unban user'),
        BotCommand('broadcast', 'broadcast message')
    ]

    DUMP_ID = int(os.environ.get("DUMP_ID", 0))

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7619169027:AAG33n3Em3vicp48ADx1_uE80bNZLcbZgSA")

    APP_ID = int(os.environ.get("APP_ID", "21894814"))
    API_HASH = os.environ.get("API_HASH","4366bdf6ed33089c363df8e4d7b9a1b5f0a88")

    # Authorized User IDS
    AUTH_USERS = [int(id) for id in os.environ.get(
        "AUTH_USERS", "5071005351").split()] if os.environ.get("AUTH_USERS", None) else None

    OWNER_ID = int(os.environ.get('OWNER_ID'))

    # MongoDB
    DATABASE_URL = os.environ.get("mongodb+srv://ndjdn6062:QrBljgOpVLbSBeSr@cluster0.f0a88.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    # watermark file
    DEF_WATER_MARK_FILE = "💋"

    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000

    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
