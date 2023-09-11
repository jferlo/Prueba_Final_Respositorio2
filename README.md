## **Prueba\_Final\_Repositorio\_2**

**Elaborado por:** Juan Fernando López

**Fecha de elaboración:** 2023/09/09

## **Indicaciones del Repositorio**

Contiene el código relacionado con el servicio web para consultar la base de datos y mostrar algún resultado.

### **Objetivos:**

*   Consultar la información almacenada en Mongo Db.
*   Habilitar un APi para vizualizar los datos almacenados en MongoDB
*   Elaborar un codigo en python que nos permita obtener la informacion almacenada en mongoDB, para posteriormente ser vizualizados en un navegador.

### **Metodologia**:

#### Software

Para el desarrollo de este proyecto es importante instalar un IDE para poder trabajar con python, en este caso el IDE elegido es PyCharm, ya que tiene una interfaz muy amigable y es de facil manejo. Tambien es necesario instalara las diferentes librerias necesarias para la ejecucion del codigo y dado que se trabajó con tecnicas de webscraping es importante instalar el web driver del navegador que se utiliza.

Para el almacenamiento de los datos obtenidos se ha credo una cuenca en nube de MongoDB .

#### Desarrollo

Con el objetivo de tener un control de versiones del presente proyecto se ha credo un repositorio en GitHub, el cual ha side conectado con Python de monera que conforme se avanza en el proyecto se van documentando los cambios que ha sufrido nuestro trabajo, lo que nos permit tener una trazabilidad de proceso.

Una vez que se triene el repositorio creado y vinculado a python es recomendable un habilitar el entorno virtual de python para este proyecto. ya que nos permitira restringir la visualización de información sencible como links de acceso, usuarios y contraseñas.

En la siguiente imagen se resume el funcionamiento de este codigo, el cual a traves del uso de flask, google chrome, es posible mostrar en pantalla uno de los registros almacenados en MongoDB

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/a23c3fa01c76d37aa6bbd04811d4ed14d07b5d1cdb327244.png)

**Fig 1.- Diagrama de funcionamiento del codigo**

Para empezar a construir nuestro codigo es importante crear un archivo llamado **“requirements.txt”** ya que aqui vamos a definir cuales son esos paquetes que requerimos de para trabajar dentro de Python, a continuacion se muestra su contenido.

```python
flask
pymongo
python-dotenv
```

Se crea un archivo **“apimongo.py”**  el cual va a contener el codigo que realizara la consulta y proyeccion en pantalla de la informacion contenida en Mongo DB. 

```python
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
```

Ya que hemos elaborado el codigo de tal manera que las contraseñas no queden expuestas, se crea un archivo llamado “.env”, el se añade al directorio venv, el cual no se almacena en github.

```python
MONGO_USER=<username>
MONGO_PASSWORD=<password>
MONGO_HOSTNAME=cluster0.xxxxxx.mongodb.net
```

#### **Pruebas de Funcionamiento**

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/cac86db7f528ccb6170980fc91c55cf725b028f491996a20.png)

**Fig 2.- Busqueda exitosa**

### **Puntos de mejora.**

En esta parte de proyecto, pus en evidencia que los conocimiento en el manejo de python aun se deben fortalecer, ya eso limitó powder proyectar en pantalla del navegador un mayor numero de registros almacenados en MongoDb.
