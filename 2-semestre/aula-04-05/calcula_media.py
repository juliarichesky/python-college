def calcula_media(notas: list) -> float:
    qtd = len(notas)
    soma = 0
    i = 0
    while i < qtd:
        soma = soma + notas[i]
        i = i + 1
    return soma / qtd

matriz = [
    [7.3, 4.9, 8.1, 6.8, 9.1, 7.5, 5.9],
    [8.8, 6.1, 7, 4.5, 6.9, 7.8, 9.2],
    [4.5, 6, 5.7, 8.5, 4.7, 6.3, 5.5]
]

for notas_aluno in matriz:
    #print(notas_aluno)
    media = calcula_media(notas_aluno)
    print(f"A media do aluno é {media}")