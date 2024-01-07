import urllib.parse
from os import getenv

MONGO_USER = urllib.parse.quote(getenv("MONGO_USER"), safe='/', encoding="utf-8", errors=None)
MONGO_CLUSTER = urllib.parse.quote(getenv("MONGO_CLUSTER"), safe='/', encoding="utf-8", errors=None)
MONGO_PASSWORD = urllib.parse.quote(getenv("MONGO_PASSWORD"), safe='/', encoding="utf-8", errors=None)
MONGO_DATABASE = getenv("MONGO_DATABASE")
MONGO_COLLECTION = getenv("MONGO_COLLECTION")

TOKEN = getenv("BOT_TOKEN")
TRUSTED_USERS = [
    int(getenv("TRUSTED_USER")),
]