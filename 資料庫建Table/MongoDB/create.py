from pymongo import MongoClient

uri = "mongodb+srv://<vernonsoio01>:<Hasay2612>@tibame.6s7mb.mongodb.net/<database>?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    db = client.test  # 測試連接
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
