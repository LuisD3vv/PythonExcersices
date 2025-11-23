
divisas = {
    'Euro':'€',
    'Peso':'$',
    'Yen':'¥'
    }

usuario = input("Ingresa una divisa: ").capitalize()
esta = False
for clave, valor in divisas.items():
    if usuario == clave:
        esta = True
        break
    
if esta:
    print(f"Si se ecuentra en el diccionario la divisa {divisas[usuario]}")
else:
    print("No se euentra la divisa")

# forma de IA mas pythonica

entrada2 = input("Ingresa una divisa: ").capitalize()

if entrada2 in divisas:
    print(f"Sí se encuentra la divisa. Símbolo: {divisas[entrada2]}")
else:
    print("No se encuentra la divisa en el diccionario")
