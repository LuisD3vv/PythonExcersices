"""
    Codigo hecho por Luis Alejandro Aguilar Soberanes

    Licenciatura en Ciencia De Datos UAS

    Grupo 2-1


"""
from collections import defaultdict
from pathlib import Path

# Ejercicio 1 y 2 


# asi para no batallar con rutas
BASE  =  Path(__file__).resolve().parent # obtener ruta
ruta = BASE / 'archivo.txt' # unir ruta con el nombre del archivo



contador = defaultdict(int)
contar_correos = defaultdict(int)
try:
    with open(ruta) as file:
        for linea in file:
            if linea.startswith("From "): # El espacio hace la diferencia, de lo contrario asumiria que la palabra es From no que inicia
                recorte = linea.split()
                if len(recorte) > 2:
                    contar_correos[recorte[1]]+=1 # realizar conteo de aparicio de dias
                    contador[recorte[2]]+=1 # realizar conteo de aparicio de dias
except FileNotFoundError:
    print("No existe el archivo")

print(dict(contador))
print(dict(contar_correos))

# 3 El mayor numero de mensajes

correo,cantidad = max(contar_correos.items(),key=lambda x:x[1]) # devuelve la clave asociada al mayor valor

# en este caso numero de correos
print(f"Correo con mas mensajes: {correo} con {cantidad} mensajes.")


