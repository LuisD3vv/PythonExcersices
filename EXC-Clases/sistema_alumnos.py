class Alumno:
    def __init__(self,nombre):
        self.nombre = nombre
        self.calificaciones = []
    def promedio(self):
        promedio = 0
        for i in self.calificaciones:
            promedio+=i
        print(promedio)
    
class Curso:
    def __init__(self,nombre_curso):
        self.nombre_curso = nombre_curso
        self.lista_alumnos = []
    def agregar_alumnos(self,nombre):
        self.lista_alumnos.append(nombre)
    def mostrar_promedio(self,nombre):
        pass

calif= [8,7,8,7,9,9]
Lissandrito = Alumno('Luis')
Lissandrito.calificaciones(calif)
lista_alumnos = []
cursos = Curso('Matematicas')