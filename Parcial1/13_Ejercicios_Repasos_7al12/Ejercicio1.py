#Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

import os
import msvcrt

numeros_lista=[34, 40, 3, 1, 0, 78, 34, 5]

def RecorreLista():
    for x in numeros_lista:
        print(x)
    return x

def BuscarLista():
    num=int(input("Ingrese el número entero a buscar: "))  # Convertir entrada a entero
    posiciones=[i for i, x in enumerate(numeros_lista) if x == num]  # LISTA DE COMPRENSION -
    
    if posiciones:
        print(f"{num} está en la lista en las posiciones: {posiciones}")
    else:
        print(f"{num} no está en la lista.")


    
  

baibai=True
while baibai:
    os.system("cls")
    print("\tMANIPULACIÓN DE LISTA \n a) RECORRER LISTA \n b) ORDENARLA \n c) LONGITUD\n d) BUSCAR ELEMENTOS\n e)SALIR")

    opcion=input("Eliga una opción para continuar: ").upper()
   


    if opcion=="A":
        os.system("cls")
        print("\t ¡MOSTRARÉ LA LISTA RECORRIDA!")
        RecorreLista()
        print("Presione cualquier tecla para continuar....")
        msvcrt.getch()

    if opcion=="B":
        os.system("cls")
        print("\t ¡MOSTRARE LA LISTA ORDENADA!")
        numeros_lista.sort()
        print(numeros_lista)
        print("Presione cualquier tecla para continuar....")
        msvcrt.getch()

    if opcion=="C":
        os.system("cls")
        print("¡MOSTRARÉ LA LONGITUD DE LA LISTA!")
        print(f"Longitud de : {len(numeros_lista)}")
        print("Presione cualquier tecla para continuar....")
        msvcrt.getch()
    

    if opcion=="D":
        os.system("cls")
        print("¡BUSCARÉ EL NUMERO QUE DESEES!")
        BuscarLista()
        print("Presione cualquier tecla para continuar....")
        msvcrt.getch()
    
    if opcion=="E":
        os.system("cls")
        print("Ejecución terminada")
        baibai=False