from pathlib import Path

# asi para no batallar con rutas
BASE  =  Path(__file__).resolve().parent # obtener ruta
ruta = BASE / 'archivo.txt' # unir ruta con el nombre del archivo


fh = open(ruta)

letras = {}

for linea in fh:
    linea = linea.lower()
    
    for caracter in linea:
        if caracter.isalpha():
            letras[caracter] = letras.get(caracter, 0) + 1

lista = []

for letra, cantidad in letras.items():
    lista.append((cantidad, letra))

lista.sort(reverse=True)

for cantidad, letra in lista:
    print(letra, cantidad)