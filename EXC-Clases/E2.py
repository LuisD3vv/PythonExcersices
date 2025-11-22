class Inventario():
    def __init__(self):
        self.objetos = []
    def agregar(self,objeto):
        self.objetos.append(objeto)
    def remover(self,objeto):
        for indice, valor in enumerate(self.objetos):
            if valor == objeto:
                self.objetos.pop(indice)
    def mostrar(self):
        [print(f"- {elemento}") for elemento in self.objetos]

class Jugador(Inventario):
    def __init__(self,nombre,vida=100):
        self.nombre = nombre
        self.vida = vida
        self.inventario = Inventario()
        
    def recibir_daño(self,cantidad):
        self.vida = self.vida - cantidad
    def curar(self,cantidad):
        self.vida = self.vida + cantidad
    def recoger(self,item):
        print(f"El siguiente elemento se agregara al inventario {item}")
        self.inventario.agregar(item)
    def vender(self,item):
        print(f"El siguiente elemento se removido del inventario {item}")
        self.inventario.remover(item)
    def mostrar_vidas(self):
        print(f"inventario del Jugador {self.nombre}, Cantidad de vida {self.vida}")
        self.inventario.mostrar()

# Crear Instancia
Luis = Jugador(nombre='Lissandro') # quitar vida
Luis.recibir_daño(90)
Luis.curar(90)
print(f"Vida de Luis antes -> {Luis.vida}")


class Enemigo():
    def __init__(self,danno):
        self.danno = danno
    def atacar(self,jugador,cantidad):
        if not isinstance(jugador,Jugador):
            print("El jugador no forma parte de la clase padre Jugador.")
        jugador.recibir_daño(cantidad)
        
enemigo = Enemigo(90)
enemigo.atacar(Luis,100)
print(f"Vida de Luis despues -> {Luis.vida}")


Luis.recoger('Espada') 
Luis.recoger('Ak47') 
Luis.recoger('Principes') 
Luis.recoger('Pepsi Kick') 
Luis.mostrar_vidas()
Luis.curar(90)
Luis.vender('Ak47')
Luis.mostrar_vidas()
