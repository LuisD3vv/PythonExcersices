
correos = {"a@mail.com": 10, "b@mail.com": 25, "c@mail.com": 7}

print(max(correos,key=correos.get))
print(max(correos.values()))

"""
Este es interesante, toma items() con esto obtienes clave y valor, es por eso que podemos
usar clave,valor = algo()

luego el key se convierte en una funcion anonima que comparaa por el primer valor que es el numero
en este caso

[0]correo
[1]valor
"""
clave_max, valor_max = max(correos.items(), key=lambda x: x[1])
print(clave_max, valor_max)