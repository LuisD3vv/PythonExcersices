# Lista plana

# con una lista como esta  

lista = [[1, 2], [3, 4, 5], [6]]

lista2 = []

for i in lista:
    for j in i:
        lista2.append(j)

print("Lista limpia")
print(lista2)

# Palindromos en una lista

palabras = ["oso", "python", "radar", "casa", "reconocer"]

for i in palabras:
    palindormo = i[::-1]
    if i == palindormo:
        print(f"es palindromo {i}")
    else:
        print(f"no es palindromo {i}")
