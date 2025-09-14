# Dibujar un triangulo segun el numero del usuario


while True:
    n = input("Ingresa un numero: ")
    try:
        n = int(n)
        for i in range(0,n):
            print(i*'*')
        for l in range(n,0,-1):
            print(l*'*')
    except TypeError:
        print("Porfavor ingresa un numero")
        