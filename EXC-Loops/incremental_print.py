
def given_number(n):
	return sum(range(0, n + 1))


print(given_number(10))


def multiplication(n):
	for i in range(1, 11):
		print(n * i)


print(multiplication(2))


def display_numbers(lista):
	for i in lista:
		if i % 5 == 0:
			print(i)
		elif i > 150:
			continue
		elif i > 500:
			break


lista = [12, 75, 150, 180, 145, 525, 50]
print(display_numbers(lista))


def done():
	for i in range(5):
		print(i)


done()
print("Done!")


# para usar slices con listas es buena idea usar range(LEN())
def indexPosition(a):
	for i in range(len(a)):
		if i % 2 != 0:
			print(a[i])


mi_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
indexPosition(mi_lista)


def cube(n):
	for i in range(1, n):
		print(f"Current Number is: {i} and cube is {pow(i, 3)}")


print(cube(10))


for n in range(6):
	print(n*"*")

for n in range(4, 0, -1):
	print(n * "*")