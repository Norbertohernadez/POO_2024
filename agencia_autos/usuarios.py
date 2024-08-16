from conexionBD import ConexionDB

class Usuario:
    def __init__(self, id=None, nombre=None, correo=None, contrasena=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def insertar(self):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)"
                valores = (self.nombre, self.correo, self.contrasena)
                cursor.execute(sql, valores)
                conexion.commit()
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
        finally:
            ConexionDB().cerrar_conexion(conexion)

    @staticmethod
    def consultar():
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios")
                resultado = cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar usuarios: {e}")
            resultado = []
        finally:
            ConexionDB().cerrar_conexion(conexion)
        return resultado

    @staticmethod
    def obtener_por_id(correo):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
                resultado = cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener usuario por correo: {e}")
            resultado = None
        finally:
            ConexionDB().cerrar_conexion(conexion)
        return resultado

    @staticmethod
    def validar_usuario(correo, contrasena):
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s", (correo, contrasena))
                resultado = cursor.fetchone()
        except Exception as e:
            print(f"Error al validar usuario: {e}")
            resultado = None
        finally:
            ConexionDB().cerrar_conexion(conexion)
        return resultado is not None

    @staticmethod
    def actualizar(correo, nombre=None, contrasena=None):
        set_clause = []
        valores = []

        if nombre:
            set_clause.append("nombre = %s")
            valores.append(nombre)
        if contrasena:
            set_clause.append("contrasena = %s")
            valores.append(contrasena)

        if not set_clause:
            raise ValueError("No se proporcionaron valores para actualizar.")

        set_clause_str = ", ".join(set_clause)
        sql = f"UPDATE usuarios SET {set_clause_str} WHERE correo = %s"
        valores.append(correo)

        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, tuple(valores))
                conexion.commit()
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
        finally:
            ConexionDB().cerrar_conexion(conexion)

    @staticmethod
    def eliminar(correo):
        sql = "DELETE FROM usuarios WHERE correo = %s"
        conexion = ConexionDB().conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute(sql, (correo,))
                conexion.commit()
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
        finally:
            ConexionDB().cerrar_conexion(conexion)


