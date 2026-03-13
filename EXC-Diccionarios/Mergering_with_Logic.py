# |   → crear mezcla nueva
# |=  → mezclar dentro del mismo




def merge_dicts(d1, d2):
    # Start with a copy of d1 to avoid modifying the original
    result = d1.copy() # all the origin content
    
    for key, value in d2.items():
        # .get(key, 0) returns 0 if the key doesn't exist yet
        result[key] = result.get(key, 0) + value
        # .get es una forma mas segura de acceder a los elementos de un diccionario
    
    return result

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

merged = merge_dicts(dict_a, dict_b)
print(f"Merged Dictionary: {merged}")


# si ambos metodos no son guardados en una variable, su contenido se perdera.

# unir dos diccionarios

x = {"valor1":"culo"}
y = {"valor2":"vagina"}

z = x | y # operador de fusion  (pipeline), crea un nuevo objeto
# tambien  se puede encadenar z
# 
# xxx = x | y | a, con orden de operandos y como son organizados

# si una clave de a se repite, gana la de b, se crea un nuevo diccionario

print(z)

"""
    El operador ** desempaqueta pares clave-valor, ideal para argumentos de funciones.
    El operador * desempaqueta solo las claves.
    En la fusión, si hay claves duplicadas, la del último diccionario tiene prioridad
"""

# Metodo de fusion heredado

z = {**x,**y} 

a= {"valor3":"tetas"}

# si modifica el diccionario original
z |= a # operador de actualizacion nuevo, nos ayuda a prevenir el mal uso y obtener un SyntaxError y manejar ciertos errrores.

print(z)


# Desempaquetado de diccionario

datos = {'nombre':'Luis',"edad":21}
# el argumento debe de tener le mismo nombre de la clave para que funcione el desempaquetado
def saludar(nombre,edad):
    print(f"Hola {nombre} tienes {edad} de edad.")
saludar(**datos) # desempaquetar el diccionario al enviarlo como argumento


# Desempaquetar solo valores con un solo asterisco.

solo_valores = [*datos] # -> [Luis, 21]
print(solo_valores)