from os import system as sys
from pathlib import Path
import sqlite3
"""
Como repaso rapido,  los getter y setter son metodos usados para controlar el acceso a los atributos de clase, asegurando la encapsulacion de la infoamcion y permitiendo una validacion.
"""

db1 = 'GestorUas.db'

class Student:
    def __init__(self,name,lastname,accountID):
        self._name = name
        self._lastname = lastname
        self._accountID =  accountID
    # decoradro que convierte un metodo en un atributo de solo lectura y nos permite usar el punto
    # instancia.objeto = tal
    @property
    def name (self):
        """getter for name"""
        return self._name
    @name.setter
    def name (self,newName):
        """setter for name validation"""
        if not isinstance(newName,str) or not newName.strip():
            raise ValueError("Name must be a non-empty string.")
        self._name = newName
    
    @property
    def lastname (self):
        """getter for lastname"""
        return self._lastname
    @lastname.setter
    def lastname (self,newlastname):
        """setter for lastname validation"""
        if not isinstance(newlastname,str) or not newlastname.strip():
            raise ValueError("Lastame must be a non-empty string.")
        self._lastname = newlastname

    @property
    def accountID (self):
        """getter for accountid"""
        return self._accountID
    @accountID.setter
    def accountID (self,newid):
        """setter for accountid validation"""
        if not isinstance(newid,int) or newid < 0:
            raise ValueError("The number must be no negative integer.")
        self._accountID = newid

class Curse():
    def __init__(self,courseName,teacher,duration,rating):
        self._curseName = courseName
        self._teacher = teacher
        self._duration = duration
        self._rating = rating
# esta es la clase de transaccion.
class CoursePlatform():
    def __init__(self,platformName):
        self._platformName = platformName

def conexion(funcion):
    try:
        with sqlite3.connect(db1) as conn:
            ...
    except sqlite3.OperationalError as e:
        print("error")

def crearAlumno():

    nombre = input("Nombre del Alumno: ")
    apellido = input("Apellido del Alumno: ")
    noCuenta = input("Numero de cuenta: ")
    todo = [nombre,apellido,noCuenta]
    if all(todo):
        nuevoAl = Student(name=nombre,lastname=apellido,accountID=noCuenta)
        if isinstance(nuevoAl,Student):
            try:
                with sqlite3.connect(db1,timeout=30,check_same_thread=True) as con:
                    cur = con.cursor()
                    cur.execute("""
                    CREATE TABLE IF NOT EXISTS Student (
                    Student_id integer,
                    nombre varchar(50),
                    apellido varchar(50)
                    )""")
                    cur.execute("""INSERT INTO Student (Student_id,nombre,apellido) values(?,?,?)""",
                    (noCuenta,nombre,apellido))
                    con.commit()
                # verificar que si se creo
                with sqlite3.connect(db1,timeout=30,check_same_thread=True) as con:
                    cur = con.cursor()
                    cur.execute("""
                    SELECT Student_id from Student
                    where Student_id = ?
                    """,(noCuenta,))
                    print("Alumno creado correctamente")
            except sqlite3.Error as e:
                print(f"Ocurrio un error -> {e}")
        else:
            print("Error al crear alumno")
    else:
        print("Please, complete all the fields.")

def leerAlumno():
    print("Listando todos los Alumnos Registrados")
    with sqlite3.connect(db1) as conn:
        cur = conn.cursor()
        cur.execute("""
        SELECT * FROM Student
        """)
        formato()
        salio2 = cur.fetchall()
        for acid,name,lastname in salio2:
            print(f"AlumnoID: {acid}, Nombre: {name}, Apellido: {lastname}")

def ActualizarDatos():
    # primero verificar que existe
    noCuenta = input("Numero de cuenta del alumno a modificar: ")
    with sqlite3.connect(db1) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT
                nombre
            FROM
                Student
            WHERE
                Student_id = ?
        """,(noCuenta,))
        existe = cur.fetchone()
        if not existe:
            print("El usuario no fue encontrado.")
        Newname = input("Nuevo Nombre del Alumno: ")
        Newlastname = input("Nuevo Apellido del Alumno: ")
        Naccount = input("Nuevo Numero de cuenta: ")
        with sqlite3.connect(db1) as conn:
            cur = conn.cursor()
            cur.execute("""
            UPDATE TABLE Student
            set nombre = ? and set apellido = ? and set Student_id =
            where Student_id = ?
            """,(noCuenta,Newname,Newlastname,noCuenta))
            print("IMPORTANTE, el numero de cuenta cambio, debes de tomarlo en cuenta la proxima ves que consultes.")

def eliminarRegistro():
    noCuenta = input("Numero de cuenta del alumno a eliminar: ")
    with sqlite3.connect(db1) as conn:
        cur = conn.cursor()
        cur.execute("""
        DELETE FROM Student
        WHERE Student_id = ?
        """,(noCuenta,))
        salio = cur.fetchone()
        if not salio:
            print("No se encontraron coincidencias")
        else:
            print("Se elimino correctamente el Alumno del sistema")

def formato():
    print("==========================")

def gestor(opcion):
    '''Basado en el CRUD'''
    match opcion:
        case 'C':
            crearAlumno()
        case 'R':
            leerAlumno()
        case 'U':
            ActualizarDatos()
        case 'D':
            eliminarRegistro()
        case _:
            return "Error`"

def menuUsuario():
    print("Menu de estudiantes")
    print("--= ABCM =--")
    print("1) Agregar Alumno 2) Eliminar Alumno 3) Modificar Alumno 4) Ver Alumnos Listados")
    estudentOption = input(">> ")
    match estudentOption:
        case '1':
            crearAlumno()
        case '2':
            eliminarRegistro()
        case '3':
            ActualizarDatos()
        case '4':
            leerAlumno()
        case _:
            ...

def menuCurso():
    print("Menu de cursos")
    print("1) ver cursos diponibles 2) Enrolar Alumno 3) Dar de baja Alumno")
    cursoOption = input(">> ")
    match cursoOption:
        case '1':
            ...
        case '2':
            ...
        case '3':
            ...
        case _:
            ...

def menuPlataforma():
    print("Menu plataformas")
    print("1) Agregar Curso 2)")
    platOption = input(">> ")
    match platOption:
        case '1':
            ...
        case '2':
            ...
        case '3':
            ...
        case _:
            ...

def main():
    sys("clear")
    while True:
        print(" -----== Menu de Gestion UAS ==----- ")
        formato()
        print("1) Consultar estudiantes\n2) Consultar cursos\n3) Consultar Plataformas\n4) Salir")
        opcion = input(">> ")
        if not isinstance(opcion,str) or not opcion.strip():
            print("Porfavor ingresa una opcion.")
        else:
            match opcion:
                case '1':
                    menuUsuario()
                case '2':
                    menuCurso()
                case '3':
                    menuPlataforma()
                case '4':
                    print("Saliendo...")
                    break
                    ...
                case _:
                    ...
main()
'''
Ejemplo del setter y getter

persona.edad // solo leer con getter
persona.edad = 21 // modificar el elemento con setter con las restricciones colocadas


'''


'''
el reto es que un estudiante se pueda inscribir
a varios cursos y ver su progreso, la plataforma
debe permitir busqueda de estudiantes, ver que cursos tienen etc.
'''

