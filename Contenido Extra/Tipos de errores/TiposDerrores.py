#Manejo de errores (Excepciones)

#  tipos de errores de excepciones
try:
    user = input("Numero")
except ValueError:
    print("error")
except TypeError:
    print("error")
except IndexError:
    print("error")
except KeyError:
    print("error")
except FileExistsError:
    print("error")
except FileNotFoundError:
    print("error")
except FloatingPointError:
    print("error")
except KeyboardInterrupt:
    print("error")
except FileExistsError:
    print("error")
except ZeroDivisionError:
    print("error")
except ModuleNotFoundError:
    print("error")
except AttributeError:
    print("error")
except IsADirectoryError:
    print("error")
else:
    print("si")

