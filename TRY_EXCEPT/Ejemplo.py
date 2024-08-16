#Ejemplo de como funciona el Try Except
#Ahora vamos a mostrar el ejemplo del error (valueError)
#Agregaremos un ejemplo mas de TypeError
#Por ultimo agregaremos un modulo import si ya tienes experiencia en progracion sabes como funciona si no aqui aprenderas 

import sys
try:
  num=int(input("Introduce un numero: "))
  print("El resultado es: ", 1/num)
except TypeError:
  print("Se agrego un valor no numerico")
print("El error fue ", sys.exc_info()[0])
