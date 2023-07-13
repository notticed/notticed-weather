# the connection was copied from mongo docs
from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb+srv://sample:Poher_123@cluster0.zcsjtwf.mongodb.net/"
client = MongoClient(uri)
db = client['sample_mflix']


users_weather = db['users_weather']



