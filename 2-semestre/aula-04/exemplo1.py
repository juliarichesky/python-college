matriz = []
for i in range(4):
    matriz.append([0] * 5)

valor = 1

for i in range(4):   #percorrendo as linhas
    for j in range(5):   #percorrendo as colunas
        matriz[i][j] = valor
        valor = valor + 1





for lin in matriz:
    print(lin)