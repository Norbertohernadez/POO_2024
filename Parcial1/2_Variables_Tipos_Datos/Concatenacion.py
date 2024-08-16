#Formas de concatenar en python

nombre="name"
especialidad="Area de sofware multiplataforma"
carrera="Ingenieria en gestion de desarrollo de software"

#Primer forma 
print("Mi nombre es "+nombre+"estoy en la especialidad"+especialidad+" y estudio la carrera de"+carrera)

print("\n")

#Segunda forma
print("Mi nombre es",nombre,"estoy en la especialidad",especialidad," y estudio la carrera de",carrera,)

print("\n")

#Tercera forma mas comunes en python
print(f"Mi nombre es,{nombre},estoy en la especialidad,{especialidad}, y estuudio la carrera de, {carrera}")

print("\n")

#Cuarta forma
print("Mi nombre es,{}, estoy en la eapecialidad,{}, y estudio la carrera de,{}". format(nombre,especialidad,carrera))

print("\n")

#Quinta forma
print('Mi nombre es'+nombre+'estoy en la especialidad'+especialidad+' y estudio la carrera'+carrera)

print("\n")