#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

# Inicializar una variable para almacenar el número ingresado por el usuario
numero = 0

# Solicitar números al usuario indefinidamente
while numero != 111:
    numero = int(input("Ingrese un número (o ingrese 111 para salir): "))
    if numero == 111:
        print("Saliendo del programa...")
    else:
        print(f"El número ingresado es: {numero}")
