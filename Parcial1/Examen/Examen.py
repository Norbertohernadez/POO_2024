#Ingrese el nombre del trabajador 
Nombre_Del_trabajador=input("Introduce el nombre del trabajador:")

#Ingrese las horas trabajadas al dia del trabajador
horas_trabajadas=float(input("Introduce las horas trabajadas al dia:"))

#Ingresa el numero de dias trabajdos
dias_trabajados = int (input ("Introduce los dias trabajados:"))

#Solicitar sueldo por hora 
sueldo_por_hora=float(input("Introduce el sueldo por hora:"))

#Calcular sueldo semanal
sueldo_semanal=horas_trabajadas*dias_trabajados*sueldo_por_hora

#calcular sueldo mensual(asumiendo 4 semanas por mes)
sueldo_mensual=sueldo_semanal*4

#Categorias de los trabajadores 

Categoria=("Obrero tipo A" if sueldo_mensual <=10000 else
           "Otro tipo B" if sueldo_mensual  <15000 else
           "sin categoria")

#Mostrar los datos de trabajador y sus pagos 
print("\nDatos del trabajador:")




