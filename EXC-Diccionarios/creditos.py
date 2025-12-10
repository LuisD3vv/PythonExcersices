
asiganturas = {
    
}

#delattr() borra el atributo pasado

print("Cuantas asignaturas son?: ")
nasi = int(input(">> "))

for i in range(nasi):
    print("Ingresa la asignatura")
    asignatura = input(">> ")
    print("Ingresa la calificacion de la asignatura")
    while True:
        try:
            calificacion = float(input(">> "))
            asiganturas[asignatura.capitalize()] = calificacion
            break
        except ValueError:
            print("La calificacion no debe ser un string")

print("===============================")
total = 0
for materia,calificacion in asiganturas.items():
    total += calificacion
    print(f"{materia} tiene {calificacion} creditos")
print(f"El total de creditos del curso es: {total}")
try:
    division = total/len(asiganturas)
except ZeroDivisionError:
    print("No hay los suficientes elementos para realizar el promedio")
else:
    print(f"Con un promedio de: {division}")
