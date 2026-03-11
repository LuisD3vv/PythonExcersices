from os import system as sys
from colorama import init,Fore,Back,Cursor,Style
from datetime import datetime 
date = datetime.now().strftime("%d/%m/%Y")

"""
    Autor:
    Luis Alejandro Aguilar Soberanes
    
    Modulo de Funciones dee utilidad.
"""

def clear():
    '''Function made to clear console'''
    sys("clear")

def print_header():
    print(f"{Back.BLACK} {Fore.GREEN} Springvale ADMIN Management Menu {Style.RESET_ALL}\n")
    print(f"{date} {"-"*21}")

def format():
    print("-"*25)
