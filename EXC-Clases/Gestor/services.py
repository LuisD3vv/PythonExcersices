from main import Student, Course, Teacher
import db
from colorama import Fore, Style, Back
from time import sleep
import datetime

formatDate = datetime.date.today()

'''
Los datos viven donde se ejecuta la query
si otra función los necesita,
se los pasas, no los “re-preguntas” -
no podemos asumir que los conocen.
'''

"""
Rowcount -> filas afectadas (0 = ninguna, != 0 hubo cambios)
fetchone -> resultado del query (solicitud traida)
"""

# Separar responsabilidades
"""Students"""


def add_student():
    print("====--- Student Add Menu ---====")
    nombre = input("Student name: ").capitalize().strip()
    apellido = input("Student Lastname: ").capitalize().strip()
    while True:
        noCuenta = input("Account number: ")
        try:
            noCuenta = int(noCuenta)
            break
        except TypeError:
            print("The Student id must be a number.")
    if Student(nombre, apellido, noCuenta):
        con = db.databaseManage()
        cur = con.cursor()
        # insertar estudiante
        cur.execute("""INSERT INTO Student (Student_id, nombre, apellido)
                       values (?, ?, ?)""", (noCuenta, nombre, apellido))
    con.commit()
    # verificar que si se creo
    cur.execute("""SELECT Student_id
                   FROM Student
                   WHERE Student_id = ?""", (noCuenta,))
    con.commit()
    print("Student created successfully")
    sleep(2)

    con.commit()
    con.close()
    return Student(nombre, apellido, noCuenta)


def drop_student():
    noCuenta = input("Write the Student number to eliminate.")
    con = db.databaseManage()
    cur = con.cursor()
    # eliminar al estudiante
    cur.execute("""DELETE FROM Student WHERE Student_id = ?""", (noCuenta,))
    # verificar si hubo cambios en alguna fila (registro) de ser asi, entonces se imprime.
    salio = cur.rowcount()
    if salio == 1:
        print("Student Eliminated successfully")
    else:
        print(f"No coincidences for {noCuenta}")
    con.commit()
    con.close()

def modify_student():
    noCuenta = input("Type the Student account number to be modified: ")
    con = db.databaseManage()
    cur = con.cursor()
    cur.execute("""SELECT nombre FROM Student WHERE Student_id = ? """,(noCuenta,))
    existe = cur.fetchone()
    if existe:
        print(f"Student to modify: {existe[0]}")
        Newname = input("Student new name: ")
        Newlastname = input("Student new lastname: ")
        Naccount = input("New account number: ")
        cur.execute("""
        UPDATE Student SET nombre = ?, apellido = ?, Student_id = ? WHERE Student_id = ?
        """,(Newname,Newlastname,Naccount,noCuenta))
        con.commit()
        if cur.rowcount == 1:
            print("IMPORTANT, the student's account number has changed.")
            print("Consider this when you look information about this student.")
        else:
            print("The changes can't be update")
        con.close()
    else:
        print("Student Not found.")

def show_students():
    print("Showing enrolled students\n")
    con = db.databaseManage()
    cur = con.cursor()
    cur.execute("SELECT * FROM Student")
    salio2 = cur.fetchall()
    print("==============================")
    print(Back.BLACK + Fore.GREEN + "Name | Lastname | No.Account")
    print("==============================")
    for stuid, name, lastname in salio2:
        print(f"{name} {lastname}  {Fore.GREEN + str(stuid)}")
    print("==============================")
    input("Press enter to continue...")
    con.close()

def search_student(courseRol=None):
    con = db.databaseManage()
    cur = con.cursor()
    print("Select the search type\n1) Student ID/Account Number\n2) Complete Name")
    searchStudent = input(">> ")
    if searchStudent == '1':
        print("Write the student's id")
        searchStudentID = input(">> ")
        cur.execute("SELECT * FROM Student WHERE Student_id = ?", (searchStudentID,))
        userget = cur.fetchone()
        if userget is None:
            print(f"No student found with id: {searchStudentID}")
        else:
            print("-- Student found --")
            print("Displaying info")
            (Studentid, name, lastname) = userget
            print(f"Student: [{name}] [{lastname}] with {Studentid} id.")
            print("Enrolled in")
            cur.execute("""
            SELECT
                Student.nombre as 'StudentName',
                Courses.Course_Topic as Course,
                Teachers.Name as Teacher
            FROM Student
            JOIN Enrollment
                ON Student.Student_id = Enrollment.Stuid
            JOIN Courses
                ON Courses.Course_ID = Enrollment.Coursid
            JOIN Teachers
                ON Teachers.Teacher_id =  Courses.Teacher_id
            WHERE Student_id = ?""",(searchStudentID,))
            coursesRol = cur.fetchall()
            for StudentName, courseName, TeacherName in coursesRol:
                print(StudentName, courseName, TeacherName)
    elif searchStudent == '2':
        print("Write the student's name(s)")
        searchStudentName = input(">> ").strip()
        print("Write the student's lastname")
        searchStudentLastName = input(">> ").strip()
        cur.execute("""SELECT * FROM Student WHERE nombre = ? AND apellido = ? """, (searchStudentName, searchStudentLastName))
        userget = cur.fetchone()
        if userget is None:
            print("No student found with name and lastname")
        else:
            print("--- Student found ---")
            (Studentid, name, lastname) = userget
            print(f"Student {name} {lastname} with {Studentid} id.")
            print("Enrolled in")
            cur.execute("""
                SELECT
                    T.name as 'Teacher Name',
                    Course_Topic as 'Course Name'
                FROM
                    Enrollment
                JOIN main.Student S on Enrollment.Stuid = S.Student_id
                JOIN main.Courses C on Enrollment.Coursid = C.Course_ID
                JOIN main.Teachers T on C.Teacher_id = T.Teacher_id
                WHERE nombre = ?""",(name,))
            courseRol = cur.fetchall()
            for i in courseRol:
                print(i*)
    con.close()
    input("Presiona para continuar: ")

"""Courses"""


def addCourse():
    con = db.databaseManage()
    cur = con.cursor()
    while True:
        print("Input the Solicited Values")
        CTopic = input("Course Topic: ")
        CDuration = input("Duration (in minutes): ")
        CRating = input("Rating (0/5): ")
        CTeacher = input("Teacher's Name: ").strip()
        CTeacherLastname = input("Teacher's Lastame: ").strip()
        # Buscar el id de profesor mediante su nombre mas sencillo para la busqueda
        cur.execute("""SELECT Teacher_id FROM Teachers WHERE Name = ? and Lastname = ?""", (CTeacher, CTeacherLastname))
        getID = cur.fetchone() 
    # Ahora si buscamos por su id
        if getID is None:
            print(f"no coincidences for teacher with name: {CTeacher}")

        else:
            print(f"Teacher_id debug {getID[0]}")
            if Course(CTopic, float(CDuration), CRating, getID[0]):
                cur.execute("""INSERT INTO Courses (Course_Topic,Course_Duration,Course_Rating,Teacher_id) VALUES (?,?,?,?)""", (CTopic, CDuration, CRating, getID[0]))
                con.commit()
                print("Course created successfully")
                break
    con.close()

def showCourses():
    con = db.databaseManage()
    cur = con.cursor()
    cur.execute("SELECT * FROM Courses")
    impresionconsos = cur.fetchall()
    print("Available Courses")
    print("==================================================")
    print(f"|   Course  |  Duration  |  Rating  |  Teacher   |")
    print("==================================================")
    for _,name,duration,rating,teacher in impresionconsos:
        cur.execute("""SELECT Name, Lastname FROM Teachers where Teacher_id = ?""",(teacher,))
        allteacher = cur.fetchall()
        for tanme,lasname in allteacher:
            # al momento de usar colorama, despues de usar un color debemos de limparlo con style.reset_all
            print(f"[{Fore.GREEN}{name}{Style.RESET_ALL}]:\n\t    {round(float(duration/60))}hrs - {rating}/5 - {tanme} {lasname}")
    print("=================================================\n")
    input("Click to continue ")
    con.close()


"""Teachers"""

def addTeacher():
    con = db.databaseManage()
    cur = con.cursor()
    print("Menu for Add a Teacher")
    tname = input("Enter Teacher's Name: ")
    tlname = input("Enter Teacher's Lastame: ")
    while True:
        tregis = input("Enter Teacher's registration: ")
        try:
            tregis = int(tregis)
            break
        except:
            print("Teacher's id must be a number")
    cur.execute("""INSERT INTO Teachers (Name,Lastname,Registration_number) VALUES (?,?,?)""",(tname,tlname,tregis))
    con.commit()
    con.close()
    return Teacher(name=tlname,lastname=tlname,Registration_Number=tregis)

def showTeachers():
    con = db.databaseManage()
    cur = con.cursor()
    print("------ Showing Teachers ------")
    print("|  Name  |  Lastname  |  Tuition  |")
    print("-----------------------------------")
    cur.execute("""SELECT Name,Lastname,Registration_Number FROM Teachers WHERE LENGTH(Name) != 0""")
    teachgerQueryresponse = cur.fetchall()
    if teachgerQueryresponse is None:
        print("There's not teachers?")
    else:
        for Tname, Tlastname, Registration in teachgerQueryresponse:
            print(f"{Tname} {Tlastname}: {Fore.GREEN + str(Registration)}")
    print()
    con.close()
    input("Click to continue: ")


"""Enrollement"""

def enroll_student():
    con = db.databaseManage()
    cur = con.cursor()
    print("Enroll Student Menu")
    print("Enter the student id")
    studi = input(">> ")
    cur.execute("SELECT * FROM Courses")
    impresionconsos = cur.fetchall()
    print("Available Courses")
    for _, name, duration, rating, teacher in impresionconsos:
        print(f"Course: -{name}- | Duration: -{round(float(duration/60))}- Hours | Rating: {rating}/5 | Teacher: -{teacher}-")
    print("Select a course to enroll")
    ces = input(">> ")
    cur.execute("SELECT Course_ID FROM Courses WHERE Course_Topic = ?", (ces,))
    resid = cur.fetchone()
    if resid:
        cur.execute("""INSERT INTO Enrollment (Enrollment_Date,Coursid,Stuid) VALUES (?,?,?)""", (formatDate, resid[0], studi))
        sleep(2)
        print("Enrollment successfully")
    con.close()

def drop_student_data():
    con = db.databaseManage()
    cur = con.cursor()
    print("Drop a Student from a course")
    # Obtener el id del usuario
    print("Enter the Student Number")
    dropsid = input(">> ")
    cur.execute("""SELECT nombre from Student where Student_id = ?""", (dropsid,))
    dropname = cur.fetchone()
    if dropname is None:
        print("no name with account number")
    else:
        return dropsid, dropname[0]

def drop_student_show_enrolled():
    dropsid, name = drop_student_data()

    con = db.databaseManage()
    cur = con.cursor()
    courses = []
    cur.execute("""
        SELECT Courses.Course_Topic FROM Student
        JOIN Enrollment
            ON Student.Student_id = Enrollment.Stuid
        JOIN Courses
            ON Enrollment.Coursid = Courses.Course_ID
        WHERE Student_id = ?""", (dropsid,))
    rows = cur.fetchall()
    # fetch all devuelve una lista vacia en caso de no tener coincidencia, no devuelve none como fetchone, y las quieries se gastan
    if not rows:
        print(f"There no coincidences for {drop_student_data()}")
    else:
        print(f"Courses where {drop_student_data()} is enrolled")
        for courserolled in rows:
            courses.append(courserolled[0])
    return courses, name

def drop_student():
    courses, name = drop_student_show_enrolled()
    con = db.databaseManage()
    cur = con.cursor()
    for course in courses:
        print("- ", course)
    coursedropselec = input("Which course should you drop him from? (press enter to cancel): ")
    if coursedropselec not in courses:
        print("The user must be registered in the course from which they wish to be removed")
    else:
        # sacar el id del conso
        cur.execute("SELECT Course_ID FROM Courses WHERE Course_Topic LIKE ?", (f"%{coursedropselec}%",))
        idcourse = cur.fetchone()
        cur.execute("SELECT Student_id from Student WHERE nombre LIKE ?", (f"%{name}%",))
        idstudent = cur.fetchone()
        if idcourse is None and idstudent is None:
            print("There's no coincidences")
        else:
            # eliminar ya al usuario
            cur.execute("""DELETE FROM Enrollment WHERE Stuid = ? AND Coursid = ?""", (idstudent[0], idcourse[0]))
            if cur.rowcount() == 1:
                print(f"The student has been dropped from the course {coursedropselec}.")
                print("Returnig to menu...")
                sleep(1)
            else:
                print("An Error ocurred during the deleting")
    con.close()


# Podemos convertir los datos del query con row_factory

