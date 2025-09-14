#Adivina el pinche numero

from random import randint

cpu = randint(1,50)
intentos = 10

while True:
    n = input(f"No.Intentos {intentos} Ingresa un numero: ")
    try:
        n = int(n)
        if n > 999:
            print("te pasaste del rango a la verga")
        if n > cpu:
            print("el numero es mas pequeno")
            intentos -=1
        else:
            print("el numero es mas grande")
            intentos -=1
        if n == cpu:
            print(f"adivinaste el numero en {intentos} intentos.")
            break
        if intentos == 0:
            print("te quedaste sin intentos")
            break
    except ValueError:
        print("Porfavor ingresa un numero")
