# Invertir n

lista = []
while True:
    n = input("Ingresa un numero: ")
    try:
        n = int(n)
        for i in range(1,n + 1):
            lista.append(i)
        break
    except ValueError:
        print("Porfavor ingresa un numero")



print(lista[::-1])

