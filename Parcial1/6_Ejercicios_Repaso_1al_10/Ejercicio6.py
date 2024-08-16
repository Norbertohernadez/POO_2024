<<<<<<< HEAD
# Función para imprimir una tabla de multiplicar
def imprimir_tabla(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ciclo para imprimir las tablas del 1 al 10
for numero in range(1, 11):
=======
# Función para imprimir una tabla de multiplicar
def imprimir_tabla(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ciclo para imprimir las tablas del 1 al 10
for numero in range(1, 11):
>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
    imprimir_tabla(numero)