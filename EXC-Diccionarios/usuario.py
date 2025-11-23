import re,os,platform


def limpiar():
    if platform.system() == "Linux":
        return "clear"
    elif platform.system() == "Windows":
        return "cls"



os.system(limpiar())
formato = re.compile(r"(\d{10})") # formato para telefono

usuarios = []

def verifTel():
    print("Escribe el telefono")
    tel = input(">> ")
    if not re.search(formato,tel):
        print("ingresa el numero en el formato comun a 10 digitos.") 
        return None
    return tel  

    
def verifNombre():
    print("Escribe el nombre")
    nombre = input(">> ")
    if nombre == "":
        print("el nombre no debe estar vacio.")
        return None
    return nombre

def verifEdad():
    print("Escribe la edad")
    edad = input(">> ")
    try:
        edad = int(edad)
    except ValueError:
        print("La edad debe de ser un numero.")
        return None
    return edad

def verDirect():
    print("Escribe tu direccion")
    direct = input(">> ")
    if direct == "":
        print("La direccion no debe estar vacia.")
        return None
    return direct


def main():
    print("Cuantos usuarios desea ingresar?")
    n = int(input(">> "))
    i = 0
    while i < n:
        print("Usuario No.{}".format(i+1))
        while True:
            nombre = verifNombre()
            edad = verifEdad()
            telefono = verifTel()
            direccion = verDirect()
            # validando que todos los valores.
            if all([nombre,edad,telefono,direccion]):
                usuarios.append({"nombre":nombre,"edad":edad,"telefono":telefono})
                break
            else:
                os.system(limpiar())
                print("Hay valores mal ingresados, intenta de nuevo")
        i+=1
main()


for i,user in enumerate(usuarios):
    print(f"{i+1}-> {user['nombre']} tiene {user['edad']} años y su numero de telefono es {user['telefono']}")