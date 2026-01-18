import sqlite3
import os

db = "GestorUas.db"
file = os.path.join(os.path.dirname(__file__),db)

def databaseManage():
    try:
        conn = sqlite3.connect(file)
        return conn
    except sqlite3.OperationalError as o:
        print(f"Operational error{i}")
    except sqlite3.IntegrityError as i:
        print(f"Integrity error{i}")
    except sqlite3.Error as e:
        print(f"Error -> {e}")

def set_upDatabases():
    con = databaseManage()
    con.execute("""
    CREATE TABLE IF NOT EXISTS Student (Student_id integer, nombre varchar(50), apellido varchar(50))
    """)
    con.execute("""
    CREATE TABLE IF NOT EXISTS Teachers (
        Teacher_ID INTEGER  PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR (50),
        Lastname VARCHAR (50),
        Registration_number INTEGER
    )
    """)
    con.execute("""
    CREATE TABLE IF NOT EXISTS Courses (
        Course_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Course_Topic VARCHAR(40),
        Course_Duration Decimal(2,1),
        Teachid INTEGER REFERENCES Teachers(Teacher_ID)
    )
    """)
    con.execute("""
    CREATE TABLE IF NOT EXISTS Enrollment (
        Enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Enrollment_Date date,
        Coursid INTEGER REFERENCES Courses(Course_ID),
        Stuid INTEGER REFERENCES Student(Student_id)
    )
    """)
    con.close()

set_upDatabases()