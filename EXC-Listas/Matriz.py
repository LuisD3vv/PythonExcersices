matriz_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
col1, col2, col3 = zip(*matriz_2)
fila1, fila2, fila3 = matriz_2

print(fila1)
for n,j,k in zip(col1,col2,col3):
    print(f"[{n}][{j}][{k}]")


