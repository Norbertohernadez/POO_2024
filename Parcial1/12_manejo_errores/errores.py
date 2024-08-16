#los errores de ejecucuion en un lenguaje de programacion se presentan cuando existe una anomalis dentro de la ejecucion del codigo lo cual provoca que se detenga la ejecucion del SW. Con el control y manejo de excepciones será posible minimizar o evitar la interrupcion del programa debido a una excepción.

#EJEMPLO 1: CUANDO UNA VARIABLE NO SE GENERA 

# try:
#     nombre=input("Introduce el nombre completo de una persona: ")

#     if len(nombre)>0:
#        nombre_usuario="El nombre completo del usuario es: "+nombre

#     print(nombre_usuario)

# except:
#     print("Es necesario introducir un nombre de usuario......verifica por favor")

#....................................................................................
#EJEMPLO 2: CUANDO SE SOLICITA UN NUMERO Y SE INGRESA OTRA COSA

# try:
#     numero=int(input("Ingrese un numero entero: "))

#     if numero>0: 
#        print("Soy un numero positivo")

#     elif numero==0:
#        print("Soy un numero entero neustro")

#     else: 
#        print("Soy un numero entero negativo")

# except ValueError:
#     print("Introduce un valor numerico enteroooo")

#.................................................................................
#EJEMPLO 3: Generan multiples escepciones

try:
    numero=int(input("Introduce un numero: "))

    print(f"El cuadrado del numero es: {numero*numero}")

except TypeError:
    print("Introduce un valor numerico entero")
    
except TypeError:
    print("Se debe convertir el numero a entero")

else: 
    print("No se presentaron errores de ejecución")
finally: #pero tambien se ejecuta esta haya errores o no
    print("Termine la ejecución")