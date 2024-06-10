#Los errores de ejecucion en un lenguaje de programacion se presentan cuando existe una 
# anomalia dentro de la ejecucion del codigo lo cualprovoca que se detenga la ejecucion del SW
# con el control y manejo de exepciones sera posible minimizar o evitar la interrupcion
# del programa debido a unan excepcion.

#Ejemplo 1 cuando una variable no se genera  
try:
    nombre=input("Introduce el nombre completo de una persona:")

    if len(nombre)>0:
     nombre_usuario="El nombre completo del usuario es:"+nombre 

    print(nombre_usuario)
except NameError:
   print("Ingresar un nombre de usuario verifica por favor")

#Ejemplo2 cuando se solicita un numero y se ingresa otra cosa 
try:
    numero=int(input)("ingrese un numero entero")

    if numero>0:
      print("Soy un numero entero positivo")
    else:
      print("Soy un numero entero negativo")
except ValueError:
   print("Ingresa un valor numerico entero")

#Ejemplo 3 cuando se generan multiples excepciones 
try:
    numero=int("Introduce un numero")

    print("El cuadrado del numero es:"+str(numero*numero))
except ValueError:
   print("Ingresa un valor numerico entero")
except TypeError:
    print("Se debe convertir el numero a entero")
    
else:
    print("No se presentaron errores de ejecucion")
finally:
   print("Termine la ejecucion")