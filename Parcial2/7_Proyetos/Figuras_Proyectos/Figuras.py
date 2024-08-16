
import math

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dado su base y altura.
    """
    return base * altura

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    """
    return math.pi * radio ** 2

def mostrar_resultado(mensaje):
    """
    Muestra el resultado en consola.
    """
    print(mensaje)

def ocultar_resultado():
    """
    Oculta el resultado.
    """
    print("Resultado oculto.")

def mover_objeto(x, y):
    """
    Mueve el objeto a las coordenadas (x, y).
    Esta función es solo para ilustrar el concepto de mover un objeto, 
    no se puede aplicar en un  cálculo del área en este caso
    """
    print(f"Objeto movido a la posición ({x}, {y}).")

