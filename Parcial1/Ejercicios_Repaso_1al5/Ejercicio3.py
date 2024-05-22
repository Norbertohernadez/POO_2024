#Escribir  un programa que muestre los cuadrados
#Un numero multiplicado por si mismo, de los 60 primeros
#numero naturales resolver con while y for 

contador = 1
numero = 1

# Mientras el contador sea menor o igual a 60
while contador <= 60:
    # Calculamos el cuadrado del número y lo mostramos
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es: {cuadrado}")
    
    # Incrementamos el contador y el número
    contador += 1
    numero += 1