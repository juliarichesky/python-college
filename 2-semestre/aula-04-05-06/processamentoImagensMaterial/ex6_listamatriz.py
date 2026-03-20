import Imagem as img

matriz = img.getMatrizImagemCinza("olhos.jpg")

lin = len(matriz)
col = len(matriz[0])

#criando uma matriz para guardas as informações
resultado = []
for i in range(lin):
    resultado.append([0] * col)

#print(lin, " ", col)

for i in range(lin):
    for j in range(col):
        if matriz[i][j][0] <= 110:
            resultado[i][j] = 0
        else:
            resultado[i][j] = 255
img.salvaImagemCinza("olhos_preto_branco.jpg", resultado)