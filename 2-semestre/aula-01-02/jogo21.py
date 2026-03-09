import baralho as deck #apelido para o modulo baralho

def pontuacao(mao: list) -> int:
    pontos = 0
    for c in mao:
        if c[0] > 10:
            pontos = pontos + 10
        else:
            pontos = pontos + c[0]
    return pontos

def imprime_mao(mao: list):
    for c in mao:
        str_c = deck.gera_string_carta(c)
        print(str_c)
    print(f"Pontos: {pontuacao(mao)}")


def quer_carta_cpu(mao: list) -> bool:
    pontos = pontuacao(mao)
    if pontos > 16:
        return False
    else:
        return True

bar = deck.cria('Normal')
deck.embaralha(bar)

mao_hum = deck.distribui(bar, 2)
mao_cpu = deck.distribui(bar, 2)

#Jogada do ser humano
imprime_mao(mao_hum)
resp = input("Quer mais cartas (s/n)? ")
while resp == 's' or resp == "S":
    carta = deck.compra(bar)
    mao_hum.append(carta)
    imprime_mao(mao_hum)
    resp = input("Quer mais cartas (s/n)? ")

imprime_mao(mao_cpu)
while quer_carta_cpu(mao_cpu):
    carta = deck.compra(bar)
    mao_cpu.append(carta)
    imprime_mao(mao_cpu)


print(f"Você fez {pontuacao(mao_hum)} pontos")
print(f"CPU fez {pontuacao(mao_cpu)} pontos")