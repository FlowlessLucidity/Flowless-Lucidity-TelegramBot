from os import getenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse


MONGO_USER = urllib.parse.quote(getenv("MONGO_USER"), safe='/', encoding="utf-8", errors=None)
MONGO_CLUSTER = urllib.parse.quote(getenv("MONGO_CLUSTER"), safe='/', encoding="utf-8", errors=None)
MONGO_PASSWORD = urllib.parse.quote(getenv("MONGO_PASSWORD"), safe='/', encoding="utf-8", errors=None)

uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.mpm8hbk.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
