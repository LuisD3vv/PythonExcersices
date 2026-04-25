
# Uso del modulo re en este proyecto

> Uso importante para poder asegurarnos de que el formato correcto entrara a la base de datos

```python
explicacion de el formato (los espacios se toman literalmente)

\w+(\.\w+)* 

cada .algo es un grupo y el * sigifica que puede aparecer de 0 a muchas veces porque puede o no tener un punto en el username

luis.aguilar.soberanes24

# @ identificador del correo, debe al menos haber uno ahuevo es decir

al menos debe tener un (algo)@(algo.com)

\w+(\.\w+)+
.com .gov .edu .mx

ejemplo real -> @info.uas.edu.mx
```

## Los try except

>Solo aceptan objetos como exepciones, necesitamos evitar usar otras validaciones

### ValueError o Typerror

```python

    try:
    except TypeError:
        """Tipo incorrecto"""
        nombre= 122
        if not isinstance(nombre,str):
            pass
    except ValueError:
        nombre = ""
        if not nombre.strip():
            pass
        """Tipo correcto pero valor incorrecto"""
        pass

```
