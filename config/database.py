from pymongo.mongo_client import MongoClient
import ssl

uri = ""

client = MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)

db = client.todo_db

collection_name = db["todo_collection"]