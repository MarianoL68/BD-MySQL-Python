#📌MANEJO DE BASE DE DATOS CON PYTHON PARTE 1

from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")

#Configuración

import mysql.connector

#Realizamos la conexión ingrsando el user y 
#password definidos en WAMP
mydb = mysql.connector.connect(
    host = "localhost",
    user = db_user,
    password = db_password
)

print(mydb)
#La salida de la consola debería ser algo como:
# <mysql.connector.connection_cext.CMySQLConnection object at 0x000001DCA710F090>