<<<<<<< HEAD
#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#el contenido de la lista en mayusculas
#caso que la lista este vacia

try:
  lista = []
  if len(lista) <= 0:
     listo = True
     print("lista vacia")
     while listo == True:
        valor = input("añadir un valor a la lista: ")
        lista.append(valor)
        eleccion = input("desea añadir otro valor? S/N").upper()
        if eleccion == "N" or eleccion == "NO":
            listo = False
            print("ejecucion finalizada")

  lista_mayus = [lista.upper() for lista in lista]
  for lista in lista_mayus:
    print(lista)

except:
    print("lista ya cuenta con valores")
=======
#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#el contenido de la lista en mayusculas
#caso que la lista este vacia

try:
  lista = []
  if len(lista) <= 0:
     listo = True
     print("lista vacia")
     while listo == True:
        valor = input("añadir un valor a la lista: ")
        lista.append(valor)
        eleccion = input("desea añadir otro valor? S/N").upper()
        if eleccion == "N" or eleccion == "NO":
            listo = False
            print("ejecucion finalizada")

  lista_mayus = [lista.upper() for lista in lista]
  for lista in lista_mayus:
    print(lista)

except:
    print("lista ya cuenta con valores")
>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
