<<<<<<< HEAD
# crear_base_datos.py

import mysql.connector
import conexionbd

def crear_base_datos():
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS registro_mascotas")
            print("Base de datos 'registro_mascotas' creada correctamente")
        except mysql.connector.Error as error:
            print(f'Error al crear la base de datos: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    crear_base_datos()
=======
# crear_base_datos.py

import mysql.connector
import conexionbd

def crear_base_datos():
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS registro_mascotas")
            print("Base de datos 'registro_mascotas' creada correctamente")
        except mysql.connector.Error as error:
            print(f'Error al crear la base de datos: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    crear_base_datos()
>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
