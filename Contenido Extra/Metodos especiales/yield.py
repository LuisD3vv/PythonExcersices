# generacion peresoza

def pares_inf():
	n = 0
	while True:
		yield n
		n += 2


gen = pares_inf()

#print(next(gen))  # 0
#print(next(gen))  # 2
#print(next(gen))  # 4


# yiel solo genera un dato cuando se lo pedimos
# y no pierde secuencia,es increible


def pares_hasta(limite):
	n = 0
	while n < limite:
		if n % 2 == 0:
			yield n
		n += 1


for p in pares_hasta(20):
	print(f"Numero: {p}")


def generadorCuadrado(n):
	for i in range(1, n):
		yield i * i


for n in generadorCuadrado(20):
	print(n)


def Fibonacci(n):
	...


for f in Fibonacci(10):
	print(f)
