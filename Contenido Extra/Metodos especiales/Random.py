from random import *

"""
Alguno de los modulos solo crean elementos al momento y no regresan nada
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista_randomint = randint(1, 10)
lista_uniform = uniform(1, 10)
luis = random()

eleccion = ['A', 'B', 'C']
eleccionsi = choice(eleccion)

#Shuffle no devuelve una lista, la moficica en el lugar y devuelve none
shuffle(lista)

# sample si regresa una coleccion nueva de elementos de k limite
print(sample(eleccion,2))


"""
Cuando una funcion termina con ed, suele significar que va a dar
la version nueva de algo, un iterable.
"""