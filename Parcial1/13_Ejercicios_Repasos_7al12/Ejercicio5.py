# Crear una lista y un diccionario con el contenido de esta tabla: 
#   ACCION  TERROR  DEPORTES
#   MAXIMA VELOCIDAD  LA MONJA  ESPN
#   ARMA MORTAL 4 EL CONJURO MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#imprimir la información
import msvcrt

peliculas = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

dic_pelis = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

#Imprime el contenido de la lista
print("\t CONTENIDO DE LA LISTA")
for fila in peliculas:
    print(fila)
print("Presione una tecla para continuar....")
msvcrt.getch()

#Imprimi el contenido del diccionario
print("\t CONTENIDO DEL DICCINARIO:")
for categoria, pelicula in dic_pelis.items():
    print(f"Categoría: {categoria}")
    print("Peliculas:", pelicula)