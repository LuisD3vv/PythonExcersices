while True:
    print("ingresa un numero 0 para salir")
    entrada = input(">> ")
    try:
        entrada = int(entrada)
    except:
        print("Ingresa un valor entero.")
    else:
        if entrada == 0:
            break
        print(f"{entrada} * 2 = {entrada * 2}")
