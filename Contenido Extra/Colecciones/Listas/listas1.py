#las listas en python son objetos mutables e iterables
# from random import randint

# lista = ['nombre', 'nombre','nombre','nombre','nombre']

# for nombre in lista:
#     while True:
#         user = input("Que palabra deseas verificar si se encuentra: ")
#     if user in nombre:
#         print("Si esta",user)
#     else:
#         print(f"No esta la letra '{user}' ")


#Comprobar si el numero aletatorio generado es el indicado por el usuario

# cpu = randint(1,10)

# vidas = 5
# while True:
#     try:
#         intento = int(input("Ingresa un numero: "))
#         if intento > cpu:
#             print("El numero secreto es menor")
#             vidas - 1
#         elif intento < cpu:
#             print("El numero secreto es mayor")
#             vidas - 1
#         if intento == cpu or vidas < 0:
#             print(f"Felicidades, lo has logrado en {vidas} intentos")
#             break
#     except:
#         print("Debes de introducir un numero")


# Metodos de las listas
frutas = ['manzana','naranja', 'pera']
verduras = ['tomate','pepino','zanahoria']

#Concatenacion
print(frutas + verduras)
# Agregar un elemento a una lista en el lugar
frutas.append('Melon') # agregar elemento al ultimo
frutas.pop(3) # eliminar un elemento aleatorio o  pasado
frutas.sort() # ordenar la lista, es diferente de sorted
frutas.reverse() # reversa
frutas.count('a') # contar la aparicion de cierto caracter
frutas.extend(verduras) # unir la lista con otra
frutas.copy() # copiar la lista
frutas.insert(1,'ano') # insertar un elemento en un indice elegido
frutas.clear() # eliminar la lista
#indexacion
print(frutas[1:2]) # podemos acceder a los elementos a partir de cierto numero


"""
Si Alguno de los valores(keys) sumados(values) 
    es igual al introducido, se regresaran los que conformaron
    la suma
"""


# Ejemplo con un nuevo iterador y un menu ejecuitable

from os import system
# CREACION DE UN CARRITO DE COMPRAS CON MATCH 
print("Bienvenido")
compras = []
while True:
  system("clear")
  print("1.-Agregar producto\n2.-Eliminar producto\n3.-Ver lista\n4.-Salir")
  opcion = int(input("Hola, que deseas hacer?: "))
  # Sintaxis de match
  match opcion:
      case 1:
       
        print("Ingresa el nombre del producto")
        try:
          nombre = input("nombre del nuevo producto: ")
        except:
          print("algo salio mal")
        else:
          compras.append(nombre)
          print(f"Se ha agreado exitosamente {nombre}")
      case 2:
        print("cual vas a eliminar")
        for producto in enumerate(compras):
          print(producto)
        try:
          nombre_eliminar = int(input("Nombre del producto que deseas eliminar: "))
        except:
          print("Porfavor, ingresa el numero.")
        else:
          compras.pop(nombre_eliminar)
      case 3:
        print("Aqui estan los productos disponibles papu")
        for producto in enumerate(compras):
          print(producto)
      case 4:
        print("chao chao perro")
        break
      case _:
        print("Ha ocurrido un pinche error")
