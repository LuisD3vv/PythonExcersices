#Funciones anonimas, se declaran asi
lista = [1,2,3,4,5,6,7,8,9,0]

luis = map(lambda n: n % 2== 0, lista)

#utilizandolo junto a la funcion map, y lambda requiere parametro, y condicion
# ya el iterable es de map
print(list(luis))

# Lambda es una funcion anonima (sin nombre) que se escribe en una sola linea y sirve para operaciones rapidas y simples


#lambda argumentos: expresion

# Lambda simplemente significa que la funcion sera anonima
f = lambda x: x + 2
print(f(3))

# esta funcion es igual a
def f(x):
    return x + 2
