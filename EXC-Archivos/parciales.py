import os,csv
from  colorama import init,Back,Fore

init(True)

ruta = os.path.join(os.path.dirname(__file__),"calificaciones.csv")
papelFinal = os.path.join(os.path.dirname(__file__),'finales.txt')

def abrir():
    rawCalificaciones = []
    try:
        with open(ruta,'r',encoding='utf8') as file:
            # Aqui me habia ocurrido un error que era el delimitador
            next(file)
            reader = csv.reader(file, delimiter=";") # el replace es (old,new,que tantas lineas cambiar )
            for fila in reader:
                if len(fila) > 1:# obtenemos las filas
                    # no es necesario iterar aqui, ya cada elemento es una fila por separado dentro de esa columna
                    rawCalificaciones.append(
                    {'Nombre':fila[0] ,
                    'Apellido':fila[1],
                    'Asistencia': fila[2],
                    'Parcial-1':fila[3],
                    'Parcial-2': fila[4],
                    'Ordinario-P1':fila[5],
                    'Ordinario-P2':fila[6],
                    'ExaPractico':fila[7]})
    except FileNotFoundError:
        print("El archivo no existe.")
        # criterio del sorted sorted(iterable,key="criterio")
        # criterio del sorted sorted(iterable,key=lambda p: p['clave de diccionario por el cual se ordenara'])
    return sorted(rawCalificaciones,key=lambda ap: ap['Apellido'])

def paso1():
    ListaOrdenada = abrir()
    for elemento in ListaOrdenada:
        try:    
            valor1 = float(elemento['Parcial-1'].replace(",","."))
        except ValueError:
            valor1 = 0.0
        try:
            valor2 = float(elemento['Parcial-2'].replace(",","."))
        except ValueError:
            valor2 = 0.0
        try:
            valor3 = float(elemento['ExaPractico'].replace(",", "."))
        except ValueError:
            valor3 = 0.0
        # criterios de evaluacion para la nota final
        cal1 = (valor1 / 10) * 30
        cal2 = (valor2 / 10) * 30
        practico = (valor3/ 10) * 40
        final = (cal1+cal2+practico)/10
        elemento['Nota_final'] = final
    return ListaOrdenada

def paso2():
    ListaDeNombres = paso1()
    reprobados = []
    aprobados = []
    for alumno in ListaDeNombres:
        try:    
            parcial1 = float(alumno['Parcial-1'].replace(",","."))
        except ValueError:
            parcial1 = 0.0
        try:
            parcial2 = float(alumno['Parcial-2'].replace(",","."))
        except ValueError:
            parcial2 = 0.0
        try:
            ExamPractico = float(alumno['ExaPractico'].replace(",", "."))
        except ValueError:
            ExamPractico = 0.0  # o None, o lo que quieras
        try:
            asistencias = float(alumno['Asistencia'].replace(",",".").rstrip("%"))
        except ValueError:
            asistencias = 0
        # no conocia esta sintaxis del if para condiciones largas
        try:
            
            with open(papelFinal,'a') as file:
                if (
                asistencias >= 75 and
                parcial1  >= 4 and
                parcial2 >= 4 and
                alumno['Nota_final'] >= 5
                ):
                    aprobados.append({alumno['Nombre'],alumno['Apellido']})
                    file.writelines(f"Aprobado -> {alumno['Nombre']} {alumno['Apellido']}" + "\n")
                else:
                    reprobados.append({alumno['Nombre'],alumno['Apellido']})
                    file.writelines(f"Reprobado -> {alumno['Nombre']} {alumno['Apellido']}" + "\n")
        except FileNotFoundError:
            print("error en el documento")
    print("se registraron los datos.")

paso2()


