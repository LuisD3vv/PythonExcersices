from services import *

def menu_opciones():
    opciones = [
        insertar_contacto(),
        actualizar_contacto(),
        eliminar_contacto(),
        actualizar_contacto()
    ]

    for opcion in opciones:
        print(opcion)


def main():
    print("Bienvenido al menu de Contactos ContactME!")
    print("Que deseas hacer")
    menu_opciones()
    pass

main()