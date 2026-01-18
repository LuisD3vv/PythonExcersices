import sqlite3
from os import system as sys
from time import sleep
from pathlib import Path
from datetime import datetime
from colorama import init,Fore,Back,Cursor,Style

init(autoreset=True)

"""
    Como repaso rapido,  los getter y setter son metodos usados para controlar el acceso a los atributos de clase, asegurando la encapsulacion de la informacion y permitiendo una validacion.
"""
date = datetime.now()
formatDate = date.strftime("%d/%m/%Y")

# clases de dominio, solo leen, procesan y validan datos, cero consola

class Student:
    def __init__(self,name,lastname,accountID):
        self.name = name
        self.lastname = lastname
        self.accountID =  accountID
    # decorador que convierte un metodo en un atributo de solo lectura y nos permite usar el punto
    # instancia.objeto = tal
    @property
    def name (self):
        """getter for name"""
        return self._name
    @name.setter
    def name (self,newName):
        """setter for name validation"""
        if not isinstance(newName,str) or not newName.strip():
            raise ValueError("Name must be a non-empty string.")
        elif len(newName) < 3:
            raise ValueError("the name length must be more than 5 words")
        self._name = newName
    
    @property
    def lastname (self):
        """getter for lastname"""
        return self._lastname
    @lastname.setter
    def lastname (self,newlastname):
        """setter for lastname validation"""
        if not isinstance(newlastname,str) or not newlastname.strip():
            raise ValueError("Lastame must be a non-empty string.")
        elif len(newlastname) < 4:
            raise ValueError("the name length must be more than 5 words")
        self._lastname = newlastname

    @property
    def accountID (self):
        """getter for accountid"""
        return self._accountID
    @accountID.setter
    def accountID (self,newid):
        """setter for accountid validation"""
        if not isinstance(newid,int) or newid < 0:
            raise ValueError("The number must be no negative integer.")
        self._accountID = newid

class Course():
    def __init__(self,topic,teacher,rating,duration):
        self.topic = topic
        self.teacher = teacher
        self.rating = rating
        self.duration = duration

    @property
    def topic(self):
        return self._topic
    @topic.setter
    def topic(self,newtopic):
        if not isinstance(newtopic,str) or not newtopic.strip():
            raise ValueError("Lastame must be a non-empty string.")
        self._topic = newtopic
    @property
    def duration(self):#901269
        return self._duration
    @duration.setter
    def duration(self,newduration):
        if not isinstance(newduration,int) or newduration < 0:
            raise ValueError("The duration must be a number")
        self._duration = newduration
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self,newrating):
        if not isinstance(newrating,int) or newrating < 0 or newrating > 5:
            raise ValueError("The duration must be a number")
        self._rating = newrating
    @property
    def teacher(self):
        return self._teacher
    @teacher.setter
    def teacher(self,newteacher):
        if not isinstance(newteacher,str) or not newteacher.strip():
            raise ValueError("Lastame must be a non-empty string.")
        self._teacher = newteache

class Teacher():
    def __init__(self,name,lastname,Registration_Number):
        self.name = name
        self.lastname = lastname
        self.Registration_Number = Registration_Number
    @property
    def name (self):
        """getter for name"""
        return self._name
    @name.setter
    def name (self,newName):
        """setter for name validation"""
        if not isinstance(newName,str) or not newName.strip():
            raise ValueError("Name must be a non-empty string.")
        elif len(newName) < 3:
            raise ValueError("Name must have more than 3 words")
        self._name = newName
    @property
    def lastname (self):
        """getter for lastname"""
        return self._lastname
    @lastname.setter
    def lastname (self,newlastname):
        """setter for lastname validation"""
        if not isinstance(newlastname,str) or not newlastname.strip():
            raise ValueError("lastname must be a non-empty string.")
        elif len(newlastname) < 3:
            raise ValueError("Name must have more than 3 words")
        self._lastname = newlastname

    @property
    def Registration_Number(self):
        return self._Registration_Number
    @Registration_Number.setter
    def Registration_Number(self,newregis):
        if not isinstance(newregis,int):
            raise ValueError("The registration number must be a number")
        elif newregis < 0:
            raise ValueError("The registration number must contain at least 8 digits.")
        self._Registration_Number = newregis

"""
Clases de dominio, solo atributos y validaciones
"""