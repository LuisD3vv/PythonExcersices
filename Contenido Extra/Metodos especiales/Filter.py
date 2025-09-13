"""
La función incorporada filter()
permite filtrar elementos de una 
lista o de cualquier objeto iterable.
Como primer argumento se le debe indicar una función f(i)
que tome como argumento un objeto 
y retorne un valor booleano (True o False); 
"""


def es_par(n):
    return n % 2 == 0


resultado = list(filter(es_par,range(1,51)))
print(resultado)
