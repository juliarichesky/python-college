def busca(matriz: list, valor: float) -> list:
    lin = len(matriz)
    col = len(matriz[0])

    for i in range(lin):
        for j in range(col):
            if matriz[i][j] == valor:
                return [i, j]
    
    return [-1, -1]


mat = [
    [4.5, 7.8, 3.2, -0.9],
    [51.6, 79.1, -53.9, 45.2],
    [8.5, -3.8, 6.2, 10.9]
]    

print(busca(mat, 79.1))
print(busca(mat, -0.9))
print(busca(mat, -2.3))