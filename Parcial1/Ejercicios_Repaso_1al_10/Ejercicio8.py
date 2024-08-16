<<<<<<< HEAD
# Función para calcular el X por ciento de un número
def calcular_porcentaje(numero, porcentaje):
    resultado = (porcentaje / 100) * numero
    return resultado

# Solicitar al usuario que ingrese el número y el porcentaje
numero = float(input("Ingrese el número: "))
porcentaje = float(input("Ingrese el porcentaje (%): "))

# Calcular el resultado del porcentaje
resultado = calcular_porcentaje(numero, porcentaje)

# Mostrar el resultado
=======
# Función para calcular el X por ciento de un número
def calcular_porcentaje(numero, porcentaje):
    resultado = (porcentaje / 100) * numero
    return resultado

# Solicitar al usuario que ingrese el número y el porcentaje
numero = float(input("Ingrese el número: "))
porcentaje = float(input("Ingrese el porcentaje (%): "))

# Calcular el resultado del porcentaje
resultado = calcular_porcentaje(numero, porcentaje)

# Mostrar el resultado
>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
print(f"{porcentaje}% de {numero} es {resultado}")