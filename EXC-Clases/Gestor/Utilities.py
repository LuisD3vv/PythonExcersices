from os import system as sys
from colorama import init,Fore,Back,Cursor,Style

def format():
    return "*"*25

def Clear():
    '''Function made to clear console'''
    sys("clear")

def print_header():
    print(Back.BLACK + Fore.GREEN + "Springvale ADMIN Management Menu")
    print("-"*32)

def print_format():
    return ""


