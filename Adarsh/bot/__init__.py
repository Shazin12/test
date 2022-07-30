# (c) adarsh-goel
from pyrogram import Client
from vars import Var

StreamBot = Client(
    # session_name='Web Streamer',
    name="test_bot",
    api_id=18676426,
    api_hash="45257961980184a76d3ded65e31955ae",
    bot_token="5342549328:AAGIBbyiNd1-38XO_DDgb6IwKUZhZiWFCiE",
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
