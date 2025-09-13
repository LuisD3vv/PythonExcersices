"""
Ejemplo de uso de *args
"""

def promedio(*numeros):
	promedio = 0
	for n in numeros:
		promedio += n
	return promedio

lista = []
try:
	print("Calcular promedio (para salir presiona 's')")
	print("Numeros abajo ⬇️")
	while True:
		n = input(">> ")
		if n.lower() == "s":
			break
		lista.append(int(n))
except KeyboardInterrupt:
	print("Presionaste boton error")

fin = promedio(*lista)
print(f"Promedio => {fin} <= ")
