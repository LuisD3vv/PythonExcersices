def numero_romano(user_input):

  numeros = {
      'M': 1000,
      'CM': 900,
      'D': 500,
      'CD': 400,
      'C': 100,
      'XC': 90,
      'L': 50,
      'XL': 40,
      'X': 10,
      'IX': 9,
      'V': 5,
      'IV': 4,
      'I': 1
  }

  valores = []
  # Cuantas veces cabe el valor en el valor del usuario
  for clave,valor in sorted(numeros.items(), key=lambda x: x[1],reverse=True):
    cuantoCabe = user_input // valor # este simbolo nos ayuda a saber cuantas veces cabe un numero
    if cuantoCabe  > 0 :
      valores.append(clave * cuantoCabe) # se pueden guyarda
      user_input -= valor * cuantoCabe

  return "".join(valores)

  # return valores

  #   valores.append(clave)
  #   resto = operacion % valor
  #   operacion = resto
while True:
  try:
    romano = int(input("Ingresa un numero: "))
    if romano > 3999 or romano < 1:
        print("porfavor ingresa un numero dentro del rango.")
        continue
  except:
      print("Porfavor agrega un numero.")
  else:
    print(numero_romano(romano))

