class Producto:
  def __init__(self, nombre, precio,categoria):
    self.nombre = nombre
    self.precio = precio
    self.categoria = categoria


prod1 = Producto("Coca Cola", 30,'Refresco')
prod2 = Producto("Marias", 21, 'Galletas')
prod3 = Producto("Vive cien", 17, 'Refresco')
prod4 = Producto("Prime", 20, 'Refresco')
prod5 = Producto("Volt", 23, 'Refresco')
prod6 = Producto("Amper", 20, 'Refresco')

lista_de_productos = [prod1,prod2,prod3,prod4,prod5,prod6]

for prod in lista_de_productos:
  if prod.categoria == 'Refresco':
    print(prod.nombre)

class Alumno:
  def __init__(self,nombre,notas):
    self.nombre = nombre
    self.notas = notas # atributo de lista
    self.diccionario = {}

  def promedio(self):
      suma = 0
      for n in self.notas:
        suma += n
      print(f"{self.diccionario[self.nombre]} = {suma}")

notitas = [10,10,9,9,9,6]
Luisito = Alumno('Luis',notitas)
Luisito.promedio()