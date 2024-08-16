# main.py

from objetos import Rectangulo, Circulo

# Ejemplo de uso
rectangulo1 = Rectangulo(5, 10)
area_rectangulo = rectangulo1.calcular_area()
rectangulo1.mostrar()

circulo1 = Circulo(7)
area_circulo = circulo1.calcular_area()
circulo1.mostrar()

# Mover un objeto (ejemplo)
rectangulo1.mover(2, 3)
