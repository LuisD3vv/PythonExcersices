import os
from pathlib import Path

def ckeck(filename:str) -> bool:
    """
    verifica la existencia de un archivo pasado como parametro
    """
    base = Path(__file__).resolve().parent / filename
    return base.exists()


# Directorio  actual de trabajo != donde se ejecuta y busca python.
print(os.getcwd())


name = input("Ingresa el nombre del archivo: ")
if name != "":
    print(ckeck(name))
else:
    print("Ingresa algo monigote")


