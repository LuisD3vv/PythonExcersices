def flatten(lista):
    flast_list=[]

    for item in lista:
        if isinstance(item,list):
            # recursiva
            """
            basicamente lo que hace es que al encontra  un item dentro de la lista que sea otra lista, esta sublista se agrega al final a la lista y se llama a al funcion es decir se mete a las sublistas y las desempaqueta con extends
            """
            flast_list.extend(flatten(item))
        else:
            flast_list.append(item)
    return flast_list

nested = [1,[2,3],[4,[5,6]],7]
result = flatten(nested)
print(f"original {nested}")
print(f"Flatten {result}")

# extend() "desempaca" y agrega cada ítem del iterable individualmente, haciéndolo ideal para fusionar colecciones.se usa para añadir todos los elementos de un iterable (como otra lista, tupla o cadena) al final de una lista existente, modificándola directamente (in-place) sin crear una nueva lista