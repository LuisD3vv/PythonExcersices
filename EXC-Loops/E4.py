# sumatoria condicional


n = list(range(1,100))
lista = []

for i in n:
    if i % 5 == 0 or i % 3 == 0:
        lista.append(i)
        
print("multiplos de 3 y 5")
print(lista)