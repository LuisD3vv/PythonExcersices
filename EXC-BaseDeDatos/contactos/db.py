from contextlib import contextmanager
import sqlite3
from pathlib import Path

BASE = Path(__file__).parent().resolve
db = 'contactos.db'
file = BASE / db


class Safe_DB(sqlite3.Connection):
    def __init__(self,*args,**kwargs):
        super(*args,**kwargs)
    
    def simple_dml_query(self,query,params=()):
        try:
            # El orden es tal y como lo pide la funcion execute (metodo)
            cur = self.execute(query,params)
            return cur.rowcount
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            raise

    def get_one(self,query,params=()):
        try:
            cur = self.execute(query,params)
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            raise

    def get_all(self,query,params=()):
        try:
            cur = self.execute(query,params)
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            raise


@contextmanager
def cargar_Safe_DB():
    con = None
    try:
        #* Utilizandolo asi, podemos uasrla sin pasarle parametro cada rato
        con = sqlite3.connect(ruta,timeout=15,factory=Safe_DB)
        yield con # convertir la funcion en un generador en lugar de usar un retur
    except sqlite3.Error as e:
        raise RuntimeError(f"Error: {e}") #* Es una excepcion que ocurre mientras el programa se esta ejecutando, fallo imprevisto que detiene la ejecucion
    finally: # cuando sale se cierra
        if con:
            con.close()

def iniciar_db():
    with sqlite3.connect(file,factory=DB)as con:
        cur = con.cursor()
        cur.execute("""
        CREATE IF NOT EXIST contactos (
            contacto_id INTEGER PRIMARY KEY
            nombre VARCHAR(35) NOT NULL,
            apellido VARCHAR(35) NOT NULL,
            correo VARCHAR(35) UNIQUE NOT NULL,
            telefono VARCHAR(10) DEFAULT='000-000-000
        )
        """)
        con.commit()
iniciar_db()