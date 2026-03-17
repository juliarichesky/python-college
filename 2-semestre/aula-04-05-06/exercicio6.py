import random

def cria_matriz2(qtd_lin: int, qtd_col: int, lim_inf: int, lim_sup: int) -> list:
    resp = []
    for i in range(qtd_lin):
        resp.append([0] * qtd_col)

    for i in range(qtd_lin):
        for j in range(qtd_col):
            resp[i][j] = random.randint(lim_inf, lim_sup)

    return resp


def black_white(matriz: list):
    lin = len(matriz)
    col = len(matriz[0])
    for i in range(lin):
        for j in range(col):
            if matriz[i][j] <= 127:
                matriz[i][j] = 0
            else:
                matriz[i][j] = 255

if __name__ == "__main__":
    mat = cria_matriz2(10, 10, 0, 255)
    for lin in mat:
        print(lin)

    black_white(mat)
    for lin in mat:
        print(lin) 