def tabla(n):
    try:
        with open(f'tabla-{n}.txt','w+') as archivo:
            i = 1
            while i < 11:
                archivo.writelines(f"{n} x {i} = {n*i}\n")
                i+=1
    except FileNotFoundError:
        print("El archivo destino no existe")
    finally:
        print(f"Se escribio correctamente en el archivo tabla-{n}.txt.")
        
def mostrarTabla(n):
    try:
        with open(f'tabla-{n}.txt','r') as archivo:
            print(f"Aqui esta la tabla del {n}")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo destino no existe")
        
def buscarlinea(i):
    try:
        with open(f'tabla-{i}.txt','r') as archivo:
            linea = int(input("Que linea deseas buscar (1-10)?: "))
            if linea < 1 or linea > 10:
                print("La linea debe estar entre 1 y 10.")
                return
            archivo.seek(0)
            for i, contenido in enumerate(archivo):
                if i == linea - 1:
                    print("Contenido de la linea buscada:")
                    print(contenido)
                    return
            print("Linea no encontrada.")
    except FileNotFoundError:
        print("El archivo destino no existe")
        
def entrada(funcion):
    while True:
        n = input("Ingresa un numero entre el 1 y 10: ")
        try:
            if int(n) < 1 or int(n) > 10:
                print("El numero debe de estar en el rango.")
                continue
            n = int(n)
        except:
            print("Debes ingresar un numero.")
        else:
            funcion(n)
            break

def main():
    print("Que funcion deseas realizar?")
    print("1.- Crear tabla de multiplicar\n2.- Mostrar tabla de multiplicar\n3.- Buscar linea en tabla\n4.- Salir\n")
    instruccion = input(">> ")
    match instruccion:
        case '1':
            entrada(tabla)
        case '2':
            entrada(mostrarTabla)
        case '3':
            entrada(buscarlinea)
        case '4':
            print("Saliendo...")
            exit()
        case _:
            print("Opcion no valida.")
main()