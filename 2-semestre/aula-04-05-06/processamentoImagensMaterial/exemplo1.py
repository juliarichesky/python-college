import Imagem as img

tripla = img.getMatrizImagemColorida("gato.jpg")
matriz_vermelha = tripla[0]  #pegando a matriz tons de red
matriz_green = tripla[1]
matriz_blue = tripla[2]

linhas = len(matriz_vermelha)
colunas = len(matriz_vermelha[0])
print(f"{colunas} X {linhas}")

input()

#for lin in matriz_vermelha:
#    print(lin)
img.salvaImagemColorida("gato2.jpg", matriz_green, matriz_blue, matriz_vermelha)
print("imagem salva com sucesso")