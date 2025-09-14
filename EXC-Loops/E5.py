# Tabla de multiplicar avanzada
while True:
    n = input("Ingresa un numero: ")
    try:
        n = int(n)
        for i in range(1,13):
            print(f"{n} x {i} = {n *i}")
    except TypeError:
        print("Porfavor ingresa un numero")
        