"""
El operador walrus asigna y devuelve el valor al mismo tiempo
asi evitando rescribir el valor inecesariamente dos veces
"""

while (texto := input("Escribe\n")) != "vagina":
	print(texto)

# Ejemplo 2

nombre = "Lissandro"

if (n := len(nombre)) > 5:
	print(n)


""