# Función para imprimir una tabla de multiplicar
def imprimir_tabla(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ciclo para imprimir las tablas del 1 al 10
for numero in range(1, 11):
    imprimir_tabla(numero)

