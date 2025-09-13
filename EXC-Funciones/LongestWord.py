def longest_words(lista):
    mayor = lista[0]

    # Encuentras la palabra más larga
    for n in lista:
        if len(n) > len(mayor):
            mayor = n

    # Ahora recorres de nuevo para encontrar TODAS las palabras del mismo tamaño
    iguales = []
    for i in lista:
        if len(i) == len(mayor):
            iguales.append(i)

    return iguales
