import os

ruta = ""
def write(fileName):
#    os.(fileName,exist_ok=True)si el directorio falla
    try:
        print("escribe el contenido debajo")
        with open(fileName,'w') as file:
            contenido = []
            while True:
                line = input(" ")
                if line.upper() == "FIN":
                    break
                contenido.append("".join(line)+"\n")
            file.writelines(contenido)
    except FileNotFoundError:
        print(f"Archivo no encontrado {filename}")

write("EXC-Archivos/output.txt")


