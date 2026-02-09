# import re

# # este cuenta el largo del archivo completo, read() regresa un solo string gigante
def countWords(fileName):
    suma = 0
    try:
        with open(fileName) as file:
            contenido = file.read().lower()
            for linea in contenido.split():
                suma+=1
    except FileNotFoundError:
        print(f"Error, archivo {fileName} no encontrado")
    return suma

print(f"Cantidad de palabras: {countWords("EXC-Archivos/sample.txt")}")



# \w NO cuenta acentos. y aparte read() carga todo el archivo en memoria

# def countWords2(file):
#     try:
#         with open(file) as file:
#             content = file.read().lower()
#             words = re.findall(r'\b\w+\b', content)
#             return len(words)
#     except FileNotFoundError:
#         print("Error, archivo no encontrado")
#     return suma

# conteo2 = countWords2("EXC-Archivos/sample.txt")
# print(conteo2)

def countSpecificWord(inputText) -> int:
    apariciones = 0
    try:
        with open("EXC-Archivos/sample.txt") as file:
            contenido = file.read().lower()
            separado = contenido.split()
            for indice, linea in enumerate(separado):
                if inputText == linea:
                    print(f"Ubicacion Linea {indice} coincidencia --> {linea}")
                    apariciones +=1
    except FileNotFoundError:
        print("Error, archivo no encontrado")
    return apariciones


print(f"Total de apariciones: {countSpecificWord(input("Ingresa un texto: "))}")
