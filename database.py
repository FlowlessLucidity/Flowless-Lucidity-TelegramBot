from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from secrets import *

class Database:
    def __init__(self):
        self.uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}.mpm8hbk.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = AsyncIOMotorClient(self.uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            self.db = self.client[MONGO_DATABASE]
            self.collection = self.db[MONGO_COLLECTION]
        except Exception as e:
            print(e)

    async def get_random_dream(self):
        data = await self.collection.aggregate([{"$sample": {"size": 1}}]).to_list(length=None)
        return data[0]
    async def set_new_dream(self, approved_dream: dict):
        await self.collection.insert_one(approved_dream)



