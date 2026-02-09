'''
crear un loop que vaya del 1 al 10
multiplique n por esos numeros y al llegar a 10
se reinicie y ahora x sea = x+1
'''
i=1
x = 10
while i<10:
    print()
    print(f"Multiplication table of: {i}")
    # Loop interno que maneja a i, es decir el numero que aumenta
    for x in range(1,11):
        print(f"{i*x} ",end= "")
        # Aqui reiniciamos x, para poder multiplicar todos los numeros por x
        if x == 10:
            i+=1 # Aumentamos i cuando x ya es igual a 10
            break # terminamos el bucle interno
