n = int(input("Qtd de alunos: "))

acumulador = 0
i = 0
notas = []
while i < n:
    nota = float(input(f"Informe a nota do aluno {i+1}: "))
    acumulador = acumulador + nota
    notas.append(nota)

    i = i + 1

media = acumulador / n
print(f"A média foi {media}")

conta_alunos_acima = 0
conta_alunos_abaixo = 0
for n in notas:
    if n >= media:
        conta_alunos_acima = conta_alunos_acima + 1
    else:
        conta_alunos_abaixo = conta_alunos_abaixo + 1

print(f'Qtd de alunos acima ou iguais a média: {conta_alunos_acima}')
print(f'Qtd de alunos abaixo da média: {conta_alunos_abaixo}')