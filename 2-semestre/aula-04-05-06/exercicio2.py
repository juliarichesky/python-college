import random
#solucao do ex2
def cria_matriz(qtd_lin: int, qtd_col: int) -> list:
    resp = []
    for i in range(qtd_lin):
        resp.append([0] * qtd_col)

    for i in range(qtd_lin):
        for j in range(qtd_col):
            resp[i][j] = random.randint(0, 1000)

    return resp

def cria_matriz2(qtd_lin: int, qtd_col: int, lim_inf: int, lim_sup: int) -> list:
    resp = []
    for i in range(qtd_lin):
        resp.append([0] * qtd_col)

    for i in range(qtd_lin):
        for j in range(qtd_col):
            resp[i][j] = random.randint(lim_inf, lim_sup)

    return resp

def soma_pos(matriz: list) -> int:
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > 0:
                soma = soma + matriz[i][j]
    return soma 


if __name__ == "__main__":
    #mat = cria_matriz(qtd_lin=3, qtd_col=5)
    mat = cria_matriz2(3, 5, -10, 10)

    for lin in mat:
        print(lin)

    resp = soma_pos(mat)
    print(f"A soma dos positivos vale {resp}")