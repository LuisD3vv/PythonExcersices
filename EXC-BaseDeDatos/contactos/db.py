from contextlib import contextmanager
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
db = 'contactos.db'
file = BASE / db

class Safe_DB(sqlite3.Connection):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) # super clase

    def simple_dml_query(self,query,params=()):
        try:
            # El orden es tal y como lo pide la funcion execute (metodo)
            cur = self.execute(query,params)
            print("Regresando:",cur.rowcount)
            return cur.rowcount
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            return -1

    def get_one(self,query,params=()):
        try:
            cur = self.execute(query,params)
            return cur.fetchone()
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            return -1
    def get_all(self,query,params=()):
        try:
            cur = self.execute(query,params)
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            return -1

@contextmanager
def cargar_Safe_DB():
    con = None
    try:
        #* Utilizandolo asi, podemos uasrla sin pasarle parametro cada rato
        con = sqlite3.connect(file,timeout=15,factory=Safe_DB,check_same_thread=True)
        yield con # convertir la funcion en un generador en lugar de usar un retur
    except sqlite3.Error as e:
        raise RuntimeError(f"Error: {e}") #* Es una excepcion que ocurre mientras el programa se esta ejecutando, fallo imprevisto que detiene la ejecucion
    finally: # cuando sale se cierra
        if con:
            con.close()

def iniciar_db():
    with sqlite3.connect(file)as con:
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            contacto_id INTEGER PRIMARY KEY,
            nombre VARCHAR(35) NOT NULL,
            apellido VARCHAR(35) NOT NULL,
            correo VARCHAR(35) UNIQUE NOT NULL,
            telefono VARCHAR(11) DEFAULT('0000000000'))
        """)
        con.commit()
iniciar_db()