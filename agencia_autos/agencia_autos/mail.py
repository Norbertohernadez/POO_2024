from autos import Auto
from clientes import Cliente
from revisiones import Revision

def menu_autos():
    while True:
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
                print(auto)

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

def menu_clientes():
    while True:
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
                print(cliente)

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

def menu_revisiones():
    while True:
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
                print(revision)

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

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Gestionar Autos")
        print("2. Gestionar Clientes")
        print("3. Gestionar Revisiones")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            menu_autos()
        elif opcion == '2':
            menu_clientes()
        elif opcion == '3':
            menu_revisiones()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu_principal()
