from random import *
from os import system
"""
    Las reglas ya todos las conocemos:
    
    papel gana piedra
    piedra gana tijeras
    tijera gana papel
    
    En cualquier otro caso es empate
"""
system("clear")
print("Hola crack")
nombre = input("Ingresa tu nombre: ")
system("clear")
print("====================")
print("Cuarzo Papiro Navaja")               
print("====================")
print("----------------------")
simbols = ['✊','✋','✌️'] # piedra = 0, papel = 1 y tijeras = 2, por el momento
# Poder trabjar con el valor y el indice independientemente, desempaquendo la tupla
for valor, simbolo in enumerate(simbols):
    print(valor,simbolo)
"""
Otra opcion para trabajar con la lista si trabajamos con indices que son
puros numeros
for valor in range(len((simbols)):
    print(valor)
"""

def transformar_a_letra(userEntry,cpuEntry):
    user = userEntry
    cpu = cpuEntry
    if cpu == 0:
        cpu = 'piedra'
    elif cpu == 1:
        cpu = 'papel'
    elif cpu == 2:
        cpu = 'tijeras'

    if user == 0:
        user = 'piedra'
    elif user == 1:
        user = 'papel'
    elif user == 2:
        user = 'tijeras'
    return user, cpu


def imprimir_eleccion(iuser,cepeu):
    cpu = cepeu
    user = iuser
    print(f"Variables de impresion {cpu}, {user}")
    print(f"Tu eliges: {user}: {simbols[user]}")
    print(f"Cpu elige: {cpu}: {simbols[cpu]}")


def verificar_ganador(entradaUser,entradaCPU):
    """Procesando quien gano"""
    user, cpu = transformar_a_letra(entradaUser,entradaCPU) # Porque la funcion regresa dos valores
    ganador = 'william'
    # Opciones User
    gU = [ # Comprobar si la combinacion esta adentro
        ('piedra','tijeras'),
        ('papel','piedra'),
        ('tijeras','papel')
    ]
    #gC = [(b,a) for (a,b) in gU] # inviertiendo el orden de las tuplas con list comprehesion, me sirve porque ahora se como puedo voltearlas.
    for a,b in gU:
        if user == cpu:
            return "EMPATE"
        elif user == a and cpu == b:
            ganador = "Gana Player"
            return ganador
        elif user == b and cpu == a:
            ganador = "Gana Cpu"
            return ganador
    return f"No se han podidio procesar los datos {user}-{cpu}"


#Para que esto funcione, necesitamos que las claves ya existan.
jugadas = {nombre: 0, "Cpu": 0}
while True:
    cpu = randint(0,2)
    try:
        intento = int(input(f"Hola {nombre}!, selecciona una opcion (0-2) | (-1 debug exit): "))
        system("clear")
        if intento == -1:
            for clave, valor in jugadas.items():
                print(f"\nJugador: {clave} | Puntuacion: {valor}")
            print("Hasta pronto!!")
            exit()
        elif intento > 2:
            print("Ingresa un numero dentro del rango")
            continue
    except IndexError:
            ("Has sobrepasado el indice de la lista, utiliza un numero dentro del rango")
    except ValueError:
            print("Porfavor, ingresa un numero")
    else:
        transformar_a_letra(intento,cpu)
        imprimir_eleccion(intento,cpu)
        print(verificar_ganador(intento,cpu).upper())
        resultado = verificar_ganador(intento,cpu)
        if resultado == "Gana Player":
            jugadas[nombre] += 1
        elif resultado == "Gana Cpu":
            jugadas["Cpu"] += 1
