# Aqui estudiaremos todos los metodos de lso string

print("Nombre ")
Palabra = input(">> ")

print(Palabra[::-1])
print(f" {Palabra}")

for i in Palabra:
    print(i, sep="-", end=" ")

print("\n")
print(Palabra.upper())
print(Palabra.lower())
print(Palabra.title())
print(Palabra.swapcase()) # invertir minusculas por mayusculas
print(Palabra.capitalize())
print(Palabra.count("o"))
print(Palabra.find("o"))
print(Palabra.replace("o", "a"))
print(Palabra.split(" "))
print(Palabra.ljust(10, "x"))
print(Palabra.rjust(10, "0"))


# Si la palabra es mayuscula se convierte en minuscula
for i in Palabra:
    if i.isupper():
        i = i.lower()
        print(i, end=" ")

# No puede recibir multiples valores, pero si una tupla de strings
if Palabra.startswith(('a', 'e ', 'i', 'o', 'u')):
    print("si")
else:
    print("no")


if Palabra.endswith(('a', 'e ', 'i', 'o', 'u')):
    print("si")
else:
    print("no")