import Imagem as img


def gira_180(matriz: list) -> list:
    lin = len(matriz)
    col = len(matriz[0])
    resp = []
    for i in range(lin):
        resp.append([0] * col)
    #resp[lin-1][col-1 - 0] = matriz[0][0]
    #resp[lin-1][col-1 - 1] = matriz[0][1]
    #resp[lin-1][col-1 - 2] = matriz[0][2]

    for i in range(lin):
        for j in range(col):
            resp[lin - 1 - i][col - 1 - j] = matriz[i][j]

    return resp


dados = img.getMatrizImagemColorida("naturezaMorta.jpg")
mat_red = gira_180(dados[0])
mat_green = gira_180(dados[1])
mat_blue = gira_180(dados[2])

img.salvaImagemColorida("natureza180.jpg", mat_red, mat_green, mat_blue)    