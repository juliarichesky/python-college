import random

def cria(tipo: str) -> list:
    retorno = []
    if tipo == 'Normal':
        for valor in range(1, 14):
            retorno.append([valor, '❤️'])
            retorno.append([valor, '♠️'])   #alt + 3, 4, 5, 6
            retorno.append([valor, '♣️'])
            retorno.append([valor, '♦️'])

    return retorno

def embaralha(baralho: list):
    for i in range(len(baralho)):
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

def gera_string_carta(carta: list) -> str:
    valor, naipe = carta
    
    mapeamento = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    v = mapeamento.get(valor, str(valor))
    
    espaco = "" if v == "10" else " "

    desenho = (
        f"┌─────────┐\n"
        f"│{v}{espaco}       │\n"
        f"│         │\n"
        f"│    {naipe}    │\n"
        f"│         │\n"
        f"│       {espaco}{v}│\n"
        f"└─────────┘"
    )
    
    return desenho


#teste
if __name__ == "__main__":
    bar = cria('Normal')
    print(bar)
    embaralha(bar)
    print("_" * 30)
    print(bar)