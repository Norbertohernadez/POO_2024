#Listas(Array)
#son coleciones o conjunto de datos/valores bajo un mismo nombre para acceder a los valores se hace con un indice numerico
#Nota:sus valores si son modificables 
#La lista es una coleccion ordenada y modificable permite miembros duplicados.

#Ejemplo uno crear una lista de numeros y imprimir el contenido

numeros= [23,34]
print(numeros)

#Recorrer la lista con un ciclo for
for i in numeros:
    print(i)


#Recorrer la lista con un ciclo while
i=0
while i<=len(numeros)-1:
       print( numeros [i])
       i+=1

#Crear una lista de palabras y posterior mente buscar la coincidencia de una palabra

palabras=["naranja,Utd,,america,azul"]
 
palabra_buscar=input("Ingresa la palabra a buscar:")

for i in palabras:
      if i ==palabra_buscar:
            print(f"se encontro la palabra a buscar en la posicion {palabra,index}")
      else: