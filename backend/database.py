import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
db_name = os.getenv("MONGODB_DB_NAME", "support_db")

client = MongoClient(mongo_uri)
db = client[db_name]

users_col = db["users"]
complaints_col = db["complaints"]
chat_messages_col = db["chat_messages"]
call_sessions_col = db["call_sessions"]
ai_memory_col = db["ai_memory"]
