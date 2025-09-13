#Practica de funciones con args y kwargs.

def suma_cuadrados(*args): # No conocemos los argumentos  basicamente dice (todos los argumentos)
  total = 0
  for arg in args:
      total += arg ** 2
  return total

suma_cuadrados(2,3,4,5,6,7,8,9)


def valor_absoluto(num):
    if num < 0:
        return -num  # Convierte a positivo
    else:
        return num  # Mantiene el valor como está


def suma_absolutos(*args):
    total = 0
    for num in args:
        total += valor_absoluto(num)  # Usa la función para obtener el valor absoluto
    return total

print(suma_absolutos(-6, 78, -4, 5, -89, -32, -20))


def numeros_persona(nombre, *args):
  total = 0
  for n in args:
      total += n
  return str(nombre) + " " + "la suma de tus numeros es" + " " + str(total)


numeros_persona("Luis", 1,3,4,5,6,7)

def numeros_persona(nombre, *args):
  suma_numeros = 0
  for n in args:
      suma_numeros += n
  return (f"{nombre}, la suma de tus números es {suma_numeros}")


numeros_persona("Lissandro",1,3)



#KWARGS
def prueba(num1, num2, *args ,**kwargs):

  print(f"el primer valor es {num1}")
  print(f"el segundo valor es {num2}")

  for arg in args:
    print(f"arg = {arg}")

  for clave,valor in kwargs.items():
    print(f"{clave} = {valor}")


args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}
prueba(15,50, *args, **kwargs)

