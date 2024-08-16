 #Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado


# Solicitar dos números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Verificar si el segundo número es distinto de cero antes de realizar la división
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre cero"

# Mostrar los resultados por pantalla
print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division}")