from contextlib import contextmanager
import sqlite3 
from pathlib import Path

# con Path(file) ya obtenemos la ruta de lo que este adentro y sera un objeto path

# siempre es mejor trabajar con rutas absolutas.

BASE_DIR = Path(__file__).resolve().parent # DIRECTORIO BASE / resolve -> ruta absoluta y .parent devuelve la ruta padre (de)
ruta = BASE_DIR / "notas.db"


# Crear un factory persnoalizado con el objeto  sqlite3.Connection, que nos permite 
# Personalizar ciertas cosas del objeto como agregar ciertas comprobaciones o impresiones
class Notas_safe(sqlite3.Connection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    # mejor manera para trabajr con metodos y mueveSQlo
    def ejecucion_segura(self, query,params=()):
        self.execute(sql, params)
        self.commit()

    def notas_dmd(self,query,params=()):
        try:
            cur = self.execute(query, params)
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            raise
    def notas_single_query(self,query,params=()): 
        try:
            cur = self.execute(query, params)
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            raise

    def notas_get_all(self,query,params=()):
        try:
            cur = self.execute(query, params)
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error en query: {e}")
            raise

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
        notas = con.ejecucion_segura("""
        CREATE TABLE IF NOT EXISTS notas (
        id_nota  INTEGER PRIMARY KEY, -- Autoincrement lento y pesado
        titulo text NOT NULL,
        contenido text NOT NULL,
        fecha DATE DEFAULT CURRENT_DATE
        )
        """)
        con.commit() # necesario
iniciar_bases_de_datos()