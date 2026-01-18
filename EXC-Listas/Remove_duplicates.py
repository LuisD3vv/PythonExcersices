'''
    Remover los duplicados de una lista manteniendo el orden
'''


def remove_dupl(input_list):
    seen = set()
    result = []

    for x in input_list:
        # muy sencillo de entender
        if x not in seen:
            result.append(x)
            seen.add(x)
        # en caso de que este, pues no se agrega
    return result



given_list  = [1,2,2,3,1,4,2]
result = remove_dupl(given_list)
print(f"Orignal list {given_list}")
print(f"Without duplicates {result}")