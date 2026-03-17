import Imagem as img

def transposta(mat: list) -> list:
    lin = len(mat)
    col = len(mat[0])
    resp = []
    for i in range(col):
        resp.append([0] * lin)

    for i in range(lin):
        for j in range(col):
            resp[j][i] = mat[i][j]
    return resp    


matriz = img.getMatrizImagemCinza("yao-ming.png")

#Operacao Transposta de uma matriz?
#1 linha vira 1 coluna
#2 linha vira 2 coluna
#3 linha vira 3 coluna
matriz_transposta = transposta(matriz)

for lin in matriz_transposta:
    print(lin)

img.salvaImagemCinza("yao_t.png", matriz_transposta)
