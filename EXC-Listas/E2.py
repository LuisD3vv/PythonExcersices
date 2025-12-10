# solicitar al usuario una palabra y contar las putas vocales

from collections import defaultdict
from math import sqrt

user = input("Ingresa la palabra: ")
conteo = defaultdict(int)
for i in list(user):
    if i in ('a','e','i','o','u'):
        conteo[i]+=1
print(conteo)


# Calcular el prodcuto de dos matrices


a = [
    [1,2,3],
    [4,5,6]
]
b = [
    [-1,0],
    [0,1],
    [1,1]
]
# tamano de la matriz resultante, que al multiplicar se crea otra matriz
c = [
    [0,0],
    [0,0]
]
# las filas de a deben ser iguales a las columna de b
for i in range(len(a)):
    for j in range(len(b[0])):
        # el tamano de la nueva matriz
        for k in range(len(b)):
            c[i][j]+= a[i][k] * b[k][j]

print("matriz resultante")
for fila in c:
    print(fila)

# Dar media y desviacion atipica

numeros = []
entrada = input("Ingresa una muestra de numeros: ")
for n in entrada.split(','):
    numeros.append(int(n))

promedio = sum(numeros) / len(numeros)
suma_cuadrados = 0
for i in numeros:
    suma_cuadrados += pow(i-promedio,2)
print("La media de la muestra es {}".format(promedio))
print("La desviacion de la muestra es {}".format(sqrt(round(suma_cuadrados/len(numeros)-1,2))))
