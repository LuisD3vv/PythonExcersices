# Numeros primos en un rango dado por el usuario


while True:
    print("Ingresa un numero entero")
    n = input(">> ")
    try:
        n = int(n)
        print(f"Deseas conocer los pares o impares hasta {n} (1-Pares / 2-Impares)")
        opcion = int(input(">> "))
        if opcion == 1:
            print(f"Numeros pares hasta {n}")
            for i in range(1,n):
                if i %2 == 0:
                    print(i)
        else:
            print(f"Numeros impares hasta {n}")
            for i in range(1,n):
                if i %2 != 0:
                    print(i)
    except TypeError:
        print("Porfavor ingresa un numero")
    