"""

Formas de acceder a un diccionario

con .get("clave") -> valor -> se puede manejar un default
con dic[clave] -> valor (solo si estas seguro de que existe)

"""

producto = {"nombre":"Laptop","precio":7000}

# Devolver un valor por defecto

print(producto["nombre"])
print(producto.get("marca","sin marca"))

# Agregar

producto["marca"] = "dell"

# Eliminar una clave

del producto["precio"]

# eliminarla y obteneer el valor de la clave eliminada

nombre = producto.pop("nombre")
print(nombre)


print(producto)


# Metodos utiles de los diccionarios

alumnos = [
    {"nombre":"Luis","edad":21},
    {"nombre":"Eduardo","edad":24},
    {"nombre":"William","edad":21},
    {"nombre":"Diego","edad":20},
    {"nombre":"Juan","edad":34},
]

alumnos[0].keys()
# -> ["nombre","edad"]

alumnos[0].values()
# -> ["luis","21"]

for alumno in alumnos:
    for nombre,edad in alumno.items():
        print(nombre,edad)
# -> [(nombre,edad),(nombre,edad),(nombre,edad)] # pares clave valor en tuplas por registro
# (),

# actualizar valores existentes y agregar nuevos usando keyword arguments

alumnos[0].update(peso=95)

# verificar key en diccionario


# Diccionarios anidados
# Datos de un pedido (típico de una API)
pedido = {
    "id": 1234,
    "cliente": {
        "nombre": "María García",
        "email": "maria@email.com"
    },
    "productos": [
        {"nombre": "Laptop", "precio": 850},
        {"nombre": "Mouse", "precio": 25}
    ],
    "total": 875
}

# Acceder a datos anidados
print(pedido["cliente"]["nombre"])  # → María García
print(pedido["productos"][0]["nombre"])  # → Laptop

# Forma segura (por si falta alguna clave)
email = pedido.get("cliente", {}).get("email", "No disponible")