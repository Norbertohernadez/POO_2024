from clientes import Cliente
from revisiones import Revision
from usuarios import Usuario
from autos import Auto 
import os
import platform
import getpass

def borrar_pantalla():
    """Limpia la pantalla de la terminal."""
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def esperar_tecla():
    """Espera a que el usuario presione Enter para continuar."""
    input("Presiona Enter para continuar...")

def gestionar_usuarios():
    """Gestión de usuarios: insertar, consultar, actualizar y eliminar."""
    while True:
        borrar_pantalla()
        print("\n--- Gestión de Usuarios ---")
        print("1. Insertar nuevo usuario")
        print("2. Consultar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del usuario: ")
            correo = input("Correo del usuario: ")
            contrasena = getpass.getpass("Contraseña del usuario: ")
            usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena)
            usuario.insertar()
            print("Usuario insertado exitosamente.")
        
        elif opcion == '2':
            usuarios = Usuario.consultar()
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}")
        
        elif opcion == '3':
            correo = input("Correo del usuario a actualizar: ")
            nombre = input("Nombre (dejar en blanco para no actualizar): ")
            contrasena = getpass.getpass("Contraseña (dejar en blanco para no actualizar): ")
            Usuario.actualizar(correo, nombre if nombre else None, contrasena if contrasena else None)
            print("Usuario actualizado exitosamente.")
        
        elif opcion == '4':
            correo = input("Correo del usuario a eliminar: ")
            Usuario.eliminar(correo)
            print("Usuario eliminado exitosamente.")
        
        elif opcion == '5':
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        esperar_tecla()

def menu_autos():
    """Gestión de autos: insertar, consultar, actualizar y eliminar."""
    while True:
        borrar_pantalla()
        print("\nGestión de Autos")
        print("1. Insertar Auto")
        print("2. Consultar Autos")
        print("3. Actualizar Auto")
        print("4. Eliminar Auto")
        print("5. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            matricula = input("Matrícula: ")
            marca = input("Marca: ")
            modelo = int(input("Modelo: "))
            color = input("Color: ")
            nif = int(input("NIF del cliente (puede no existir en la tabla clientes): "))
            auto = Auto(matricula, marca, modelo, color, nif)
            auto.insertar()
            print("Auto insertado exitosamente.")
        
        elif opcion == '2':
            autos = Auto.consultar()  
            for auto in autos:
                print(f"Matrícula: {auto[0]}, Marca: {auto[1]}, Modelo: {auto[2]}, Color: {auto[3]}, NIF Cliente: {auto[4]}")
        
        elif opcion == '3':
            matricula = input("Matrícula del auto a actualizar: ")
            marca = input("Marca (dejar en blanco para no actualizar): ")
            modelo = input("Modelo (dejar en blanco para no actualizar): ")
            color = input("Color (dejar en blanco para no actualizar): ")
            nif = input("NIF del cliente (dejar en blanco para no actualizar): ")

            Auto.actualizar(matricula, marca if marca else None, int(modelo) if modelo else None, color if color else None, int(nif) if nif else None)
            print("Auto actualizado exitosamente.")
        
        elif opcion == '4':
            matricula = input("Matrícula del auto a eliminar: ")
            Auto.eliminar(matricula)
            print("Auto eliminado exitosamente.")
        
        elif opcion == '5':
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        esperar_tecla()

def menu_clientes():
    """Gestión de clientes: insertar, consultar, actualizar y eliminar."""
    while True:
        borrar_pantalla()
        print("\nGestión de Clientes")
        print("1. Insertar Cliente")
        print("2. Consultar Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nif = int(input("NIF: "))
            nombre = input("Nombre: ")
            direccion = input("Dirección: ")
            ciudad = input("Ciudad: ")
            tel = int(input("Teléfono: "))
            cliente = Cliente(nif, nombre, direccion, ciudad, tel)
            cliente.insertar()
            print("Cliente insertado exitosamente.")
        
        elif opcion == '2':
            clientes = Cliente.consultar()
            for cliente in clientes:
                print(f"NIF: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Ciudad: {cliente[3]}, Teléfono: {cliente[4]}")
        
        elif opcion == '3':
            nif = int(input("NIF del cliente a actualizar: "))
            nombre = input("Nombre (dejar en blanco para no actualizar): ")
            direccion = input("Dirección (dejar en blanco para no actualizar): ")
            ciudad = input("Ciudad (dejar en blanco para no actualizar): ")
            tel = input("Teléfono (dejar en blanco para no actualizar): ")

            Cliente.actualizar(nif, nombre if nombre else None, direccion if direccion else None, ciudad if ciudad else None, int(tel) if tel else None)
            print("Cliente actualizado exitosamente.")
        
        elif opcion == '4':
            nif = int(input("NIF del cliente a eliminar: "))
            Cliente.eliminar(nif)
            print("Cliente eliminado exitosamente.")
        
        elif opcion == '5':
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        esperar_tecla()

def menu_revisiones():
    """Gestión de revisiones: insertar, consultar, actualizar y eliminar."""
    while True:
        borrar_pantalla()
        print("\nGestión de Revisiones")
        print("1. Insertar Revisión")
        print("2. Consultar Revisiones")
        print("3. Actualizar Revisión")
        print("4. Eliminar Revisión")
        print("5. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            no_revision = int(input("Número de revisión: "))
            cambiofiltro = input("Cambio de filtro (S/N): ")
            cambioaceite = input("Cambio de aceite (S/N): ")
            cambiofrenos = input("Cambio de frenos (S/N): ")
            otros = input("Otros detalles: ")
            matricula = input("Matrícula del auto: ")
            revision = Revision(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
            revision.insertar()
            print("Revisión insertada exitosamente.")
        
        elif opcion == '2':
            revisiones = Revision.consultar()
            for revision in revisiones:
                print(f"Número de Revisión: {revision[0]}, Filtro: {revision[1]}, Aceite: {revision[2]}, Frenos: {revision[3]}, Otros: {revision[4]}, Matrícula: {revision[5]}")
        
        elif opcion == '3':
            no_revision = int(input("Número de revisión a actualizar: "))
            cambiofiltro = input("Cambio de filtro (dejar en blanco para no actualizar): ")
            cambioaceite = input("Cambio de aceite (dejar en blanco para no actualizar): ")
            cambiofrenos = input("Cambio de frenos (dejar en blanco para no actualizar): ")
            otros = input("Otros detalles (dejar en blanco para no actualizar): ")
            matricula = input("Matrícula del auto (dejar en blanco para no actualizar): ")

            Revision.actualizar(no_revision, cambiofiltro if cambiofiltro else None, cambioaceite if cambioaceite else None, cambiofrenos if cambiofrenos else None, otros if otros else None, matricula if matricula else None)
            print("Revisión actualizada exitosamente.")
        
        elif opcion == '4':
            no_revision = int(input("Número de revisión a eliminar: "))
            Revision.eliminar(no_revision)
            print("Revisión eliminada exitosamente.")
        
        elif opcion == '5':
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        esperar_tecla()

def menu_secundario():
    """Menú secundario para gestionar autos, clientes, revisiones y usuarios."""
    while True:
        borrar_pantalla()
        print("\nMenú Secundario")
        print("1. Gestión de Autos")
        print("2. Gestión de Clientes")
        print("3. Gestión de Revisiones")
        print("4. Gestión de Usuarios")
        print("5. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            menu_autos()
        
        elif opcion == '2':
            menu_clientes()
        
        elif opcion == '3':
            menu_revisiones()
        
        elif opcion == '4':
            gestionar_usuarios()
        
        elif opcion == '5':
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        esperar_tecla()

def iniciar_sesion():
    """Realiza la autenticación del usuario y permite el acceso a las funcionalidades del sistema si es correcto."""
    borrar_pantalla()
    print("\n--- Iniciar Sesión ---")
    correo = input("Correo electrónico: ")
    contrasena = getpass.getpass("Contraseña: ")

    if Usuario.validar_usuario(correo, contrasena):
        print("Inicio de sesión exitoso!")
        return True
    else:
        print("Credenciales incorrectas. Inténtalo de nuevo.")
        return False

def registrarse():
    """Registra un nuevo usuario en el sistema."""
    borrar_pantalla()
    print("\n--- Registrarse ---")
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    contrasena = getpass.getpass("Contraseña: ")
    confirmacion_contrasena = getpass.getpass("Confirmar contraseña: ")

    if contrasena != confirmacion_contrasena:
        print("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")
        return False
    
    # Verifica si el correo ya está registrado
    if Usuario.obtener_por_id(correo):
        print("El correo electrónico ya está registrado.")
        return False
    
    # Registra el nuevo usuario
    usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena)
    usuario.insertar()
    print(f"Registro exitoso para {nombre}. Puedes iniciar sesión ahora.")
    return True

def menu_principal():
    """Menú principal del sistema."""
    while True:
        borrar_pantalla()
        print("\n--- Menú Principal ---")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            if iniciar_sesion():
                menu_secundario()
        
        elif opcion == '2':
            if registrarse():
                menu_secundario()
        
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        
        esperar_tecla()

if __name__ == "__main__":
    menu_principal()
