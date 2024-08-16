<<<<<<< HEAD
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




=======
# conexionbd.py

import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña"
        )
        print("Conexión establecida correctamente")
        return conexion
    except mysql.connector.Error as error:
        print(f'Error al conectar con la base de datos: {error}')
        return None




>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
