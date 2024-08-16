# conexionbd.py

import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        print("Conexión establecida correctamente")
        return conexion
    except mysql.connector.Error as error:
        print(f'Error al conectar con la base de datos: {error}')
        return None




