"""
Los dicciorios en python son estructuras de datos versatiles y utiles
contienen claves unicas y los valores pueden ser mutables o inmutabes
acceso por clave yu no indice
"""
usuario = {"Nombre": "Lissandro", "Edad": 21}

print(usuario["Nombre"])  # Acceso directo
print(usuario.get("Edad"))  # Acceso seguro, si no existe devuelve none

# Set default
usuario.setdefault("Nombre", "Vacio")

# acualizar elementos
usuario["Edad"] = 24
usuario["Nombre"] = "Eduardo"

# Eliminar Elementos

usuario.pop("Edad")  # Elimina y devuelve el valor de 'edad'
usuario.popitem()  # Elimina y devuelve el último par clave:valor
#  del usuario["Nombre"]  # Elimina la clave 'nombre'
#  usuario.clear()  # Vacía el diccionario

# Elementos para obtener vistas

print(usuario.keys())  # dict_keys (['Nombre','Edad']) # Claves del diccionario
print(usuario.values())  # dict_values([Lissandro,21]) # Valores del diccionario
print(usuario.items())  # dict_items(('Nombre','Lissandro')('Edad',21)) # claves y su valor del indice

# Recorrer un elemento

for clave, valor in usuario.items():
	print(clave, valor)

usuario2 = {"Apellido": "Aguilar", "Ciudad": "Mexico"}
usuario.update(usuario2)  # Se unen y sobrescriben claves repetidas
print(usuario2)

# Incializa las claves con valores que tendran todas por defecto

claves = ["clave-1", "clave-2", "clave-3"]
nuevoDict = dict.fromkeys(claves, 0)  # todos los valores tendras por defecto
#  nuevoDict = dict.fromkeys(claves(sin valor por defecto)) # Los valores seran None
print(nuevoDict)

# Copiar diccionario
copia = usuario.copy()
print(f"Copia del diccionario {copia}")