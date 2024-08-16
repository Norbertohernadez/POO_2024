<<<<<<< HEAD
# seleccionar_mascotas.py

import mysql.connector
import conexionbd

def seleccionar_mascotas():
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM mascotas")
            registros = cursor.fetchall()
            if registros:
                for mascota in registros:
                    print(mascota)
            else:
                print("No hay registros de mascotas")
        except mysql.connector.Error as error:
            print(f'Error al seleccionar registros: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    seleccionar_mascotas()


=======
# seleccionar_mascotas.py

import mysql.connector
import conexionbd

def seleccionar_mascotas():
    conexion = conexionbd.conectar()
    
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM mascotas")
            registros = cursor.fetchall()
            if registros:
                for mascota in registros:
                    print(mascota)
            else:
                print("No hay registros de mascotas")
        except mysql.connector.Error as error:
            print(f'Error al seleccionar registros: {error}')
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer conexión con la base de datos")

# Llama a la función principal
if __name__ == "__main__":
    seleccionar_mascotas()


>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
