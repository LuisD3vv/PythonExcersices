from pathlib import Path
import re
from datetime import datetime
import zipfile
from db import iniciar_bases_de_datos,cargar_db
from os import system as sys
import json

def contar_notas():
    with cargar_db() as con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM notas")
        total = cur.fetchone()
        if total is None:
            return "hubo un error al cargar las notas"
        else:
            if total[0] == 0:
                return "No hay notas"
            else:
                return total[0]
    return None


def guardar_nota(titulo,contenido):
    sys("clear")
    titulo = titulo.strip().lower()
    contenido = contenido.strip().lower()
    fecha_actual = datetime.now().strftime("%d/%m/%Y") # Fecha
    if contenido == "":
        print("No se ha recibido nada")
        return False
    with cargar_db() as con:
        cur = con.cursor()
        cur.execute("""INSERT INTO notas (titulo,contenido,fecha) VALUES (?,?,?)""",(titulo,contenido,fecha_actual))
        con.commit()
        if cur.rowcount > 0:
            return True
        con.close()
    input("Presiona enter para continuar...")

def crear_nota():
    sys("clear")
    print("Ingresa el titulo de la nota: ")
    titulo = input(">> ")
    contenido = []
    if titulo != "":
        print("Escribe el contenido de la nota:")
        while True:
            texto = input(">> ")
            if texto.upper() == "FIN":
                break
            contenido.append(texto)
    else:
        print("Escribe un titulo")    
    final = "\n".join(contenido) # se convierte en un string
    if len(final) == 0:
        print("Ingresa algo a la nota")
    else:
        if guardar_nota(titulo,final):
            print("La nota se guardo correctamente.")
        else:
            print("Hubo un problema al guardar tu nota, posiblemente esta vacia.")
    input("Presiona enter para continuar...")

def listar_notas():
    sys("clear")
    with cargar_db() as con:
        cur = con.cursor()
        cur = con.execute("""SELECT titulo,contenido FROM notas""")
        todos = cur.fetchall()
        if todos is None:
            print("No hay ninguna nota registrada, se el primero!")
            return None
        else:
            print("Notas disponibles:")
            for titulo,_ in todos:
                print(f"-{titulo}")
    input("Presiona enter para continuar...")       

def buscar_nota():
    sys("clear")
    with cargar_db() as con:
        cur = con.cursor()  
        print("Ingresa el titulo de la nota")
        titulo_busqueda=input(">> ")
        if titulo_busqueda.strip() == "":
            print("Porfavor ingresa el contenido")
        else:
            cur.execute("""
            SELECT contenido FROM notas WHERE titulo = ?
            """,(titulo_busqueda,))
            busqueda = cur.fetchone()
            if busqueda is None:
                print("No hay resultado con el titulo")
            else:
                print(f"Contenido de `{titulo_busqueda}`")
                print("---------------------")
                print(*busqueda)
                print("---------------------")
    input("Presiona enter para continuar...")

def eliminar_nota():
    sys("clear")
    with cargar_db() as con:
        cur = con.cursor()        
        print("Ingresa el titulo de la nota a eliminar: ")
        titulo = input(">> ")
        if titulo.strip() == "":
            print("Porfavor ingresa el titulo")
        # Borrar
        else:
            cur.execute("""DELETE FROM notas WHERE titulo = ?""",(titulo,))
            con.commit()
            # Comprobar
            if cur.rowcount == 1:
                print(f"Se ha eliminado con exito la nota: `{titulo}`")
            else:
                print(f"No se ha eliminado correctamente la nota.")
    input("Presiona enter para continuar...")

def exportar_notas():
    sys("clear")
    todo = {}
    seguir = False
    print("Deseas exportar todas las notas (si-no)?")
    opcion = input(">> ").strip()
    with cargar_db() as con:
        if opcion == "si":
            cur = con.cursor()
            cur.execute("""SELECT titulo,contenido from notas""")
            todas = cur.fetchall()
            if todas is None:
                print("No hay registros para exportar.")
                return None
            else:
                seguir = True
                for titulos,contenidos in todas:
                    todo[titulos] = contenidos
            if seguir:
                with open('notas.json','w') as file,zipfile.ZipFile('notas.zip','w') as mi_zip:
                    file.write(json.dumps(todo,indent=2,allow_nan=False)) # convertirlo en json, ya que dict tiene una estructura similar
                    mi_zip.write('notas.json')
                    print("Se han exportado correctamente.!!")
                    print("Nombre: notas.zip")
        else:
            main_menu()
