from collections import Counter


def stringCount(text):
    # como tal no necesita mas que el propio counter que ya regresa el contador (un diccionario)
    return Counter(text)


text = "Python Programming".lower().replace(" ","")
print(stringCount(text))