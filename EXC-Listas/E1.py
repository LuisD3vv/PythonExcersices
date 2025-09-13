# practica con lista
lista = []
print("Ingresa el texto, escribe FIN para salir abajo")
while True:
    ingreso = input()
    if ingreso == "FIN":
        break
    for letra in ingreso:
        if letra != ' ':
            lista.append(letra) # .replace(" ", "")0

print("".join(lista))



Lista = ['Luis@gmail.com', 'Eduardo@gmail.com', 'William@gmail.com']

usuarios = [user.split("@")[0] for user in Lista] # Lo partimos mediante el arroba, y agarramos el indice 0 que son los nombres

print(usuarios)