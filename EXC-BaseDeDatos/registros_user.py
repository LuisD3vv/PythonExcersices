import sqlite3,os

db = 'usuarios.db'
ruta = os.path.join(os.path.dirname(__file__),db)

with sqlite3.connect(ruta) as conn:
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS 
    usuarios(
    usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad integer,
    rol TEXT
    )""")

def IngresarUsuario():
    print("--===== Menu de ingreso de usuario =====--")
    while True:
        print("Ingresa el nombre del usuario")
        nombre = input(">> ")
        print("Ingresa la edad del usuario")
        edad = input(">> ")
        print("Ingresa el rol del usuario")
        rol = input(">> ")
        todos = [nombre,edad,rol]
        vacios = [campo for campo in todos if campo == ""]
        if any(vacios):
            print("Todos los campos deben de llenarse")
            continue
        else:
            break

    with sqlite3.connect(ruta) as conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO usuarios(nombre,edad,rol) VALUES (?,?,?)""",(nombre,edad,rol))
    print("Se ingreso corectamente el usuario")

def ConsultarUsuario():
    print("Como deseas realizar la consulta")
    opcion = input(">> ")
    match opcion:
        case 'individual':
            print("busqueda individual")
        case 'todos':
            print("busqueda todos")
            pass
        case 'rol':
            print("busqueda por rol")
            pass
        case _:
            print("opcion incorrecta")


def EliminarUsuario():
    ...

# 4. Consultar todo

# 5. Consultar por rol (input del usuario)


def main():
    print("========= Bienvenido =========")
    while True:
        print("Que deseas realizar el dia hoy")
        print("1) Nuevo usuario\n2) Consulta\n3) Eliminar usuario\n4) Salir")
        porHacer = input(">> ")
        match porHacer:
            case '1':
                IngresarUsuario()
            case '2':
                ConsultarUsuario()
            case '3':
                EliminarUsuario()
            case '4':
                print("hasta pronto!!")
                break
            case _:
                print("opcion incorrecta")
main()
