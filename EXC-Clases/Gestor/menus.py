from time import sleep
from pathlib import Path
from datetime import datetime
from colorama import init,Fore,Back,Cursor,Style
from main import Student,Course,Teacher
import Utilities as U
import services as S

def Studentmenu():
    U.Clear()
    print("Students Managment Menu\n")
    print("="*24)
    print("1) Add Student\n2) Delete Student\n3) Modify Student Info\n4) View all Students\n5) Search Student by")
    print("="*24)
    print("What do you want to do?")
    estudentOption = input(">> ").strip()
    if estudentOption == "":
        pass
    else:
        match estudentOption:
            case '1':
                S.add_student()
            case '2':
                S.drop_student_data()
            case '3':
                S.modify_student()
            case '4':
                S.show_students()
            case '5':
                S.search_student()
            case _:
                print(Back.RED + Fore.WHITE + f"Please select a option")
    U.Clear()

def CourseMenu():
    print("="*28)
    print("--= Course's menu option =--")
    print("1) Show courses\n2) Add Course")
    print("="*28)
    courseoption = input(">> ").strip()
    match courseoption:
        case '1':
            S.show_courses()
        case '2':
            S.add_course()
        case _:
            print(Back.RED + Fore.WHITE +f"Please select a option")

    print("="*28)
    U.Clear()

def Teachermenu():
    U.Clear()
    print("="*28)    
    print("--= Teacher's menu option =--")
    print("1) Show teachers\n2) Add teacher")
    print("="*28)
    teacheroption = input(">> ").strip()
    match teacheroption:
        case '1':
            S.show_teachers()
        case '2':
            S.add_teacher()
        case _:
            print(Back.RED + Fore.WHITE + f"Please select a option")

    print("="*28)
    U.Clear()

def Enrollementmenu():
    print("="*28)
    print("--= Enrollement's menu option =--")
    print("Enrolled Options")
    print("1) Enroll Student \n2) Drop a student from a course")
    print("="*28)
    platOption = input(">> ").strip()
    match platOption:
        case '1':
            S.enroll_student()
        case '2':
            S.drop_student()
        case _:
            print(Back.RED + Fore.WHITE +f"Please select a option")

    print("="*28)
    U.Clear()

'''
    main function to control the others and show the options, is a good escalable menu.
'''
def main():			
    U.Clear()
    options = ["Manage Students", "Manage Courses", "Manage Teacher's", "Enrollment Options", "Clear Terminal", "Exit"]
    print("Loading...")
    sleep(1)
    U.Clear()
    print("Success!!")
    sleep(1)
    U.Clear()
    while True:
        U.print_header()
        for i, option in enumerate(options,start=1): # en lugar de que inicie con el 0
            print(f"{i}) {option}")
        print("Type the option or number")
        opcion = input(">> ").capitalize().strip()
        if not isinstance(opcion,str) or not opcion.strip():
            print(Back.RED + Fore.WHITE +f"Please select a option")
        else:
            match opcion:
                case '1'|'Students':
                    Studentmenu()
                case '2'|'Courses':
                    CourseMenu()
                case '3'|'Teachers':
                    Teachermenu()
                case '4'|'Enrrolment':
                    Enrollementmenu()
                case '5'|'Clear':
                    print("Cleaning...")
                    sleep(1)
                    U.Clear()
                case '6'|'Exit':
                    U.Clear()
                    print("Exiting...")
                    sleep(1)
                    U.Clear()
                    break
                case _:
                    print(Back.RED + Fore.WHITE +f"Please select a option")
    U.Clear()
main()

