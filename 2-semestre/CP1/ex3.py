def soma_linha(mat: list) -> list:
    resp = []
    for i in range(len(mat)):
        soma = 0
        for j in range(len(mat[0])):
            soma = soma + mat[i][j]
        resp.append(soma)
    return resp

matriz = [
    [2, 3, 78, -10, 12], #Analia Franco
    [4, 2, -2, 10, 5],   #Tatuape
    [0, 4, 1, -5, 2],    #Plaza Sul
    [6, 7, 0, -3, 1],    #Ibirapuera
]

acumulado = soma_linha(matriz)
print(acumulado)
