
"""
    Como repaso rapido,  los getter y setter son metodos usados para controlar el acceso a los atributos de clase, asegurando la encapsulacion de la informacion y permitiendo una validacion.
"""

# clases de dominio, solo leen, procesan y validan datos, cero consola

class Estudiante:
	"""Clase estudiante"""
	def __init__(self, nombre, apellido, numero_de_cuenta,correo='sin@correo.com'):
		self.nombre = nombre
		self.apellido = apellido
		self.numero_de_cuenta = numero_de_cuenta
		self.correo = correo

	# decorador que convierte un metodo en un atributo de solo lectura y nos permite usar el punto
	# instancia.objeto = tal
	@property
	def nombre(self):
		"""getter for nombre"""
		return self._nombre

	@nombre.setter
	def nombre(self, nuevo_nombre):
		"""setter for nombre validation"""
		if not isinstance(nuevo_nombre, str) or not nuevo_nombre.strip():
			raise ValueError("nombre must be a non-empty string.")
		elif len(nuevo_nombre) < 3:
			raise ValueError("the nombre length must be more than 5 words")
		self._nombre = nuevo_nombre

	@property
	def apellido(self):
		"""getter for apellido"""
		return self._apellido

	@apellido.setter
	def apellido(self, nuevo_apellido):
		"""setter for apellido validation"""
		if not isinstance(nuevo_apellido, str) or not nuevo_apellido.strip():
			raise ValueError("Lastame must be a non-empty string.")
		elif len(nuevo_apellido) < 4:
			raise ValueError("the name length must be more than 5 words")
		self._apellido = nuevo_apellido

	@property
	def numero_de_cuenta(self):
		"""getter for numero_de_cuenta"""
		return self._numero_de_cuenta

	@numero_de_cuenta.setter
	def numero_de_cuenta(self, nuevo_id):
		"""setter for numero_de_cuenta validation"""
		if not isinstance(nuevo_id, int) or nuevo_id < 0:
			raise ValueError("The number must be no negative integer.")
		self._numero_de_cuenta = nuevo_id

	@property
	def correo(self):
		"""getter for accountid"""
		return self._correo

	@correo.setter
	def correo(self, nuevo_correo):
		"""setter for accountid validation"""
		if not isinstance(nuevo_correo, str)or not nuevo_correo.strip():
			raise ValueError("The number must be no negative integer.")
		self._correo = nuevo_correo


class Curso:
	"""Clase Courso"""
	def __init__(self, topic, teacher, rating, duration):
		self.topic = topic
		self.teacher = teacher
		self.rating = rating
		self.duration = duration

	@property
	def topic(self):
		return self._topic

	@topic.setter
	def topic(self, newtopic):
		if not isinstance(newtopic, str):
			raise ValueError("Lastname must be string.")
		self._topic = newtopic

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, newduration):
		if not isinstance(newduration, int) or newduration < 0:
			raise ValueError("The duration must be a number")
		self._duration = newduration

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, newrating):
		if not isinstance(newrating, int) or newrating < 0 or newrating > 5:
			raise ValueError("The duration must be a number")
		self._rating = newrating

	@property
	def teacher(self):
		return self._teacher

	@teacher.setter
	def teacher(self, newteacher):
		if not isinstance(newteacher, str):
			raise ValueError("Lastname must be string")
		self._teacher = newteacher


class Maestro:
	"""Clase Maestro"""
	def __init__(self, name, lastname, Registration_Number):
		self.name = name
		self.lastname = lastname
		self.Registration_Number = Registration_Number

	@property
	def name(self):
		"""getter for name"""
		return self._name

	@name.setter
	def name(self, newName):
		"""setter for name validation"""
		if not isinstance(newName, str) or not newName.strip():
			raise ValueError("Name must be a non-empty string.")
		elif len(newName) < 3:
			raise ValueError("Name must have more than 3 words")
		self._name = newName

	@property
	def lastname(self):
		"""getter for lastname"""
		return self._lastname

	@lastname.setter
	def lastname(self, newlastname):
		"""setter for lastname validation"""
		if not isinstance(newlastname, str) or not newlastname.strip():
			raise ValueError("Lastname must be a non-empty string.")
		elif len(newlastname) < 3:
			raise ValueError("Name must have more words")
		self._lastname = newlastname

	@property
	def Registration_Number(self):
		return self._Registration_Number

	@Registration_Number.setter
	def Registration_Number(self, newregis):
		if not isinstance(newregis, int):
			raise ValueError("The registration number must be a number")
		elif newregis < 0:
			raise ValueError("The registration number must contain at least 8 digits.")
		self._Registration_Number = newregis
