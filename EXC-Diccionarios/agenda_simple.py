from os import system
agenda = []

def agregar_contacto():
    system("clear")
    print("Menu actual -> Agregar Contacto")
    print("Nombre:")
    nombre = input(">> ")
    print("Telefono: ")
    telefono = input(">> ")
    agenda.append({"nombre":nombre,"telefono":telefono})

def buscar_contacto():
    system("clear")
    print("Menu actual ->  Buscar Contacto")
    print("Nombre:")
    nombre = input(">> ").strip()
    for contacto in agenda:
        if contacto.get('nombre','no encontrado') == nombre:
            print(f"Aqui esta el telefono: {contacto.get('telefono','sin numero')} del contacto {nombre}.")

def eliminar_contacto():
    system("clear")
    print("Menu actual ->  Eliminar Contacto")
    nombre = input(">> ").strip()
    for contacto in agenda: # contacto es todo el diccionario completo que se esta iterando.
        if contacto["nombre"]== nombre: #@ si la el valor de la clave nombre de ese diccionario es ==
            agenda.remove(contacto) # entocnes borramos esa instancia completa
            print(f"contacto {nombre} eliminado.")
            break

def modificar_contacto():
    pass

system("clear")
while True:
    print("Lissandro's Contact Menu")
    print("1 Agregar contacto\n2 Buscar contacto\n3 Eliminar contacto\n4 Salir")
    op = input(">> ")
    try:
        op = int(op)
        match op:
            case 1:
                agregar_contacto()
            case 2:
                buscar_contacto()
            case 3:
                eliminar_contacto()
            case 4:
                break
            case _:
                print("Selecciona una opcion dentro del menu")
    except ValueError:
        print("Ingresa una opcion numerica")