#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
# Solicitar dos números al usuario
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

# Verificar el orden de los números ingresados
if inicio <= fin:
    # Mostrar todos los números entre el inicio y el fin (inclusive)
    print("Los números entre", inicio, "y", fin, "son:")
    for numero in range(inicio, fin + 1):
        print(numero, end=" ")
else:
    # Mostrar un mensaje de error si los números están en orden incorrecto
    print("Error: El primer número debe ser menor o igual que el segundo número.")