palabra = input("ingresa una palabra: ")

def es_palindromo(palabra):
    palabra = list(palabra)
    reversa = palabra[::-1]
    if palabra == reversa:
        print("es palindroma")
        return True
    else:
        print("no es palindroma")
    return False


es_palindromo(palabra)