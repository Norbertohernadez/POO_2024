from conexion import create_connection, close_connection

class Cabana:
    def __init__(self, id_cabana, nombre, capacidad, costo_por_noche, disponible):
        self.id_cabana = id_cabana
        self.nombre = nombre
        self.capacidad = capacidad
        self.costo_por_noche = costo_por_noche
        self.disponible=disponible

    @staticmethod
    def crear(nombre, capacidad, costo_por_noche, disponible=True):  # disponible=True por defecto
        cursor, connection = create_connection()
        if cursor and connection:
            query = """
            INSERT INTO Cabana (nombre, capacidad, costo_por_noche, disponible)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, capacidad, costo_por_noche, disponible))
            connection.commit()
            id_cabana = cursor.lastrowid
            close_connection(connection, cursor)
            return Cabana(id_cabana, nombre, capacidad, costo_por_noche, disponible)
        else:
            print("No se pudo establecer la conexión con la base de datos.")


    @staticmethod
    def leer(id_cabana):
        cursor, connection = create_connection()
        if cursor and connection:
            query = "SELECT * FROM Cabana WHERE id_cabana = %s"
            cursor.execute(query, (id_cabana,))
            data = cursor.fetchone()
            close_connection(connection, cursor)
            if data:
                return Cabana(*data)
            else:
                print("Cabaña no encontrada.")
                return None
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return None

    def actualizar(self, nombre=None, capacidad=None, costo_por_noche=None, disponible=None):
        cursor, connection = create_connection()
        if cursor and connection:
            query = """
            UPDATE Cabana
            SET nombre = COALESCE(%s, nombre),
                capacidad = COALESCE(%s, capacidad),
                costo_por_noche = COALESCE(%s, costo_por_noche),
                disponible = COALESCE(%s, disponible)
            WHERE id_cabana = %s
            """
            cursor.execute(query, (nombre, capacidad, costo_por_noche, disponible, self.id_cabana))
            connection.commit()
            close_connection(connection, cursor)
            print("Cabaña actualizada con éxito.")
        else:
            print("No se pudo establecer la conexión con la base de datos.")

    @staticmethod
    def eliminar(id_cabana):
        cursor, connection = create_connection()
        if cursor and connection:
            query = "DELETE FROM Cabana WHERE id_cabana = %s"
            cursor.execute(query, (id_cabana,))
            connection.commit()
            close_connection(connection, cursor)
            print("Cabaña eliminada con éxito.")
        else:
            print("No se pudo establecer la conexión con la base de datos.")

    @staticmethod
    def getAll():
        cursor, connection = create_connection()
        if cursor and connection:
            query = "SELECT * FROM Cabana"
            cursor.execute(query)
            data = cursor.fetchall()
            close_connection(connection, cursor)
            return [Cabana(*row) for row in data]
        else:
            print("No se pudo establecer la conexión con la base de datos.")
            return []
