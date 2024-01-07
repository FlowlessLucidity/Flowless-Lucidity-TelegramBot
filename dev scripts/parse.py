import json
import re
from pymongo import MongoClient
import datetime


dream_diary_txt = open("Dream Diary.txt", "r", encoding="utf-8").read().split("\n\n")
dream_diary_dict = {}
client = MongoClient("mongodb://localhost:27017/")
db = client["Flowless_Lucidity"]
collection = db["Dream_Journal"]

for dream in dream_diary_txt[:]:
    collection.insert_one(
        {
            "date": datetime.datetime.strptime(dream.split("\n")[0], "%d.%m.%y"),
            "location": None,
            "feelings": None,
            "vision": None,
            "subjective sleep duration": None,
            "sleep start": None,
            "sleep end": None,
            "number of REM phases": None,
            "dream type": None,
            "sleep type": None,
            "dream": dream[dream.index("\n") + 1:].strip(),
        }
    )
    print(dream.split("\n")[0], "done")
