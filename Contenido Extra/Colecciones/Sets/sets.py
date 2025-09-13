"""
Es una coleccion no ordenada de elementos unicos (sin duplicados)

Es mutable, se pueden agregar o quitar elementos pero no repetidos


"""


#  Sintaxis basica de un set
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set)

# No usar llaves vacias para crear sets, se creara un diccionario vacio {}

empty_set = set()

# Metodos Comunes de sets

print(my_set.add(10))
print(my_set.remove(7))
print(my_set.discard(1))
print(my_set.pop())
print(my_set.clear())

# Operarciones a modo de conjuntos matematicos

set1 = {2, 4, 6, 8, 10}
set2 = {1, 3, 5, 7, 9}
# Union
print(set1.union(set2))
# Interseccion
print(set1.intersection(set2))
# Diferencia
print(set1.difference(set2))
# Diferencia simetrica
print(set1.symmetric_difference(set2))


# Ejemplos rapidos de operaciones con conjuntos
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)
