from functools import reduce
import collections, math

# valores = []


# while True:
#     a=int(input("Numero>> "))
#     if a == 0:
#         break
#     valores.append(a)
# print(valores)


# suma = reduce(lambda x,y: x+y,valores)
# print(f"El promedio es {suma/len(valores)}")


def tendencia_central(lista):
    valores = {
        "Media":0,
        "Varianza":0,
        "Desviacion":0
    }
    suma = reduce(lambda x,y: x+y,lista)
    mean = round(suma/len(lista),2)
    valores["Media"] = mean
    
    valores_restados_al_cuadrado = []
    
    for i in lista:
        valores_restados_al_cuadrado.append(pow(i - mean,2))
        
    varianza = sum(valores_restados_al_cuadrado) / len(lista)
    valores["Varianza"] = round(varianza,2)
    
    valores["Desviacion"] = round(math.sqrt(varianza),2)
    return valores

lista2 = []
while True:
    a=int(input("Numero: "))
    if a == 0:
        break
    lista2.append(a)
resultado2 = tendencia_central(lista2)
print(resultado2)

