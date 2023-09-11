from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()
user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
hostname = os.getenv('MONGO_HOSTNAME')
uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"



mongo_client = MongoClient(uri, server_api=ServerApi('1'))
mi_db = mongo_client.get_database('db_prueba_final')
mi_coleccion = mi_db.get_collection('Juan Fernando_inmuebles')

def insertar_data():
    mi_task = {"nombre":"Juan Fer","edad":" 34 años"}
    mi_coleccion.insert_one(mi_task)

app = Flask(__name__)
#def leer_data():
@app.route("/api/db")
def get_database_info():
    resultado = mi_coleccion.find()
    for x in resultado:
        del x['_id']
        return {"datos":x}
        #print ({"datos":x})
#leer_data()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)

