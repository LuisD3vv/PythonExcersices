import sqlite3


try:
	con = sqlite3.connect("estudiantes.db")
	cur = con.cursor()

	nombre_user = input("Ingresa tu nombre: ")
	edad_user = int(input("Ingresa tu edad: "))

	# Para insertar varaibles ajenas, debemos de colocarle parametros tal como en el ejemplo
	cur.execute("insert into alumnos(nombre,edad) values (?,?)", (nombre_user, edad_user))
	# subir el resultado o guardar el esatdo
	con.commit()
	# impresion en caso de que salga todo bien
	print("Insersion exitosa")
except SyntaxError as error0:
	print("Tienes un error de sintaxis", error0)
except sqlite3.IntegrityError as error1:
	print("Error de integridad", error1)
except sqlite3.OperationalError as error2:
	print("Error de operacion", error2)
except sqlite3.DatabaseError as error3:
	print("Error de database", error3)
finally:
	con.close()


