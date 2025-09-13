
# El factorial se define como un numero no negativo, producto de todos los numeros positivos menos o igual a n.
def factorial(n): #Caso base = 0, es lo que limita la recursividad
  if (n == 0):  # El numero va en cuenta regresiva hasta que llega a 0, aqui
    return 1  # Es donde la base regresa 1 y empieza la multiplicacion
  return n * factorial(n -1)


print(f"El factorial de tu numero es {factorial(10)}")
