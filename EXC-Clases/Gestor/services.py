from main import Estudiante,Curso,Maestro
import db
from colorama import Fore, Style, Back
from time import sleep
from Utilities import clear
import re
import sqlite3

"""
    Autor:
    Luis Alejandro Aguilar Soberanes
    
    Modulo de Funciones Principales


    Los datos viven donde se ejecuta la query
    si otra función los necesita,
    se los pasas, no los “re-preguntas” -
    no podemos asumir que los conocen.

    Rowcount -> filas afectadas (0 = ninguna, != 0 hubo cambios)
    fetchone -> resultado del query (solicitud traida)
"""

# Separar responsabilidades
"""Estudiantes"""


def nuevo_alumno()-> Estudiante:
    modelo = r'\w+@\w+\.(com|mx|edu|com.br)$'
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    print(f"{Back.BLACK} {Fore.GREEN}--= Nuevo estudiante =--{Style.RESET_ALL}")
    if input("presiona -1 para salir: ") == '-1':
        return None
    else:
        pass
    nombre = input("Nombre(s) del estudiante: ").capitalize().strip()
    apellido = input("Apellido(s) del estudiante: ").capitalize().strip()
    while True:
        noCuenta = input("Numero de cuenta: ")
        try:
            noCuenta = int(noCuenta)
            break
        except TypeError:
            print("El numero del estudiante debe de ser un numero.")
    correo = input("Ingresa el correo: ").strip()
    if re.search(modelo,correo):
        if Estudiante(nombre, apellido, noCuenta,correo):
            # insertar estudiante
            try:
                cur.execute("""INSERT INTO Estudiantes VALUES (?, ?, ?,?)""", (noCuenta, nombre, apellido,correo))
            # verificar que si se creo, no lleva parentesis, porque no es una funcion o metodo.
                if cur.rowcount > 0:
                    print("Estudiante creado correctamente")
                    input("presione para salir ")
            except sqlite3.IntegrityError as e:
                print("El numero de cuenta ya se encuentra registrado")
            finally:
                con.commit()
                con.close()
    return Estudiante(nombre, apellido, noCuenta,correo)

def eliminar_alumno()-> None:
    clear()
    print(f"{Back.BLACK} {Fore.GREEN}--= Dar de baja estudiante =--{Style.RESET_ALL}")
    noCuenta = input("Escribe el numero de cuenta del alumno.")
    con = db.databaseManage()
    cur = con.cursor()
    # eliminar al estudiante
    cur.execute("""DELETE FROM Estudiantes WHERE id_estudiante = ?""", (noCuenta,))
    # verificar si hubo cambios en alguna fila (registro) de ser asi, entonces se imprime.
    if cur.rowcount > 0:
        print("El estudiante ha sido eliminado de los registros.")
    else:
        print(f"Sin coincidencias para: {noCuenta}")
    con.commit()
    con.close()

def modificar_alumno()-> None:
    COLUMNAS_VALIDAS = {"id_estudiante","nombre", "apellido", "correo"}
    modelo = r'\w+@\w+\.(com|mx|edu|com.br)$'
    clear()
    noCuenta = input("ingresa el numero de cuenta del estudiante que deseas modificar: ")
    con = db.databaseManage()
    cur = con.cursor()
    cur.execute("""SELECT nombre FROM Estudiantes WHERE id_estudiante = ? """,(noCuenta,))
    existe = cur.fetchone()
    if existe:
        print(f"Estudiante: {existe[0]}")
        cambio = input("Que deseas modificar\n1) Nombre\n2) Apellido\n3) No. Cuenta\n4) Correo\n")
        match cambio:
            case '1':
                atributo = "nombre"
                columna = input("Nuevo nombre: ")
            case '2':
                atributo = "apellido"
                columna = input("Nuevo apellido: ")
            case '3':
                atributo = "id_estudiante"
                columna = input("Nuevo numero de cuenta: ")
            case '4':
                atributo = "correo"
                while True:
                    columna = input("correo nuevo: ")
                    if re.search(modelo,columna):
                        break
                    print("ingresa el formato de correo correcto.")
            case _:
                print("ingresa una opcion del menu")

        # utilizando una lista blanca de columnas validas para preevenir interpolacion e inyeccion sql
        if atributo not in COLUMNAS_VALIDAS:
            raise ValueError("Columna no permitida")
        cur.execute(f"UPDATE Estudiantes SET {atributo} = ? WHERE id_estudiante = ?",(columna,noCuenta))
        con.commit()
        if cur.rowcount > 0:
            print("estudiante actualizado con exito")
        else:
            print("Los cambios no surgieron efecto.")
    else:
        print("El estudiante no se encontro")
    input("presiona enter para continuar...")
    con.close()

def mostrar_estudiantes()-> None:
    clear()
    print("Mostrando Estudiantes")
    con = db.databaseManage()
    cur = con.cursor()
    cur.execute("SELECT * FROM Estudiantes")
    salio2 = cur.fetchall()
    if salio2 is None:
        print("No hay ningun estudiante registrado")
    else:        
        print("==============================")
        print(f"{Back.BLACK}{Fore.GREEN }Nombre | Apellido |  Correo  | NO.cuenta{Style.RESET_ALL}\n")
        for id_estudiante, nombre, apellido,correo in salio2:
            print(f"| {nombre} {apellido} {correo} {Fore.GREEN}[{str(id_estudiante)}]{Style.RESET_ALL}")
        print("==============================")
    input("presiona enter para continuar...")
    con.close()

def buscar_estudiante(courseRol=None)-> None:
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    print(f"{Back.BLACK}{Fore.GREEN }Selecciona el tipo de busqueda{Style.RESET_ALL}\n1) Numero de cuenta\n2) Nombre\n3) Correo")
    searchStudent = input(">> ")    
    try:
        match searchStudent:
            case '1':
                clear()
                print("Escribe el numero de cuenta")
                searchStudentID = input(">> ")
                cur.execute("SELECT * FROM Estudiantes WHERE id_estudiante = ?", (searchStudentID,))
                userget = cur.fetchone()
                if userget is None:
                    print(f"No se encontro un estudiante con el id: {searchStudentID}")
                else:
                    print(f"{Back.BLACK}{Fore.GREEN }-- Estudiante encontrado --{Style.RESET_ALL}")
                    print("Mostrando informacion del estudiante...")
                    (Studentid, name, Apellido) = userget
                    print(f"Estudiante: [{name}] [{Apellido}] con NO.Cuenta: {Studentid}.")
                    print("inscrito en:\n")
                    cur.execute("""
                    SELECT
                        Estudiantes.nombre as 'StudentName',
                        cursos.topico_del_curso as Course,
                        maestros.Name as Teacher
                    FROM Estudiantes
                    JOIN Enrollments
                        ON Estudiantes.id_estudiante = Enrollments.Stuid
                    JOIN cursos
                        ON cursos.id_curso = Enrollments.Coursid
                    JOIN maestros
                        ON maestros.Numero_de_registro =  cursos.Numero_de_registro
                    WHERE id_estudiante = ?""",(searchStudentID,))
                    cursosRol = cur.fetchall()
                    for StudentName, courseName, TeacherName in cursosRol:
                        print(StudentName, courseName, TeacherName)
            case '2':
                clear()
                print("escribe los nombres(s)")
                searchStudentName = input(">> ").strip()
                print("escribe los apellido(s)")
                searchStudentApellido = input(">> ").strip()
                cur.execute("""SELECT * FROM Estudiantes WHERE nombre = ? AND apellido = ? """, (searchStudentName, searchStudentApellido))
                userget = cur.fetchone()
                if userget is None:
                    print(f"No se encontro un estudiante con {Fore.RED} {searchStudentName} {Style.RESET_ALL} y de apellido {Fore.RED} {searchStudentApellido} {Style.RESET_ALL}\n")
                else:
                    print(f"{Back.BLACK}{Fore.GREEN }-- Estudiante encontrado  --{Style.RESET_ALL}")
                    (Studentid, name, Apellido) = userget
                    print(f"Estudiante {name} {Apellido} con NO.Cuenta:  {Studentid}")
                    print("inscrito en:\n")
                    cur.execute("""
                        SELECT
                            T.name as 'Teacher Name',
                            topico_del_curso as 'Course Name'
                        FROM
                            Enrollments
                        JOIN Estudiantes S on Enrollments.Stuid = S.id_estudiante
                        JOIN cursos C on Enrollments.Coursid = C.id_curso
                        JOIN maestros T on C.Numero_de_registro = Enrollments.Numero_de_registro
                        WHERE S.nombre = ?""",(name,))
                    courseRol = cur.fetchall()
                    for teacher_name,course_name in courseRol:
                        print(f"{teacher_name} {course_name}")
            case '3':
                print("Escribe el correo del estudiante")
                searchStudentEmail = input(">> ")
                cur.execute("SELECT * FROM Estudiantes WHERE correo = ?", (searchStudentEmail,))
                userget = cur.fetchone()
                if userget is None:
                    print(f"No se encontro un estudiante con el correo: {searchStudentEmail}")
                else:
                    print(f"se encontro 1 coincidencia con el correo: {searchStudentEmail}")
                    print("-"*10)
                    for i in userget:
                        print(i)
                    print("-"*10)
    except sqlite3.Error as e:
        print(f"Ha ocurrido un error {e}")
    finally:
        con.close()
    input("presiona enter para continuar...")

"""cursos"""
def nuevo_curso()-> Curso:
    VALIDAS = {""}
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    clear()
    while True:
        print(f"{Back.BLACK} {Fore.GREEN}--= Nuevo Curso =--{Style.RESET_ALL}\n")
        CTopic = input("Tema del curso: ")
        CDuration = input("Duracion (en minutos): ")
        CRating = input("Rating (0/5): ")
        print("Como deseas buscar al profesor\n1) Nombre\n2) ID")
        op = input(">> ").strip()
        match op:
            case '1':
                CTeacher = input("Nombre del maestro: ").strip()
                CTeacherApellido = input("Apellido del maestro: ").strip()
                cur.execute("""SELECT Numero_de_registro FROM maestros WHERE nombre = ? and apellido = ?""", (CTeacher, CTeacherApellido))
            case '2':
                cid = input("Ingresa el id del maestro: ")
                cur.execute("""SELECT nombre FROM maestros WHERE Numero_de_registro = ?""", (cid,))
            case _:
                print("elige una opcion valida")
        # Buscar el id de profesor mediante su nombre mas sencillo para la busqueda
        getID = cur.fetchone() 
    # Ahora si buscamos por su id
        if getID is None:
            print(f"No hay coincidencias para el profesor: {CTeacher}")
        else:
            print(f"Maestro  debug {getID[0]}")
            try:
                cur.execute("""INSERT INTO cursos VALUES (?,?,?,?)""", (CTopic, CDuration, CRating, getID[0]))
                con.commit()
                print("Curso creado correctamente")
            except sqlite3.Error as e:
                print(f"Error {e}")
            finally:
                con.close()
    input("presiona enter para continuar...")
    return Curso(CTopic, float(CDuration), CRating, getID[0])

def mostrar_curso()-> None:
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    cur.execute("SELECT * FROM cursos")
    todos_los_cursos= cur.fetchall()
    clear()
    print("Cursos Disponibles:")
    print("=================================================")
    print(f"|   Curso  |  Duracion  |  Rating  |  Maestro   |")
    for _,name,duration,rating,teacher in todos_los_cursos:
        # Sacar el nombre del profesor
        cur.execute("""SELECT Name, Apellido FROM maestros where Numero_de_registro = ?""",(teacher,))
        allteacher = cur.fetchall()
        for tanme,lasname in allteacher:
            # al momento de usar colorama, despues de usar un color debemos de limparlo con style.reset_all
            print(f"[{Fore.GREEN}{name}{Style.RESET_ALL}]:\n\t    {round(float(duration/60))}hrs - {rating}/5 - {tanme} {lasname}")
    print("=================================================\n")
    input("presiona enter para continuar...")
    con.close()

def buscar_curso(a)-> None:
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    if a =='1':
        # todos los resultados coincidentes
        print("Filtrar curso por:\nMaestro\nDuracion\nTopic\nRating")
        filter_type = input()
        print("ingresa el campo solicitado")
        course_search = input()
        cur.execute("""
        SELECT * FROM cursos
        where ? = ?
        """,(filter_type,course_search))
    elif a =='2':
        # resultado (s) unicos 
        print("----------------------------")
        print("Buscar por:\nMaestro\nDuracion\nTopic\nRating")
        print("----------------------------")
    input("presiona enter para continuar...")
    con.close()

"""maestros"""
def nuevo_maestro()-> Maestro:
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    clear()
    print(f"{Back.BLACK} {Fore.GREEN}--= Nuevo Maestro =--{Style.RESET_ALL}")
    tname = input("Nombre(s) del maestro: ")
    tlname = input("Apellido(s) del maestro: ")
    while True:
        tregis = input("Numero de cedula del maestro: ")
        try:
            tregis = int(tregis)
            break
        except:
            print("La cedula debe ser numerica")
    cur.execute("""INSERT INTO maestros VALUES (?,?,?)""",(tname,tlname,tregis))
    if cur.rowcount > 0:
        print("profesor ingresado correctamente")
    con.commit()
    con.close()
    input("presiona enter para continuar...")
    return Maestro(tlname,tlname,tregis)

def mostrar_maestros()-> None:
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    clear()
    print("------------- Profesores -----------")
    print("|  Nombre  |  Apellido  |  Cedula  |")
    print("-----------------------------------")
    cur.execute("""SELECT nombre,apellido,Numero_de_registro FROM maestros""")
    teachgerQueryresponse = cur.fetchall()
    if teachgerQueryresponse is None:
        print("No hay maestros registrados?")
    else:
        for Tname, TApellido, Registration in teachgerQueryresponse:
            print(f"{Tname} {TApellido}: {Fore.GREEN }{str(Registration)}{Style.RESET_ALL}")
    input("presiona enter para continuar...")
    con.close()

"""Enrollement"""
def inscribir()-> None:
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    print(f"{Back.BLACK} {Fore.GREEN}--= menu de inscripcion de estudiantes =--{Style.RESET_ALL}")
    print("Ingresa el numero de cuenta del alumno")
    studi = input(">> ")
    cur.execute("SELECT * FROM cursos")
    impresionconsos = cur.fetchall()
    print("Cursos disponibles")
    for _, name, duration, rating, teacher in impresionconsos:
        print(f"curso: {name} | duracion: {round(float(duration/60))} horas | Rating: {rating}/5 | Maestro: {teacher}")
    print("ingresa el curso donde quieres inscribir al estudiante")
    ces = input(">> ")
    cur.execute("SELECT id_curso FROM cursos WHERE topico_del_curso = ?", (ces,))
    resid = cur.fetchone()
    if resid:
        cur.execute("""INSERT INTO Inscripciones  VALUES (?,?,?)""", (default, resid[0], studi))
        sleep(2)
        print("inscripcion exitosa")
    input("presiona enter para continuar...")
    con.close()

# Pendiente
def dar_de_baja()-> None:
    clear()
    con = db.databaseManage()
    cur = con.cursor()
    print(f"{Back.BLACK} {Fore.GREEN}--= Dar de baja estudiante  =--{Style.RESET_ALL}")
    # Obtener el id del usuario
    print("Ingresa el numero de cuenta del estudiante")
    dropsid = input(">> ")
    cur.execute("""SELECT nombre from Estudiantes where id_estudiante = ?""", (dropsid,))
    dropname = cur.fetchone()
    if dropname is None:
        print(f"No se encontro un nombre asociado con el numero de cuenta: {dropsid}")
    else:
        return dropsid, dropname[0]
    input("presiona enter para continuar...")

def drop_student_show_enrolled()-> None:
    clear()
    dropsid, name = drop_student_data()
    con = db.databaseManage()
    cur = con.cursor()
    cursos = []
    cur.execute("""
        SELECT cursos.topico_del_curso FROM Estudiantes
        JOIN Enrollments
            ON Estudiantes.id_estudiante = Inscripciones.id_estudiante
        JOIN cursos
            ON Inscripciones.id_curso = cursos.id_curso
        WHERE id_estudiante = ?""", (dropsid,))
    rows = cur.fetchall()
    # fetch all devuelve una lista vacia en caso de no tener coincidencia, no devuelve none como fetchone, y las quieries se gastan
    if not rows:
        print(f"No hay coincidencias para {drop_student_data()}")
    else:
        print(f"Cursos donde {drop_student_data()} esta inscrito")
        for courserolled in rows:
            cursos.append(courserolled[0])
    return cursos, name

def drop_student()-> None:
    clear()
    cursos, name = drop_student_show_enrolled()
    con = db.databaseManage()
    cur = con.cursor()
    for course in cursos:
        print("- ", course)
    coursedropselec = input("De cual curso deseas eliminarlo? (presiona enter para cancelar): ")
    if coursedropselec not in cursos:
        print("El usuario debe estar en el curso en cuestion para ser eliminado")
    else:
        # sacar el id del curso
        cur.execute("SELECT id_curso FROM cursos WHERE topico_del_curso LIKE ?", (f"%{coursedropselec}%",))
        curso_id = cur.fetchone()
        cur.execute("SELECT id_estudiante FROM Estudiantes WHERE nombre LIKE ?", (f"%{name}%",))
        estudiante_id = cur.fetchone()
        if curso_id is None and estudiante_id is None:
            print(f"No se encontraron coincidencias con numero de cuenta {curso_id}")
        else:
            # eliminar ya al usuario
            cur.execute("""DELETE FROM Inscripciones WHERE id_estudiante = ? AND id_curso = ?""", (estudiante_id[0], curso_id[0]))
            if cur.rowcount() == 1:
                print(f"El estudiante ha sido eliminado del curso: {coursedropselec}.")
                print("regresando al menu...")
                sleep(1)
            else:
                print("Ha ocurrido un error al intentar borrar al estudiante")
    con.close()

# Podemos convertir los datos del query con row_factory

