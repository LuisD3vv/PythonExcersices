# cadena = " Hola mundo \n"
# print(repr(cadena))
# nueva_cadena = cadena.strip(" \n")
# print(repr(nueva_cadena))
# print(nueva_cadena)

# simbolos = "***____Hola===\n"

# sin_simbolos = simbolos.strip("*_=\n")
# print(repr(sin_simbolos))
# print(sin_simbolos)

# nombre = "nombre:juan|edad:20|correo:juan@mail.com"

# nuevo = nombre.split("|")
# for line in nuevo:
#     print(line, sep= " ")


liner = "User: lissandro | Password b'$2b$12$ | Date 2025-05-21"
nombre, contrasenia, fecha = liner.split("|")
print(nombre, contrasenia, fecha)

cadenita = [" Juan\n", " Ana ", "\tPedro", ""]
