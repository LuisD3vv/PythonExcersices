import sqlite3
import os

"""
    Autor:
    Luis Alejandro Aguilar Soberanes
    
    Modulo de Inciacion y prueba de base de datos.
"""

db = "GestorUas.db"
file = os.path.join(os.path.dirname(__file__),db)

def databaseManage():
    try:
        conn = sqlite3.connect(file)
        return conn
    except sqlite3.OperationalError as o:
        print(f"Operational error{o}")
    except sqlite3.IntegrityError as i:
        print(f"Integrity error{i}")
    except sqlite3.Error as e:
        print(f"Error -> {e}")

def set_upDatabases():
    con = databaseManage()
    con.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
	id_estudiante INTEGER,
	nombre varchar(40) NOT NULL,
	apellido varchar(40) NOT NULL,
	correo varchar(30) UNIQUE,
	PRIMARY KEY(id_estudiante)
    )
    """)

    con.execute("""
    CREATE TABLE IF NOT EXISTS maestros (
	nombre	VARCHAR(50) NOT NULL,
	apellido	VARCHAR(50) NOT NULL,
	Numero_de_registro	INTEGER,
	PRIMARY KEY(Numero_de_registro)
    )
    """)
    # Pendiente abreviacion.
    con.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
	id_curso	INTEGER PRIMARY KEY,
	topico_del_curso	VARCHAR(40) NOT NULL,
	duracion	INTEGER 
    CHECK (duracion > 0),
	calificacion	DECIMAL(2, 1)
    CHECK (calificacion > 0),
	id_maestro	INTEGER,
	FOREIGN KEY(id_maestro) REFERENCES maestros(id_maestro)
    )
    """)
    # autoincremento en sqlite con: INTEGER PRIMARY KEY, nada de serial o autoincrement.
    con.execute("""
    CREATE TABLE IF NOT EXISTS inscripciones (
    id_inscripcion	INTEGER PRIMARY KEY,
    fecha_inscripcion DATE DEFAULT CURRENT_DATE,
    id_curso	INTEGER,
    id_estudiante INTEGER,
	FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
	FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante)
    )
    """)
    con.close()

set_upDatabases()