"""
Los tuples son colecciones de datos ordenados, a si mismo
son una coleccion inmutable de elementos, ademas, gracias a su
inmutabilidad, podemos utilizarla como llaves de diccionarios
"""

# Sintaxis
Mi_tuple = ()  # tuple vacio

# Puede contener diferentes tipos de datos
Mi_tuple2 = ("Luisa", 21, True, "a")

# Invertir el valor logico
if "a" not in Mi_tuple2:
	print("No esta")
else:
	print("Si esta")

# Acceder a sus elementos
print(Mi_tuple2[0])
print(Mi_tuple2[-1])

# Comprobando su inmutabilidad
try:
	Mi_tuple2[0] = "Eduardo"
except TypeError as error:
	print(f"Elemento inmutable [=> {error} <=]")
finally:
	print("FIN")

# regresa el numero de elementos de la tupla
print(len(Mi_tuple2))
# regresa el numeoro de veces que se repite un elemetno en la tupla
print(Mi_tuple2.count('a'))
# Regresa el indice de la primera coincidencia/ debemos saber de antemano el nombre exacto
print(Mi_tuple2.index("Luisa"))

"""
Es importante conocer como trabajar ocn tuplas, porque son muy versatiles y son utiles
porque al momento de regresar valores de una funcion estos estan en tuplas, es util
porque podemos trabajar con datos especificos que regresa una funcion y usar lo sque necesitamos
"""

# Podemos trabajar con desempaquetado

coordenadas = (10, 20)
x, y = coordenadas
print(x, y)

# Desempaquetar los valores restantes (se crea una lista)

tuple_numeros = (1, 2, 3, 4, 5)

a, b, *resto = tuple_numeros
print(a)
print(b)
print(resto)

# Ignorar Valores

x, _, z = (10, 20, 30)
print(x)
print(z)
# El valor 20 se ignora


# Ignorar varios elementos y al mismo tiempo tomar otros

a, _, c, *_ = (1, 2, 3, 4, 5, 6)
print(a)
print(c)
# imprime el 1, ignora el 2, y simultaneamente ignora el 4,5 y 6

# Probando con una funcion, asi podemos reutilizar los valores y usar los que queremos

def valores(nombre):
	extra = nombre.swapcase()
	minusculas = nombre.lower()
	mayusculas = nombre.upper()
	reversa = nombre[::-1]

	return minusculas, mayusculas, reversa, extra # Tuple


print("Nombre")
name = input(">> ")
(uno, dos, tres, cuatro) = valores(name)
print(uno)
print(dos)
print(tres)
print(cuatro)
