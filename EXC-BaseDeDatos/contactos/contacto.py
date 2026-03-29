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
        if isinstance(nuevo_nombre,str):
            raise ("El nombre debe ser una cadena")
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,nuevo_apellido):
        if isinstance(nuevo_apellido,str):
            raise ("El apellido debe ser una cadena")
        self._apellido = nuevo_apellido

    @property
    def correo(self):
        return self._correo
    
    @correo.setter
    def correo(self,nuevo_correo):
        import re
        patron = r''
        pass

    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self,nuevo_telefono):
        pass
