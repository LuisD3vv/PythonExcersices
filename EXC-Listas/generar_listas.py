ceros = [0] * 5
print(ceros)

matriz = [[1]*3 for _ in range(3)]
[print(i) for i in matriz]

# repeticion de elementos en lista (no multiplicacion)

numeros = [1,2,3,4,5]
letras = ["a","b","c","d"]
print(numeros * 2)
print(letras * 2)

# elemento real vs misma direccion

a = [1,2,3]
b = a
b.append(4) # mismo elemento

a # [1,2,3,4]
b # [1,2,3,4]

# Ambos objetos son la msima coleccion en memoria

#comprobacion

print(id(a)) # verifciar si apuntan al mismo objeto
print(id(b))

# copia real = diferente idvewr

b = a.copy()

print(id(a))
print(id(b))

# Shallow copy /  o copia superficial

a = [[1,2],[3,4]]
b = a[:]

print(id(a)) # diferentes
print(id(b))

print(id(a[0])) # pero a un nivel mas bajo son iguales
print(id(b[0]))


# para copiar mejor y mas profundo usar la libreria copy con deepcopy()

a = [1,2,3]
b = a
b.append(4)
b

# metodo 2
c = [1,2,3]
d = c[:]
d.append(4) # solo cambia d, ya no son el mismo objeto

