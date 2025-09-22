gols_A = int(input("Gols do time A: "))
gols_B = int(input("Gols do time B: "))


if gols_A >= gols_B:
    if gols_A == gols_B:
        print("Empataram")
    else:
        print("Vencedor foi o time A")
else:
    print("Vencedor foi o time B")