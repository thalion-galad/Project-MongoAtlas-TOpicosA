from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI_ATLAS")
DB_NAME_ATLAS = os.getenv("MONGODB_DATA")

try:
    client = MongoClient(MONGO_URI)
    client.admin.command("ping")   # <-- prueba de autenticación real
    db = client[DB_NAME_ATLAS]
    print("Conexión exitosa a Atlas")

except Exception as e:
    print("Error:", e)
