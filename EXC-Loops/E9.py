# Lista sin duplicados


ListaOriginal = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,1,1,1]
ListaNueva = []


# for numero in ListaOriginal:
#     if numero not in ListaNueva:
#         ListaNueva.append(numero)
#     else:
#         print(f"El numero ya estaba en la lista {numero}")
# print(ListaNueva)


# Transpuesta de una matriz

matriz=[[0,0,0],
        [0,0,0],
        [0,0,0]]

print("lissandro".center(25))
# matriz[0][0]
# matriz[0][1] 
# matriz[0][2] 
# matriz[1][0] 
# matriz[1][1] 
# matriz[1][2] 
# matriz[2][0] 
# matriz[2][1] 
# matriz[2][2] 


filas = 2
while filas >=0:
    """  es necesario declararlo dentro ya que asi es el funcionamiento
    correcto de las matrices en python es decir, el numero de columnas
    no debe  de variari nunca porque se deben de recorrer siempe als mimsas
    lo unico que debe de cambiar y reducirce fuera del loop son las
    filas que son las que debemos recorrer sin repetir reralmente"""
    columnas = 2
    while columnas >=0:
        matriz[filas][columnas] = 10
        columnas-=1
    filas -= 1
for fila in matriz:
    print(fila)
