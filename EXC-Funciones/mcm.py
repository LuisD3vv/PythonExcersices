# esta bien, debemos de mejorar la parte de los nuimeros fraccionarios
from math import  ceil
from functools import reduce
def mcm(a,b):
    "Utilizando Factores Primos"
    print(f"Numeros Introducidos {a} {b}")
    # generar un lista de primos
    
    factores_primos = []
    for n in range(2, 100):
        es_primo = True
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            es_primo = False
            break
    if es_primo:
        factores_primos.append(n)# incluirse el mismo como caso de primo relativo, es decir que su unico factor sea el mismo o la unidad
    multiplo = []
    i = 0
    while a != 1 or b != 1:
        # simpre utilizar este para evitar el index error con un while
        if i >= len(factores_primos):
            if a != 1:
                multiplo.append(a)
                a = 1
            if b != 1:
                multiplo.append(b)
                b = 1
            break
        
        moduloA = a % factores_primos[i]
        moduloB = b % factores_primos[i]
        
        
        print(f"Modulos actuales a: {moduloA}")
        print(f"Modulos actuales b: {moduloB}")
        
        
        if moduloA == 0 and moduloB == 0:
            multiplo.append(factores_primos[i])
            # Guardar valores enteros
            a //= factores_primos[i]
            b //= factores_primos[i]
            # no incrementamos para seguir usando el mismo factor
        else:
            i+=1
        
    print(f"Valores final de a {a}")
    print(f"Valores final de b {b}")
    print(f"Multiplos guardados {multiplo}")
    # forma correcta de utilizar reduce y lambda para reducir la multiplicacion a un solo valor
    multiploFinal = reduce(lambda y,x: y*x,multiplo)
    print(f"El multiplo es {multiploFinal}")
# print("Ingresa los numeros que deseas conocer su MCM (numeros del 1 al 100)"
n = int(input("Ingresa A: "))
n1 = int(input("Ingresa B: "))
mcm(n,n1)

"""_summary_
    Iterar facilmente sobre el siguiente elemento
    de esta manera zip crea parejas y se detiene hasta que una de las dos se quede solo.
    
        for actual, siguiente in zip(lista, lista[1:]):
    print(actual, siguiente)
    
    con enumerate
    
    for indice, elemento in enumerate(lista):
        print(elemento,i)
    
    la correcta seria con indice incluido con el rango
    
    for i in range(len(lista)):
        print(lista[i])
"""