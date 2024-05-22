#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
# Solicitar al usuario que ingrese los dos números
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

# Asegurarse de que el primer número sea menor que el segundo número
if inicio > fin:
    inicio, fin = fin, inicio

print(f"Números impares entre {inicio} y {fin}:")

# Iterar a través de los números entre los dos números ingresados
for numero in range(inicio, fin + 1):
    if numero % 2 != 0:  # Verificar si el número es impar
        print(numero)
