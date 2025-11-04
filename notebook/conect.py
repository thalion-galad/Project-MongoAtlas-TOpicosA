from pymongo import MongoClient,errors
from dotenv import load_dotenv
import os

#Cargar variables de entorno
load_dotenv()

MONGO_URI=os.getenv("MONGODB_URI_ATLAS")
DB_NAME_ATLAS=os.getenv("MONGODB_DATA")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME_ATLAS]
    print("Conexión exitosa a Atlas")

except errors.serverSelectionTimeoutError as e:
    print("No se pudo conectar",e)