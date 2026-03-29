

# Creamos un array de tamaño 4x3, formado únicamente por unos (1)

unos = np.ones((4,3))
unos

# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)

cero = np.zeros((2,4,3))
cero

# Creamos un array de números en el rango de 0 a 100, con un paso de 5

array_1 = np.arange(0,101,5)
array_1

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)

array_2 = np.random.randint(0,10,(2,5))
array_2

# Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5)

array_3 = np.random.random((3,5))
array_3

# Establecemos la "semilla" de números aleatorios en 27
np.random.seed(27)
# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)
array_4 = np.random.randint(0,10,(3,5))
array_4

# basicamente se estanca el putisimo coidigo

# Encontramos los valores únicos del array_4
np.unique(array_4)

# Extraemos el elemento de índice 1 del array_4
array_4[1]

# Extraemos las primeras dos filas del array_4
array_4[:2]

# Extraemos los dos primeros datos de las primeras dos filas del array_4
array_4[:2,:2]

# Creamos dos arrays de tamaño 3x4: uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos
array_5 = np.random.randint(0,10,(3,4))
array_6 = np.ones((3,4))

# invocamos el array_5
array_5

# invocamos el array_6
array_6

# Sumamos los dos arrays
array_5 + array_6

# Creamos ahora un array de tamaño (4,3) lleno de unos
array_7= np.one(4,3)
array_7

# Intentaremos sumar los arrays 6 y 7
array_6 + array_7


# Entonces crearemos otro array de tamaño (4,3) lleno de unos
array_8 = np.ones((4,3))
array_8

# Restamos el array_8 al array_7
array_8 - array_7

# Creamos otros dos arrays de tamaño 3x3 con números aleatorios del 1 al 5
array_9 = np.random.randint(1,6,(3,3))
array_10 = np.random.randint(1,6,(3,3))

# invocamos el array_9
array_9

# invocamos el array_10
array_10

# Multiplicamos los últimos dos arrays entre sí
array_9 * array_10

# Elevamos el array_9 al cuadrado
np.pow(array_9,2)

# Buscamos la raíz cuadrada del array_10
np.sqrt(array_10)

# Hallamos el promedio de los valores del array_9
np.mean(array_9)

# Hallamos el valor máximo de los valores del array_9
np.max(array_9)

# Hallamos el valor mínimo de los valores del array_9
np.min(array_9)

# Cambiamos la forma del array_9 por una de 9x1, y lo almacenamos como array_11

array_11 = np.reshape(array_9,(9,1))

# invocamos el array_11
array_11

# Transponemos el array_11
np.transpose(array_11)