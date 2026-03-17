import Imagem as img

def negativo(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = 255 - matriz[i][j]

    
mat = img.getMatrizImagemCinza("wallpaper.png")
negativo(mat)
img.salvaImagemCinza("neg_wallpaper.png", mat)

