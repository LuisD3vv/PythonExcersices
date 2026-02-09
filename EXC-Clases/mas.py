class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return f"Vehicle Name: {self.name} Speed: {self.max_speed}km/h Mileage: {self.mileage} km"
    def seating_capacity(self,capacity):    
        return f"The seating capacity of a {self.name} is {capacity} passangers"



class Bus(Vehicle):
    def seating_capacity(self,capacity=50):    
        return super().seating_capacity(capacity) # super nos permite llamar a los metodos del padre como si fueramos una instancia de el., utiliza el mimso self y mantiene la herencia correctamente


# hereda todo de Vehicle, incluso sin haberle declarado codigo
SchoolBus = Bus("Volvo",180,12)
print(SchoolBus.seating_capacity())
print(Bus.__mro__)

# super no apunta al padre direcro, solo al siguiente en el orden de resolucion (MRO)
print(isinstance(SchoolBus,Vehicle))