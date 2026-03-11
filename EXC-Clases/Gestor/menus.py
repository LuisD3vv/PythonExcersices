from time import sleep
from colorama import Fore, Back,Style
import Utilities as U
import services as S

"""
    Autor:
    Luis Alejandro Aguilar Soberanes

    Modulo de Funciones Procedimentales.
"""

def students_menu()-> None:
    U.clear()
    print(f"{Back.BLACK} {Fore.GREEN}--= Menu de administracion de estudiante =--{Style.RESET_ALL}")
    U.format()
    print("1) Nuevo estudiante\n2) Dar de baja estudiante\n3) Modificar estudiante\n4) Todos los estudiantes\n5) Buscar estudiante")
    U.format()
    print("Que quieres hacer?")
    estudentOption = input(">> ").strip()
    if estudentOption == "":
        pass
    else:
        match estudentOption:
            case '1':
                S.nuevo_alumno()
            case '2':
                S.eliminar_alumno()
            case '3':
                S.modificar_alumno()
            case '4':
                S.mostrar_estudiantes()
            case '5':
                S.buscar_estudiante()
            case _:
                U.clear()
                print(f"{Back.RED} {Fore.WHITE}Porfavor selecciona una opcion.{Style.RESET_ALL}\n")
    U.clear()

def courses_menu()-> None:
    U.clear()
    U.format()
    print(f"{Back.BLACK} {Fore.GREEN}--= Cursos =--{Style.RESET_ALL}\n")
    print("1) Mostrar Cursos\n2) Nuevo Curso\n3) Filtrar Curso\n4) Buscar Curso\n")
    U.format()
    print("Que quieres hacer?")
    courseoption = input(">> ")
    match courseoption:
        case '1':
            S.mostrar_curso()
        case '2':
            S.nuevo_curso()
        case '3':
            S.buscar_curso('1')
        case '4':
            S.buscar_curso('2')
        case _:
            print(f"{Back.RED} {Fore.WHITE}Porfavor selecciona una opcion.{Style.RESET_ALL}\n")
    U.format()
    U.clear()

def teachers_menu()-> None:
    U.clear()
    U.format()
    print(f"{Back.BLACK} {Fore.GREEN}--= Maestros =--{Style.RESET_ALL}\n")
    print("1) Maestros Registrados\n2) Nuevo Maestro\n3) Filtrar\n4) Buscar Maestro\n")
    U.format()
    print("Que quieres hacer?")
    teacheroption = input(">> ")
    match teacheroption:
        case '1':
            S.mostrar_maestros()
        case '2':
            S.nuevo_maestro()
        case _:
            print(f"{Back.RED} {Fore.WHITE}Porfavor selecciona una opcion.{Style.RESET_ALL}\n")
    U.format()
    U.clear()

def enrollements_menu()-> None:
    U.clear()
    U.format()
    print(f"{Back.BLACK} {Fore.GREEN}--= Inscripciones =--{Style.RESET_ALL}\n")
    print("1) Inscribir estudiante \n2) Eliminar a un estudiante de un curso")
    U.format()
    print("Que quieres hacer?")
    platOption = input(">> ")
    match platOption:
        case '1':
            S.inscribir()
        case '2':
            # Pendiente
            S.dar_de_baja()
        case _:
            print(f"{Back.RED} {Fore.WHITE}Porfavor selecciona una opcion.{Style.RESET_ALL}\n")
    U.format()
    U.clear()


def main()->None:
    '''
    Funcion centrar para manejar las funciones extras1
     de cada clase
    Args:
        none
    Returns:
        none
    '''
    options = ["Administrar estudiantes <-", "Administrar cursos", "Administrar maestros", "Inscripciones", "Limpiar consola", "Salir ->"]
    print("Cargando...")
    sleep(1)
    U.clear()
    print("Listo!!")
    sleep(1)
    U.clear()
    while True:
        U.print_header()
        for i, option in enumerate(options, start=1): # en lugar de que inicie con el 0
            print(f"{Fore.BLACK}{str(i)}.- {Fore.YELLOW}{option}{Style.RESET_ALL}")
        print("-"*32)
        print("Escribe la opcion o ingresa el numero.")
        opcion = input(">> ").capitalize()
        if not isinstance(opcion, str) or not opcion.strip():
            print(f"{Back.RED} {Fore.WHITE}Porfavor selecciona una opcion.{Style.RESET_ALL}\n")
        else:
            match opcion:
                case '1' | 'Students':
                    students_menu()
                case '2' | 'Courses':
                    courses_menu()
                case '3' | 'Teachers':
                    teachers_menu()
                case '4' | 'Enrollment':
                    enrollements_menu()
                case '5' | 'clear':
                    print("Cleaning...")
                    sleep(1)
                    U.clear()
                case '6' | 'Exit':
                    U.clear()
                    print("Saliendo...")
                    sleep(1)
                    U.clear()
                    break
                case _:
                    print(f"{Back.RED} {Fore.WHITE}Porfavor selecciona una opcion.{Style.RESET_ALL}\n")
    U.clear()

main()

