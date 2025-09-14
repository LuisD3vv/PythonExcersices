#  Recibir una cadena y contar vocales

conteo = 0
vocales = []
try:
    n = input("Ingresa la palabra: ")
    for letra in n.lower():
        if letra in ('a','e','i','o','u'):
            vocales.append(letra)
            conteo += 1
except ValueError:
    print("Porfavor, ingresa un string")
    
print(f"Cantidad de vocales en tu palabra: {conteo}\nSon las siguientes {" ".join(vocales)}")

