'''
Unir dos diccionarios, si comparten una clave, el nuevo diccionario debe almecar una lista con ambos valores que comparten la clave(), en lugar de sobrescribir
'''


def merge_dict(d1,d2):
    result = {}
    llaves = []
    for key1,key2 in zip(d1.keys(),d2.keys()):
        print(key1,key2)
    return llaves


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge_dict(d1,d2))


