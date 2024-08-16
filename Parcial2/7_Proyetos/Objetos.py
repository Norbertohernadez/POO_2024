<<<<<<< HEAD
# objetos.py

from figuras import area_rectangulo, area_circulo, mostrar_resultado, ocultar_resultado, mover_objeto

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = 0
    
    def calcular_area(self):
        """
        Calcula el área del rectángulo utilizando la función del módulo figuras.
        """
        self.area = area_rectangulo(self.base, self.altura)
        return self.area
    
    def mostrar(self):
        """
        Muestra el área del rectángulo.
        """
        mostrar_resultado(f"Área del rectángulo: {self.area}")
    
    def ocultar(self):
        """
        Oculta el área del rectángulo.
        """
        ocultar_resultado()
    
    def mover(self, x, y):
        """
        Mueve el rectángulo a las coordenadas (x, y).
        """
        mover_objeto(x, y)

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
    
    def calcular_area(self):
        """
        Calcula el área del círculo utilizando la función del módulo figuras.
        """
        self.area = area_circulo(self.radio)
        return self.area
    
    def mostrar(self):
        """
        Muestra el área del círculo.
        """
        mostrar_resultado(f"Área del círculo: {self.area}")
    
    def ocultar(self):
        """
        Oculta el área del círculo.
        """
        ocultar_resultado()
    
    def mover(self, x, y):
        """
        Mueve el círculo a las coordenadas (x, y).
        """
        mover_objeto(x, y)







=======
# objetos.py

from figuras import area_rectangulo, area_circulo, mostrar_resultado, ocultar_resultado, mover_objeto

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = 0
    
    def calcular_area(self):
        """
        Calcula el área del rectángulo utilizando la función del módulo figuras.
        """
        self.area = area_rectangulo(self.base, self.altura)
        return self.area
    
    def mostrar(self):
        """
        Muestra el área del rectángulo.
        """
        mostrar_resultado(f"Área del rectángulo: {self.area}")
    
    def ocultar(self):
        """
        Oculta el área del rectángulo.
        """
        ocultar_resultado()
    
    def mover(self, x, y):
        """
        Mueve el rectángulo a las coordenadas (x, y).
        """
        mover_objeto(x, y)

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
    
    def calcular_area(self):
        """
        Calcula el área del círculo utilizando la función del módulo figuras.
        """
        self.area = area_circulo(self.radio)
        return self.area
    
    def mostrar(self):
        """
        Muestra el área del círculo.
        """
        mostrar_resultado(f"Área del círculo: {self.area}")
    
    def ocultar(self):
        """
        Oculta el área del círculo.
        """
        ocultar_resultado()
    
    def mover(self, x, y):
        """
        Mueve el círculo a las coordenadas (x, y).
        """
        mover_objeto(x, y)







>>>>>>> 9438c29a50360c7fce3d03b942d3b257211e0861
