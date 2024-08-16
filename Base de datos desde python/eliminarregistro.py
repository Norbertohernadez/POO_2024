<<<<<<< HEAD
# eliminar_mascota_por_id.py

import mysql.connector
import conexionbd

def eliminar_mascota_por_id(id_mascota):
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            sql = "DELETE FROM mascotas WHERE id = %s"
            cursor.execute(sql, (id_mascota,))
            conexion.commit()
            print("Registro eliminado correctamente")
        except mysql.connector.Error as error:
            print(f'Error al eliminar registro: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    # Ejemplo de uso de la función para eliminar una mascota por ID
    eliminar_mascota_por_id(1)  # Reemplaza 1 con el ID de la mascota que deseas eliminar


=======
# eliminar_mascota_por_id.py

import mysql.connector
import conexionbd

def eliminar_mascota_por_id(id_mascota):
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            sql = "DELETE FROM mascotas WHERE id = %s"
            cursor.execute(sql, (id_mascota,))
            conexion.commit()
            print("Registro eliminado correctamente")
        except mysql.connector.Error as error:
            print(f'Error al eliminar registro: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    # Ejemplo de uso de la función para eliminar una mascota por ID
    eliminar_mascota_por_id(1)  # Reemplaza 1 con el ID de la mascota que deseas eliminar


>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
