import baralho

maco = baralho.cria('Normal')
baralho.embaralha2(maco)

pts_jog1 = 0
pts_jog2 = 0

for i in range(26):
    c1 = baralho.compra(maco)
    c2 = baralho.compra(maco)

    str_c1 = baralho.gera_string_carta(c1) 
    str_c2 = baralho.gera_string_carta(c2) 

    print(f"{str_c1}")
    print(f"{str_c2}")

    if c1[0] < c2[0]:
        pts_jog1 = pts_jog1 + 1
    else:
        pts_jog2 = pts_jog2 + 1

print(f"Jogador 1: {pts_jog1}")
print(f"Jogador 2: {pts_jog2}")