def soma(mA: list, mB: list) -> list:
    #criar a matriz resposta
    n_lin = len(mA)
    n_col = len(mA[0])

    resposta = []
    for i in range(n_lin):
        resposta.append([0] * n_col)
    
    #resposta[0][0] = mA[0][0] + mB[0][0]
    #resposta[0][1] = mA[0][1] + mB[0][1]
    for i in range(n_lin):
        for j in range(n_col):
            resposta[i][j] = mA[i][j] + mB[i][j]
    
    return resposta