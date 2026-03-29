import numpy as numpy


# Podemos crear arrays de una dimension con la funcion np.array()

array_unidim = np.array([1,2,3,4,5]) # vector

# O un array de dos dimensiones

array_bidim = np.array([[1,2,3],# bidimensional
                    [4,5,6]]) 

# o un array tridimencional

array_tridim = np.array([[1,2,3], # tridimencional
                    [4,5,6],
                    [7,8,9],
                    [10,12,13]])


# propiedades de cada uno de los arrays

# Atributos del array unidimensional (forma,numero de dimensiones,tipos, tamano y tipo)

array_unidim.shape, array_unidim.ndim,array_unidim.dtype,array_unidim.size,type(array_unidim)

# Atributos del array bidimensional (forma,numero de dimensiones,tipos, tamano y tipo)

array_bidim.shape, array_bidim.ndim,array_bidim.dtype,array_bidim.size,type(array_bidim)


# Atributos del array tridimensional (forma,numero de dimensiones,tipos, tamano y tipo)

array_tridim.shape, array_tridim.ndim,array_tridim.dtype,array_tridim.size,type(array_tridim)



