import os
import platform

def borrar_pantalla():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')
def esperar_tecla():
    input("Presiona Enter para continuar...")
