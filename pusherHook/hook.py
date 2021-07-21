import pusher
import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def initlizePusherClinet():
    return pusher.Pusher(
        app_id=os.getenv('PUSHER_APP_ID'),
        key=os.getenv('PUSHER_API_KEY'),
        secret=os.getenv('PUSHER_SECRET'),
        cluster=os.getenv('PUSHER_CLUSTER'),
        ssl=True
    )
