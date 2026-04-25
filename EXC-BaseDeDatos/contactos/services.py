from os import system
from contacto import Contacto
from db import cargar_Safe_DB
import re

patron = r'\d{3}-\d{7}' # 667-3273581 
patron_correo = re.compile(r'(\w+)((\.\w+)*)@(\w+)((\.\w+)+)') # SEPARADO POR GRUPOS3

COLUMNAS_VALIDAS = {1:'nombre',2:'apellido',3:'correo',4:'telefono'}

def validar_nombre():
    valido = 0
    while not valido:
        nombre = input("Nombre(s) del contacto: ")
        if not isinstance(nombre, str) or not nombre.strip():
            print("Nombre inválido")
        else:
            valido= 1
            return nombre.strip()

def validar_apellido():
    valido = 0
    while not valido:
        apellido = input("Apellido(s) del contacto: ")
        if not isinstance(apellido, str) or not apellido.strip():
            print("Apellido inválido")
        else:
            valido= 1
            return apellido.strip()

def validar_correo():
    valido = 0
    while not valido:
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        correo = input("Correo: ")
        if not re.match(patron, correo):
            print("Correo inválido")
        else:
            valido= 1
            return correo

def validar_telefono():
    valido = 0
    while not valido:
        patron = r"^\d{10}$"
        telefono = input("Telefono: ")
        if len(telefono) < 10:
            print("Debes ingresar 10 digitos contando el guion.")
        if not re.match(patron, telefono):
            print("Teléfono inválido")
        else:
            valido = 1
            return telefono


def insertar_contacto() -> Contacto:
    system("clear")
    print("Menu para ingresar contacto (n) para salir (enter) para continuar")
    seguir = input("")
    if seguir == "":
        print("Ingresa los datos solicitados.")
        # separamos responsabilidades y optimizamos el flujo
        nombre = validar_nombre()
        apellido = validar_apellido()
        correo  = validar_correo()
        telefono = validar_telefono()

        # validar y crear objeto
        Contacto(nombre,apellido,correo,telefono)

        print("Contacto agregado exitosamente")
        
    else:
        return
    input("Enter para continuar...")
    return ingresar_contacto_db(nombre,apellido,correo,telefono)

def ingresar_contacto_db(nombre,apellido,correo,telefono)-> int:
    with cargar_Safe_DB() as con:
            query = con.simple_dml_query("insert into contactos(nombre,apellido,correo,telefono) values(?,?,?,?)",(nombre,apellido,correo,telefono))
            con.commit()
            if query > 0:
                print("Contacto agregado")
                return 1
            else:
                return 0

def listar_contacto():
    system("clear")
    
    with cargar_Safe_DB() as con:
        res = con.get_all("select nombre,apellido,correo,telefono from contactos")
        if len(res) == 0:
            print("No has agregado ningun contacto aun!.")
        else:
            print("Contactos disponibles\n")
            print("-"*65)
            print("\tNombre\t\t\tCorreo\t\t\tTelefono")
            print("-"*65)
            for contactos in res:
                nombre,apellido,correo,telefono = contactos
                print(f"{nombre} {apellido} | {correo} | {telefono.replace("-","")}")    
    input("Presiona enter para continuar...")

def menu_actualizar(contacto_id) -> int:
    system("clear")
    if contacto_id != None and isinstance(contacto_id,int):
        while True:
            print(f"Que Atributo deseas modificar: ")
            print("-"*5)
            for clave,valor in COLUMNAS_VALIDAS.items():
                print(f"{clave}) {valor.capitalize()}")
            atributo = int(input(">> "))
            if atributo in COLUMNAS_VALIDAS.keys():
                print(f"Ingresa el nuevo {COLUMNAS_VALIDAS.get(atributo)}: ")
                nuevo_valor = input(">> ").strip()
                # mejorar utilizando acceso directo.
                columna = COLUMNAS_VALIDAS.get(atributo,"no se encontro el atributo")
                if columna is None:
                    raise ValueError("Atributo invalido")
                with cargar_Safe_DB() as con:
                    query = con.simple_dml_query(f"UPDATE contactos set {columna} = ? where contacto_id = ?",(nuevo_valor,contacto_id))
                    con.commit()
                if query > 0:
                    print("contacto actualizado con exito.")
                    return 1
                else:
                    print("No se ha actualizado correctamente el atributo.")
                    return 0

def actualizar_por_nombre(nombre,apellido) -> int:
    with cargar_Safe_DB() as con:
        # Solo regresa una tupla.
        res = con.get_one("select contacto_id from contactos where (nombre = ?) and (apellido = ?)",(nombre,apellido))
        if res is None:
            print(f"sin resultados para {nombre} {apellido}")
            return 0
        else:
            if len(res) > 0:
                print(f"Coincidencia -> {res[0]}")
                print(f"salida -> {res}")
                cotact_id =res[0] # desempaquetar lista -> mejorar.
                menu_actualizar(cotact_id)
                return 1

def actualizar_por_telefono(telefono) -> int:
    with cargar_Safe_DB() as con:
        res = con.get_all("SELECT contacto_id from contactos where telefono = ?",(telefono,))
        if not res:
            print("No se ha encontrado ningun contacto con ese numero registrado")
            return 0
        else:
            if len(res) > 0:
                print(f"Coincidencia -> {res[0]}")
                print(f"salida -> {res}")
                cotact_id = res[0]
                menu_actualizar(cotact_id)
                return 1

def actualizar_por_correo(correo)  -> int:
    with cargar_Safe_DB() as con:
        res = con.get_all("SELECT contacto_id from contactos where correo = ?",(correo,))
        if not res:
            print("No se ha encontrado ningun contacto con ese numero registrado")
            return 0
        else:
            if len(res) > 0:
                print(f"Coincidencia -> {res[0]}")
                print(f"salida -> {res}")
                cotact_id =res[0][0] # desempaquetar lista -> mejorar.
                menu_actualizar(cotact_id)
                return 1


def actualizar_contacto()-> int:    
    system("clear")
    print("Menu de actualizacion")
    while True:
        print("Selecciona como deseas buscar el contacto.")
        print("-"*20)
        print("1) Nombre \n2) Telefono \n3) Correo\n4) Regresar")
        tbusqueda = input(">> ").strip()
        try:
            tbusqueda = int(tbusqueda)
            match tbusqueda:
                case 1:
                    print("Busqueda por nombre")
                    print("Ingresa los nombre(s) y apellido(s).")
                    nombre  = input("Nombre: ").strip()
                    apellido = input("Apellido: ").strip()
                    actualizar_por_nombre(nombre,apellido)
                case 2:
                    print("Busqueda por telefono")
                    while True:
                        print("Escribe el numero: ")
                        numeroTel = input(">> ").strip()
                        lista=[]
                        for i,numero in enumerate(numeroTel):
                            if i == 3:
                                lista.append("-")
                            lista.append(numero)
                        numeroTel = "".join(lista)
                        if not numeroTel.strip():
                            print("Ingresa un numero de telefono")
                            continue
                        if not re.search(patron,numeroTel):
                            print("Porfavor ingresa el telefono con el formato correcto")
                            continue 
                        else:                           
                            print(actualizar_por_telefono(numeroTel))
                            break
                case 3:
                    print("Busqueda por correo")
                    print("Ingresan el correo del contacto")
                    correo = input(">> ").strip()
                    if re.search(patron_correo,correo):
                        actualizar_por_correo(correo)
                    else:
                        print("Porfavor escribe el correo en el formato correcto")
                case 4:
                    return None
                case _:
                    print("Elige una opcion valida")
        except ValueError:
            print("La opcion debe ser numerica")
    input("presiona enter para continuar")

# Puede regresar o un eestado de error/exito o un None.
def eliminar_contacto_busqueda_id(op,*args) -> int | None:
    QUERYS_VALIDOS = [                    "nombre = ? and apellido = ?","correo = ?","telefono = ?"]
    with cargar_Safe_DB() as con:
        match op:
            case 'nombre':
                nombre=args[0]
                apellido=args[1]
                query = QUERYS_VALIDOS[0]
                res = con.get_all(f"select contacto_id from contactos where {query}",(nombre,apellido))
            case 'correo':
                correo = args[0]
                query = QUERYS_VALIDOS[1]
                res = con.get_all(f"select contacto_id from contactos where {query}",(correo,))
            case 'tel':
                tel = args[0]
                query = QUERYS_VALIDOS[2]
                res = con.get_all(f"select contacto_id from contactos where {query}",(tel,))
            case _:
                print("Opcion invalida")
        if not res: # porque aunque no haya resultado regresa []
            print(f"sin resultados")
            return None
        print(f"res_id --> {res[0][0]} --> dtype {type(res)}")
        eliminar_contacto(res[0][0]) # id evitar error de binding

def eliminar_contacto_por_nombre():
    print("Busqueda por nombre")
    print("Ingresa los nombre(s) y apellido(s) separados por un espacio.")
    nombre = validar_nombre()
    apellido = validar_apellido()
    eliminar_contacto_busqueda_id('nombre',nombre,apellido)

def eliminar_contacto_por_correo():
    print("Busqueda por correo")
    eliminar_contacto_busqueda_id('correo',validar_correo())

def eliminar_contacto_por_telefono():
    print("Busqueda por telefono")
    numeroTel = validar_telefono()
    eliminar_contacto_busqueda_id('tel',numeroTel)

def eliminar_contacto_menu() -> int:
    system("clear")
    print("Menu para eliminar contacto")
    while True:
        print("Selecciona como deseas buscar el contacto.")
        print("-"*20)
        print("1) Nombre \n2) Telefono \n3) Correo\n4) Regresar")
        tbusqueda = input(">> ").strip()
        try:
            tbusqueda = int(tbusqueda)
            match tbusqueda:
                case 1:
                    eliminar_contacto_por_nombre()
                case 2:
                    eliminar_contacto_por_telefono()
                case 3:
                    eliminar_contacto_por_correo()
                case 4:
                    return None
                case _:
                    print("Elige una opcion valida")
        except ValueError:
            print("La opcion debe ser numerica")
    input("Presiona enter para continuar...")

def eliminar_contacto(contacto_id):
    if contacto_id is not None:
        with cargar_Safe_DB() as con:
            query = con.simple_dml_query("delete from contactos where contacto_id = ?",(contacto_id,))
            con.commit()
            if query > 0:
                print("contacto eliminado con exito.")
                return 1
            else:
                print("No se ha eliminado correctamente.")
                return 0
    else:
        print("No hubo resultados.")