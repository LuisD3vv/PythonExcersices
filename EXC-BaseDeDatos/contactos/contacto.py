import re
class Contacto:
    def __init__(self,nombre,apellido,correo,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono  = telefono

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        '''
        si no es string o si despues de limpiarlo no tiene contenido
        '''
        if not isinstance(nuevo_nombre,str):
            raise TypeError("Class: El argumento debe ser una cadena")
        if not nuevo_nombre.strip():
            raise ValueError("Class: El argumento no debe estar vacio")
        self._nombre = nuevo_nombre.strip()

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,nuevo_apellido):
        if not isinstance(nuevo_apellido,str):
            raise TypeError("Class: El argumento debe ser una cadena")
        if not nuevo_apellido.strip():
            '''
            tipo correcto contenido incorrecto
            un ejemplo es esperar un string pero
            no un string vacio
            '''
            raise ValueError("Class: El argumento no debe estar vacio")
        self._apellido = nuevo_apellido.strip()

    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self,nuevo_correo):
        patron = re.compile(r'(\w+)((\.\w+)*)@(\w+)((\.\w+)+)') # SEPARADO POR GRUPOSJIKM
        if not re.search(patron,nuevo_correo):
            # raise necesita un objeto que sea una exepcion pero raise solo devuelve un string 
            raise re.error("Class: Formato correo incorrecto")
        self._correo = nuevo_correo

    @property
    def telefono(self):
        return self._telefono 
    
    @telefono.setter
    def telefono(self,nuevo_telefono):
        patron = r"^\d{10}$"
        if not re.search(patron,nuevo_telefono):
            raise re.error("Class: Formato telefono incorrecto")
        self._telefono = nuevo_telefono
