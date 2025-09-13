#Las funcion any es una funcion que 
# nos sirve para hacer evaluaciones 
# rapidas  dentro de listas e iterables

"""
Como en este ejemplo de un verificacador de contraseñas.
"""

contra = input("Ingresa tu contraseña: ")

def es_valida(contra):
    mayusculas = any(c.isupper() for c in contra) # Alguna coincidencia dentro de un iterable
    minusculas = any(c.islower() for c in contra)
    numeros = any(c.isnumeric() for c in contra)

    if len(contra) < 8:
        return "Al menos necesitas 8 caracteres"

    if not mayusculas:
        print("❌ ingresa almenos una mayuscula")
    else:
        print("Mayuscula ✔")

    if not minusculas:
        print(" ❌ ingresa al menos una minuscula")
    else:
        print("Minuscula ✔")

    if not numeros:
        print(" ❌ Ingresa al menos un numero")
    else:
        print("Numero ✔")

    if mayusculas and minusculas and numeros:
        return "contraseña valida"
    else:
        return "contraseña invalida"

variable = es_valida(contra)
print(variable)