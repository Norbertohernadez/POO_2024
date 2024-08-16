<<<<<<< HEAD
# crear_tabla.py

import mysql.connector
import conexionbd

def crear_tabla():
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mascotas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    tipo VARCHAR(50) NOT NULL,
                    edad INT,
                    propietario VARCHAR(100)
                )
            """)
            print("Tabla 'mascotas' creada correctamente")
        except mysql.connector.Error as error:
            print(f'Error al crear la tabla: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    crear_tabla()



=======
# crear_tabla.py

import mysql.connector
import conexionbd

def crear_tabla():
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mascotas (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    tipo VARCHAR(50) NOT NULL,
                    edad INT,
                    propietario VARCHAR(100)
                )
            """)
            print("Tabla 'mascotas' creada correctamente")
        except mysql.connector.Error as error:
            print(f'Error al crear la tabla: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    crear_tabla()



>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
