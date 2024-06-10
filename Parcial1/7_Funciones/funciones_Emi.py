#Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple un funcion especifica. La funcion se puede reutilizar con sinple escho de invocarla es decir mandarla llamar

#Sintaxis

#def nombredeMifuncion(parametros):
    #bloque o conjunto de instrucciones 

#nombredeMifuncion(parametros)

#La funcion puede ser de 4 tipos 

#1.-Funcion que no recibe parametros y no regresa valor 
#2.-Funcion que no recibe parametros y regresa valor 
#3.-Funcion que recibe parametros y no regresa valor 
#4.-Funcion que recibe parametros y regresa valor


#Ejercicio 1: Crear un funcion para imprimir nombres de personas 
#1.-Funcion que no recibe parametros y no regresa valor
def solicitarNombre():
    nombre=input("Ingresa el nombre completo: ")

solicitarNombre()
#Ejemplo 2 suma dos numeros 

def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()

#Ejepmos 3 sumar dos numeros 
#2.-Funcion que no recibe parametros y regresa valor 
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma 

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejepmos 4 sumar dos numeros 
#3.-Funcion que recibe parametros y no regresa valor 
def suma(n1,n2):
    suma=n1+n2
    print(f"La suma es: {suma}")