#O salário mensal de um professor, sem considerar os impostos, corresponde a soma dos seguintes valores: salário base, hora-atividade e descanso semanal remunerado (DSR). Para calcular o salário base multiplicamos o número de aulas semanais por 4,5 semanas e pelo valor hora-aula, a hora-atividade corresponde a 5% do salário base e o descanso semanal remunerado corresponde a 1/6 do salário base mais a hora-atividade.

#Para exemplificar, suponha um professor que ganha 50,00 por hora-aula e leciona 12 aulas por semana:

#- Salário Base: 2.700,00 (12 * 4, 5 * 50,00)
#- Hora-atividade: 135,00 (2.700 * 5%)
#- DSR: 472, 50 (2.700,00 + 135,00) * 1/6
#- Salário Mensal: 3.307,50 (2.700,00 + 135,00 + 472,50)

#Escreva um algoritmo que calcula e imprime o valor do salário base, o valor da hora-atividade, o valor do DSR e o valor do salário mensal. A entrada do algoritmo será o número de aulas semanais e valor hora-aula, não se preocupe com a validação de dados.

aulas_semanais = float(input("Digite o número das horas semanais: "))
valor_horas_aulas = float(input("Digite o valor da hora-aula: "))
print("-" * 30)

salario_base = aulas_semanais * 4.5 * valor_horas_aulas
print(f"O salário base é de {salario_base:.2f}!")

hora_atividade = salario_base * 0.05
print(f"A hora-atividade é de {hora_atividade:.2f}!")

dsr = (salario_base + hora_atividade) / 6
print(f"O valor do DSR é {dsr:.2f}")

salario_mensal = salario_base + hora_atividade + dsr
print(f"O salário mensal total é de {salario_mensal:.2f}")
print("-" * 30)