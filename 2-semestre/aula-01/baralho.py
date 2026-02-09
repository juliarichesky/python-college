import random

def cria(tipo: str) -> list: #essa função é responsável para gerar todas as cartas do baralho.
    retorno = []
    if tipo == 'Normal':
        for valor in range(1, 14): #criando os numeros  do baralho
                                   #precisa ser até o 14 porque ele roda com -1
            retorno.append([valor, 'C']) #copas
            retorno.append([valor, 'E']) #espadas
            retorno.append([valor, 'P']) #paus
            retorno.append([valor, 'O']) #ouros

    return retorno

def embaralha(baralho: list):
    for i in range(len(baralho)): #intervalo fechado, por isso -1
        j = random.randint(0, len(baralho) - 1)
        aux = baralho[i]
        baralho[i] = baralho[j]
        baralho[j] = aux

def embaralha2(baralho: list):
    random.shuffle(baralho)

def compra(baralho: list) -> list: #uma carta
    if len(baralho) > 0:
        return baralho.pop()
    else:
        return None #é o equivalente ao null do java
    
def distribui(baralho: list, qtd: int) -> list:
    mao = []
    for i in range(qtd):
        mao.append(compra(baralho))

    return mao

#teste
if __name__ == "__main__":
    bar = cria('Normal')
    print(bar)
    embaralha(bar)
    print("_" * 30)
    print(bar)