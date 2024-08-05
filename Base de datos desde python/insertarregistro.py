# insertar_mascota.py

import mysql.connector
import conexionbd

def insertar_mascota(nombre, tipo, edad, propietario):
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            sql = "INSERT INTO mascotas (nombre, tipo, edad, propietario) VALUES (%s, %s, %s, %s)"
            valores = (nombre, tipo, edad, propietario)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Registro insertado correctamente")
        except mysql.connector.Error as error:
            print(f'Error al insertar registro: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    # Ejemplo de uso de la función para insertar una mascota
    insertar_mascota("Milo", "Perro", 5, "Juan Pérez")


