#  Importar la biblioteca de sql
import sqlite3

try:
	# Crear conexion con el servidor
	con = sqlite3.connect("estudiantes.db")
	cur = con.cursor()

	# Ejecutar sentencias sql
	cur.execute("create table prueba(id,nombre,apellido,edad)")
	cur.execute("insert into prueba(id,nombre,apellido,edad) values ()")
	# con variables externo
	cur.execute("insert into prueba(id,nombre,apellido,edad) values (?,?,?),()")
	# Subir el contenido, es obligatorio porque si no se hace los cambios no se guardan
	con.commit()
except sqlite3.Error as error:
	print(f"Error {error}")

finally:
	# Cerrar la conexion
	con.close()