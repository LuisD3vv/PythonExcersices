from contextlib import contextmanager
import sqlite3
from os import path

"""
    Autor:
    Luis Alejandro Aguilar Soberanes
    
    Modulo de Inciacion y prueba de base de datos.

    16/03/26
"""

# os

db = 'NoteME.db'
file = path.join(path.dirname(__file__),db)

# path

# BASE_DIR = Path(__file__).resolve().parent # DIRECTORIO BASE / resolve -> ruta absoluta y .parent devuelve la ruta padre (de)
# ruta = BASE_DIR / "NoteME.db"
class Notas_safe(sqlite3.Connection):
    """
    Clase que hereda todos los metodos de connection, es la razon
    del porque podemos usar self.tal()
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # mejor manera para trabajar con metodos y mueveSQlo, funciona como una capa de seguridad en consultas
    def query(self, sql,params=()):
        """
            Este patron se llama muchas veces DAL (Data Access Layer)
        """
        try:
            cur = self.execute(sql, params)  # genera automaticamente el cursor  = cursor() + execute()

            # consultas con select
            if sql.strip().upper().startswith("SELECT"):
                return cur.fetchall() # para consultas que traen datos

            # para insert/update/delete y create
            self.commit()
            return cur.rowcount # conteo de resultados > 0 igual exito


        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            raise

        def safe_execution(self,sql,params=()):
            self.execute(sql,params)
            self.commit()

@contextmanager
def cargar_db(): 
    '''
    Funcion generadora, que mantiene abierta la conexion, se pausa y luego vuelve. gracias a yield
    '''
    con = None
    try:
        #* Utilizandolo asi, podemos uasrla sin pasarle parametro cada rato
        con = sqlite3.connect(ruta,timeout=15,check_same_thread=True,factory=Notas_safe)
        yield con # convertir la funcion en un generador en lugar de usar un retur
    except sqlite3.Error as e:
        raise RuntimeError(f"Error: {e}") #* Es una excepcion que ocurre mientras el programa se esta ejecutando, fallo imprevisto que detiene la ejecucion
    finally: # cuando sale se cierra
        if con:
            con.close()

def iniciar_bases_de_datos():
    with cargar_db() as con:
        notas = con.safe_execution("""
        CREATE TABLE IF NOT EXISTS notes (
        note_id  INTEGER PRIMARY KEY, -- Autoincrement lento y pesado, integer ya es autoincremental por defecto
        title text NOT NULL,
        content text NOT NULL,
        date DATE DEFAULT CURRENT_DATE
        )
        """)
        con.commit() # necesario por el yield
        
iniciar_bases_de_datos()