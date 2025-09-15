#escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma partida. escrever o nome do vencedor. caso não haja vencedor deverá ser impresso a palavra EMPATE.

timeA = int(input("Digite o nome do primeiro time: "))
golsA = int(input("Digite o número de gols do primeiro time: "))
timeB = int(input("Digite o nome do segundo time: "))
golsB = int(input("Digite o número de gols do segundo time: "))

if golsA>golsB:
    print(input(f"{timeA} possui mais gols que {timeB}"))
elif golsB>golsA:
    print(input(f"{timeB} possui mais gols que {timeA}"))
else:
    print(input("EMPATE!"))