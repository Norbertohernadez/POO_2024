<<<<<<< HEAD
# actualizar_mascota.py

import mysql.connector
import conexionbd

def actualizar_mascota(id_mascota, nombre, tipo, edad, propietario):
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            sql = "UPDATE mascotas SET nombre = %s, tipo = %s, edad = %s, propietario = %s WHERE id = %s"
            valores = (nombre, tipo, edad, propietario, id_mascota)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Registro actualizado correctamente")
        except mysql.connector.Error as error:
            print(f'Error al actualizar registro: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    # Ejemplo de uso de la función para actualizar una mascota por ID
    actualizar_mascota(1, "Milo", "Gato", 3, "Ana García")  # Reemplaza los valores con los nuevos datos de la mascota
=======
# actualizar_mascota.py

import mysql.connector
import conexionbd

def actualizar_mascota(id_mascota, nombre, tipo, edad, propietario):
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            sql = "UPDATE mascotas SET nombre = %s, tipo = %s, edad = %s, propietario = %s WHERE id = %s"
            valores = (nombre, tipo, edad, propietario, id_mascota)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Registro actualizado correctamente")
        except mysql.connector.Error as error:
            print(f'Error al actualizar registro: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    # Ejemplo de uso de la función para actualizar una mascota por ID
    actualizar_mascota(1, "Milo", "Gato", 3, "Ana García")  # Reemplaza los valores con los nuevos datos de la mascota
>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
