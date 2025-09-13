def decimal_a_romano(user_input):

    numeros = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
    }
    valores = []
    
    # Cuantas veces cabe el valor en el valor del usuario
    for clave,valor in sorted(numeros.items(), key=lambda x: x[1],reverse=True):# los ordena, gracias a key,es
            #decir, toma como parametro x, que es la key, y x[1] es cada value de cada tupla de datos. y luego el true hace que de invierta de menor a mayor, a mayor a menor
        cuantoCabe = user_input // valor # este simbolo nos ayuda a saber cuantas veces cabe un numero, es decir, guarda cuanto cabe enteramente
        if cuantoCabe  > 0 : 
            valores.append(clave * cuantoCabe) # se pueden gurdar resultados de operaciones como tal
            user_input -= valor * cuantoCabe

    return "".join(valores)

while True:
    print("Operaciones Disponibles: ")
    print("1.-Decimal a Romano\n2.-Romano a decimal\n3.-Salir")
    opcion = int(input("Elegi una opcion: "))
    
    if opcion == 1:
        control = True
        while control:
            try:
                decimal = int(input("Ingresa un numero: (-1 para salir): "))
                if decimal > 3999:
                    print("porfavor ingresa un numero dentro del rango.")
                    continue # nos ayuda a poder saltar la condicion
                if decimal == -1:
                    control = False
            except:
                print("El valor no debe de ser un string")
            else:
                print(decimal_a_romano(decimal))
    elif opcion == 2:
        print("Romano a decimal, no disponible por el momento.")
    elif opcion ==3:
        print("Hasta Luego")
        break

print(decimal_a_romano((90)))
