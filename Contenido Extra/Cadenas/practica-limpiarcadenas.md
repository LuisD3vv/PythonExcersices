Nivel 1: Cadenas y limpieza

    Eliminar espacios
    Dada la cadena " Hola mundo \n", elimina los espacios y saltos de línea.

    Eliminar símbolos personalizados
    Quita todos los *, - y = del inicio y fin de la cadena: "***---Hola===\n".

    Separar valores
    Dada la cadena "nombre:juan|edad:20|correo:juan@mail.com", sepárala en partes y extrae cada valor.

🟡 Nivel 2: Leer líneas y procesarlas

    Leer un archivo y limpiar
    Crea un archivo .txt con varias líneas, algunas vacías. Lee cada línea, elimina los saltos de línea, y salta las vacías.

    Contar líneas válidas
    Cuenta cuántas líneas no vacías hay en un archivo.

    Extraer campos por línea
    Cada línea es como:
    "User: lissandro | Password: b'$2b$12$...' (Encrypted) | Date: 2025-05-21"
    Extrae solo el nombre de usuario y el hash en una lista de tuplas.

🔴 Nivel 3: Encriptación con bcrypt

    Registrar usuario con bcrypt
    Crea una función que guarde un usuario y su contraseña encriptada en un archivo.

    Verificar login
    Crea una función que lea el archivo, busque al usuario, y verifique si la contraseña ingresada coincide con el hash usando bcrypt.checkpw.

    Evitar duplicados
    Modifica el sistema anterior para no permitir registros con el mismo nombre de usuario.


    Limpieza de cadenas

    Eliminar caracteres no deseados
    Dada la cadena "### Bienvenido a Python!!! \n", elimina los #, !, espacios y el salto de línea del final.

    Limpiar lista de cadenas
    Tienes una lista:
    [" Juan\n", " Ana ", "\tPedro", ""]
    Limpia cada nombre y elimina los vacíos.

🧩 Separar cadenas

    Separar por delimitadores
    Dada esta cadena:
    "nombre=luis;edad=20;correo=luis@mail.com"
    Separa los datos en un diccionario.

    Extraer de formato personalizado
    De la cadena:
    "User: ana | Password: secreto | Date: 2025-05-21"
    Extrae solo el usuario y la fecha.

🔁 Reemplazar o modificar

    Reemplazar símbolos
    Dada "Hola-mundo-Python" convierte todos los - en espacios.

    Cambiar formato de fecha
    Convierte "21/05/2025" a "2025-05-21" usando split() y join().

🔍 Buscar y contar

    Buscar palabras clave
    De un texto largo, encuentra cuántas veces aparece la palabra "Python" (mayúsculas o minúsculas).

    Validar extensión de archivo
    De una lista de archivos como ["doc.txt", "imagen.jpg", "notas.txt"], filtra solo los .txt.

🔠 Formateo y condiciones

    Formatear nombre completo
    Dado " jUAN péREz " devuelve "Juan Pérez" (limpio y capitalizado).

    Verificar contenido
    Verifica si una cadena contiene solo letras y espacios (nombres válidos).

