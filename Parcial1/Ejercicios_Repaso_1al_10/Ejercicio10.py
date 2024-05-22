#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
# Inicializar contadores para los alumnos que aprobaron y los que no
aprobados = 0
no_aprobados = 0

# Solicitar la calificación de 15 alumnos
for i in range(1, 16):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    if calificacion >= 6.0:
        aprobados += 1
    else:
        no_aprobados += 1

# Imprimir el resultado
print(f"Alumnos que aprobaron: {aprobados}")
print(f"Alumnos que no aprobaron: {no_aprobados}")