from funcionalidad import crear_nota as cn, listar_notas as ln,buscar_nota as bn,eliminar_nota as en,exportar_notas as exn,contar_notas
import webbrowser # usar e importar rutas del navegador


url = 'https://projecthorus.netlify.app/' # ruta

cantidad_notas = contar_notas()
def main_menu():
    from os import system # importacion solo local
    while True:
        system("clear")
        print("Bienvenido a NOTE ME cli version")
        print(f"Cantidad de notas: {cantidad_notas}")
        print("=======================")
        print("1-> Crear nota\n2-> Listar notas\n3-> Buscar nota\n4-> Eliminar nota\n5-> Exportar Notas\n6-> Version web ->\n7-> Salir")
        print("Escribe el numero o la accion")
        op = input(">> ")
        print("=======================")
        
        match op:
            case "1" | "crear":
                cn()
            case "2" | "listar":
                ln()
            case "3" | "buscar":
                bn()
            case "4" | "eliminar":
                en()
            case "5" | "exportar":
                exn()
            case "6":
                print("Redirigiendote...")
                webbrowser.open(url=url,new=2) # 1 ventana  # 2 pestana
            case "7" | "salir":
                print("hasta pronto...")
                break
            case _:
                print("Selecciona una opcion dentro del menu")


main_menu()