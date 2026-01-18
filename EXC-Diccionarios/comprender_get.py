# Ejercicio 1

scores = {'ana':10,'luis':9}

print(scores.get('ana',0)) #10 - si existe, entonces regresa su valor
print(scores.get('pedro',0)) # 0 - no existe, regresa 0 o none

# Suposicion de que devuelve antes de ejecutarlo


# Ejercicio 2


# si name ya existe, sumar los puntos, si no, desde 0
def add_scores(scores,name,points):
    scores[name] = scores.get(name,0) + points

scores = {'ana':10}
add_scores(scores, 'ana', 5)
add_scores(scores, 'pedro', 3)

# Ejercicio 3

def apariciones(numbers):
    conteo = {}
    for x in numbers:
        conteo[x] = conteo.get(x,0) + 1
        # valor = [incremento en caso de ser la misma clave o en este caso numero]
    return conteo

numbers = [1,12,3,3,4,4,5,5,5,5,9]
apariciones(numbers)


def conteo_palabra(words):
    conteo = {}
    for x in words:
        conteo[x] = conteo.get(x,0) + 1
        # valor = [incremento en caso de ser la misma clave o en este caso numero]
    return conteo


words = ['python', 'java', 'python', 'go', 'python', 'go']
conteo_palabra(words)



# Ejercicio 4 Fusion de diccionarios

def merge_dicts_sum(da,db):
    copia = da.copy() # necesario para el control de flujo
    for clave,valor in db.items():
        copia[clave] = copia.get(clave,0) + valor
    return copia

# Ejercicio 4 pero sin copy

def merge_dicts_sum_without_copy(da,db):
    # aqui no existe a, por lo cual solo va a imprimr el b
    copia = {}
    for clave,valor in db.items():
        copia[clave] = copia.get(clave,0) + valor
    return copia


dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}
print(merge_dicts_sum(dict_a,dict_b))

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}
print(merge_dicts_sum_without_copy(dict_a,dict_b))


# solucion de IA

def merged(da, db):
    copia = {}
    for d in (da, db):
        for clave, valor in d.items():
            copia[clave] = copia.get(clave, 0) + valor
    return copia
