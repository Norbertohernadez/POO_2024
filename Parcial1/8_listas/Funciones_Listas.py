# list(Array)
# son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

# nota: sus valores si son modificables

# La lista es una coleccion ordenada y modificable
# Permite miembros duplicados

#Ejemplo 1 crear una lista de numeros e imprimir el contenido

numeros=[23,34]
print(numeros)

#Recorrer la lista con ciclo for
for i  in numeros:
    print(i)

#Recorrer la lista con cicloo while
i=0
while i<=len(numeros)-1:
    print(numeros[i])
    i+=1

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 

palabras=["naranja","utd","saludos","america","azul"]

palabra_buscar=input("ingresa la palabra a buscar: ")

for i in palabras:
    if i==palabra_buscar:
        print(f"Se encontra la palabra a buscar en la posicion {palabras.index}")

#Ejemplo con un while 

palabras = ["naranja", "utd", "saludos", "america", "azul"]
palabra_buscar = input("Ingresa la palabra a buscar: ")

encontro = False
i = 0

while i < len(palabras):
    if palabras[i] == palabra_buscar:
        print(f"Se encontró la palabra '{palabra_buscar}' en la posición {i}")
        encontro = True 
    i += 1

if not encontro:
    print("No se encontró la palabra a buscar")


#Ejemplo 3 Agregar y Eliminar elementos de una lista os system("clear")

numeros=[23,34,23]
print(numeros)

#agregar un elemento
numeros.append(100)
print(numeros)
numeros.insert(3200)
print(numeros)

#eliminar un elemento
numeros.remove(100) #indicaar el elemento a borrar
print(numeros)
numeros.pop(2)#indicar la posicion del elemento a borrar
print(numeros)

#Ejemplo 4 







#Ejemplo 5 crear un programa que permita gestionar peliculas colocar un menu de opciones para agregar remover,consultar,peliculas 
#coloca un menu de opciones para agregar ,remover,consultar peliculas 
#notas 
#1-utilizar funciones y mandar llamar desde otro archivo
#2-utilizar listas para almacenar los nombres de peliculas 

