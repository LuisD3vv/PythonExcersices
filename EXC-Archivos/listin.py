import re,os


# Este modulo para confirmar que los numeros que se metieron tienen el formato correcto
formato = re.compile(r"(\d{10})")

# archivo, mejor idea es cambiar a ruta absoluta
ruta = os.path.dirname(__file__)
archivo = 'clientes.txt'

def consultar():
    
    print("Selecciona el tipo de busqueda")
    print("1) Busqueda individual\n2) Cartera Completa")
    tipoBusqueda = input(">> ")
    if not tipoBusqueda:
        print("Ingresa una opcion.")
    match tipoBusqueda:
        case '1':
            try:
                with open(os.path.join(ruta,archivo),"r") as arch:
                # tambien se recomienda usar readline
                    next(arch) # Saltar la cabecera en este caso
                    print("Ingresa el nombre del cliente a buscar.")
                    nombreBusqueda = input(">> ").lower()
                    for linea in arch:
                        (nombre,telefono) = linea.split(",")
                        if nombreBusqueda == nombre.lower():
                            print(f"Aqui tienes la informacion sobre {nombreBusqueda}")
                            print(f"Nombre del cliente: {nombre}, Telefono Personal: {telefono}")
                            break
                        else:
                            print("No hay resultados que coincidan con la busqueda.")
            except FileNotFoundError:
                print("El archivo no existe")
        case '2':
            try:
                with open(os.path.join(ruta,archivo),"r") as arch:
                    next(arch)
                    print("Cartelera de clientes")
                    print("-----------------------")
                    for linea in arch:
                        (nombre,telefono) = linea.split(",")
                        
                        print(f"Nombre del cliente: {nombre}, Telefono Personal: {telefono}")
                    print("-----------------------")
            except FileNotFoundError:
                print("El archivo no existe")
        case _:
            print("opcion no valida")
def nuevocliente():
    try:
        with open(os.path.join(ruta,archivo),"a") as arch:
            print("Ingresa el nombre del cliente.")
            nombre = input(">> ").strip().lower()
            while True:
                print("Ingresa el numero de telefono del cliente con el siguiente formato (e.g 667-327-3581)")
                telefono = input(">> ").strip()
                if re.search(formato,telefono):
                    print("El cliente se ingreso correctamente")
                    arch.writelines(f"{nombre},{telefono}\n")
                    break
                else:
                    print("Ingresa el telefono en el formato solicitado")
                    print("-----------------------")
    except FileNotFoundError:
        print("El archivo no existe")
    
def eliminarCliente():
    copia_txt = []
    try:
        with open(os.path.join(ruta,archivo)) as arch:
            print("Ingresa el nombre del cliente a eliminar")
            nombreEliminar = input(">> ").strip().lower()
            for i in arch:
                if nombreEliminar not in i:
                    copia_txt.append(i)
            print(f"el nombre {nombreEliminar} fue eliminado")
        with open(os.path.join(ruta,archivo),"w") as resc:
            resc.writelines(copia_txt)
    except FileNotFoundError:
        print("El archivo no existe")

def funcionero(fun):
    match fun:
        case '1':
            consultar()
        case '2':
            nuevocliente()
        case '3':
            eliminarCliente()
        case _:
            print("opcion no valida")

def main():
    os.system("clear")
    while True:
        print("====================")
        print("Bienvenido a Listin")
        print("¿Que desea realizar?")
        print("1) Consultar Cliente\n2) Añadir Cliente\n3) Eliminar Cliente\n4) Salir")
        opcion = input(">> ")
        if opcion == '4':
            break
        funcionero(opcion)
    
main()