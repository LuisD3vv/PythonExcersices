from functools import reduce

"""
Esta funcion necesita ser importada a la verga jaja

"""
# result = reduce(function, iterable[initializer])


def suma(a,b):
    return a + b


print("Suma total:")
print(reduce(suma,[1,2,3,4,5,6,7,8,9]))


