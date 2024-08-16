<<<<<<< HEAD
resultado_global = 0

def suma(a, b):
    global resultado_global
    resultado_global = a + b
    print(f"Suma: {resultado_global}")

def resta(a, b):
    global resultado_global
    resultado_global = a - b
    print(f"Resta: {resultado_global}")

suma(5, 3)
resta(5, 3)

print(f"Resultado global fuera de las funciones: {resultado_global}")resultado_global= 0

def suma(a, b):
    resultado_local = a + b
    print(f"Suma (variable local): {resultado_local}")

def resta(a, b):
    resultado_local = a - b
    print(f"Resta (variable local): {resultado_local}")

suma(5, 3)
resta(5, 3)
=======
resultado_global = 0

def suma(a, b):
    global resultado_global
    resultado_global = a + b
    print(f"Suma: {resultado_global}")

def resta(a, b):
    global resultado_global
    resultado_global = a - b
    print(f"Resta: {resultado_global}")

suma(5, 3)
resta(5, 3)

print(f"Resultado global fuera de las funciones: {resultado_global}")resultado_global= 0

def suma(a, b):
    resultado_local = a + b
    print(f"Suma (variable local): {resultado_local}")

def resta(a, b):
    resultado_local = a - b
    print(f"Resta (variable local): {resultado_local}")

suma(5, 3)
resta(5, 3)
>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
print(f"Resultado global fuera de las funciones: {resultado_global}")