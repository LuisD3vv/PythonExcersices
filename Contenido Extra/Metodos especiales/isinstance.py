class Galleta:
    def __init__(self, sabor):
        self.sabor = sabor

choco = Galleta("chocolate")

print(isinstance(choco, Galleta))  # ✅ True, es una instancia de Galleta

#choco es de tipo galletam aunque no sea oficial de python



#Ejemplo con verificar que un dato sea de tipo string

edad = 0

dato = int(input("ingresa tu edad: "))

# no tiene sentido comprobar si un input es str ya que por defecto lo es
try:
    numero = int(dato)
    if isinstance(numero,int):
        print("Correcto")
except ValueError:
    print("Eso no es un numero webon")

