import urllib.parse
from os import getenv

MONGO_USER = getenv("MONGO_USER")
MONGO_CLUSTER = getenv("MONGO_CLUSTER")
MONGO_PASSWORD = getenv("MONGO_PASSWORD")
MONGO_DATABASE = getenv("MONGO_DATABASE")
MONGO_COLLECTION = getenv("MONGO_COLLECTION")

TOKEN = getenv("BOT_TOKEN")
TRUSTED_USERS = [
    int(getenv("TRUSTED_USER")),
]