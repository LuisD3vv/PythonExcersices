import os
from datetime import datetime

os.system("clear")
fechabruta = datetime.today()
fecha = fechabruta.strftime('%d-%m-%Y')

frutas = {
    "Platano":6,
    "Manzana":12,
    "Pera":3.4,
    "Naranja":19
}
print("Nombre: ")
nombre = input(">> ")
while True:
    print(f"Bienvenido {nombre} Que haras hoy\n1) Comprar frutas\n2) Nada")
    opcion = input(">> ")
    match opcion:
        case "1":
            esta = False
            print("----------------")
            print("Precio Producto")
            for fruta, precio in frutas.items():
                # utilizando ancho fijo alineacion gracias a f-string
                print(f"${precio:<5} {fruta}")
            print("----------------")
            print("Que fruta deseas llevar?")
            eleccionFruta = input(">> ").capitalize()
            for  clave, valor  in frutas.items():
                if eleccionFruta == clave:
                    esta = True
                    break
            if esta:
                print("Cuantos kilos compraras")
                nkilos = int(input(">> "))
                total = frutas[eleccionFruta] * nkilos
            else:
                os.system("clear")
                print(f"{eleccionFruta} no se encuentra disponible.")
                continue
            print("---------------------")
            print(f"| Cliente: {nombre}\t|")
            print(f"| Producto(s) precio c/u cantidad\t|")
            print(f"| {eleccionFruta}\t\t{frutas[eleccionFruta]}\t{nkilos}")
            print(f"|\n| Total ${total}\t|")
            print()
            print(f"| {fecha}|")
            print("---------------------")
            break
        case "2":
            print("hasta pronto")
            break

    