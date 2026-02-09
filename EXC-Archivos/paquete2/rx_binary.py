# Leer en binario y escribir en otro archivo binario
import os


binaryInput = "EXC-Archivos/paquete2/input.bin"

binaryOutput = "EXC-Archivos/paquete2/output.bin"


def joinPath():
    """Abre y escribe en un archivo binario"""
    try:
    # rb para lectura binaria y wb para escibir en binario
        with open(binaryInput,"rb") as file1, open(binaryOutput,"wb") as file2:
            for i in file1.read():
                # Tranformacion a bytes  requierida
                file2.write(bytes(i))

    except FileNotFoundError as fl:
        print(f"El nombre de archivo es incorrecto {fl}")

joinPath()
