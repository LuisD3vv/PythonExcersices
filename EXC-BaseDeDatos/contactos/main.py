from services import *


def menu_opciones():
    while True:
        system("clear")
        print("Bienvenido a ContactME!")
        print("-"*20)
        print("1) Nuevo contacto\n2) Listar contactos\n3) Eliminar contacto\n4) Modificar contacto\n5) Salir")
        print("-"*20)
        print("Que deseas realizar?")
        opcion = input(">> ")
        try:
            opcion = int(opcion)
            match opcion:
                case 1:
                    insertar_contacto()
                case 2:
                    listar_contacto()
                case 3:
                    eliminar_contacto_menu()
                case 4:
                    actualizar_contacto()
                case 5:
                    break
                case _:
                    print("Opcion invalida")
        except ValueError:
            print("La opcion debe ser numerica")

def main():
    menu_opciones()

main()
