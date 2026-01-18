
'''
Basicamente es simular un carussel,
los indices negativos son para contar hasta el final.

los signos en este contexto no funcionan como operadores, aqui funcionan como una direccion

Basicamente le dicen desde que numero empezar


'''
def rotate_list(input_list,n,direction):

    # manejar cirulos (rotaciones) mas grandes que el largo de la lista
    # Muy ingenioso recupera la vuelta basicamente
    n = n % len(input_list)
    # 16 / 10 = 1, con resto de 6, entonces cuenta como turno de 6 [6:] o [:6]

    if direction.lower() == 'right':
        # concatenar listas
        return input_list[-n:] + input_list[:-n]
    else:
        return input_list[n:] + input_list[:n]
        

data  =[1,2,3,4,5,6,7,8,9,10]
print(f"Turno derecha 2: {rotate_list(data,12,'right')}") 
print(f"Turno 3 izquierda {rotate_list(data,3,'left')}") 
'''
ejemplo con texto 

lista = [1,2,3,4,5]

n=2

lista[n:]

lista[:n]

'''
print()

lista = [1,2,3,4,5]

n=2

print(lista[n:]) # 3,4,5 (Desde N hasta el final)

print(lista[:n]) ,1,2 #(hasta el inicio hasta N (sin incluirla))


print(lista[-n:]) # 4,5 (dos numero negativos hacia la izquierda, es decir corta a la izquierda dos elementos)

print(lista[:-n]) # corta dos elementos al final (hasta N)
