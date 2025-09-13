# importar la libreria
import sqlite3
# crear la coneccion
con = sqlite3.connect("estudiantes.db")

# Ejecutar acciones
cur = con.cursor()

# ejecutar una consulta e iterar sobre
for row in cur.execute("select * from alumnos"):
	print(row)

# Guardar los cambios
con.commit()

# Podemos cerrar la conexion si ya esta hecho lo que necesitamos
con.close()
