def perfil_usuario(nombre, *args, **kwargs):
  print(f"Nombre: {nombre}")
  print("Pasatiempos:")
  for arg in args:
    print(f"-{arg}")

  print("Datos personales:")
  for clave,valor in kwargs.items():
    print(f"{clave}: {valor}")

perfil_usuario('Lissandro','Estudiar', 'Programar', 'VideoJuegos', Edad=21, Ciudad='Culiacan') # solo acepta strings
