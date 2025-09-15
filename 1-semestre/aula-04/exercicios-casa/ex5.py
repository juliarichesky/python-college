#a jornada de trabalho diária de um trabalhador é de 8 horas. caso o trabalhador tenha trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra. o valor da hora-extra é o valor que ele recebe por hora acrescido de 50%. 

#supondo que ele trabalhe apenas nos dias úteis, escreva um algoritmo que recebe:
#a) o total de dias úteis de um mês
#b) o total de horas trabalhadas pelo trabalhador
#c) quanto o trabalhador recebe por hora

#calcule e mostre o valor recebido a título de hora-extra (se houver) e o salário final do trabalhador.

dias_uteis = int(input("Digite o total de dias úteis no mês: "))
horas_trabalhadas = int(input("Digite o total de horas trabalhadas no mês: "))
recebe_por_hora = int(input("Digite o quanto o trabalhador recebe por hora: "))

#cálculo jornada mensal padrão (8 horas por dia útil)
jornada_mensal = dias_uteis * 8

#se o trabalhador fez mais horas do que a jornada mensal, tem hora extra
if horas_trabalhadas>jornada_mensal:
    horas_extras = horas_trabalhadas - jornada_mensal
    salario_base = jornada_mensal * valor_por_hora #salário pelas horas normais
    print(f"Salário base (horas normais): R$ {salario_base:.2f}")
else:
    horas_extras = 0
    salario_base = horas_trabalhadas * valor_por_hora #salário pelas horas normais


#cálculo horas extras
valor_extra = valor_por_hora * 1.5 #50% acréscimo
salario_extra = horas_extras * valor_extra
print(f"Valor das horas extras: R$ {salario_extra:.2f}")

#cálculo salário final
salario_final = salario_base + salario_extra
print(f"Salário final: R$ {salario_final:.2f}")

#Como funciona o código:
#Entrada de dados: O programa pede para o usuário informar o número de dias úteis, as horas trabalhadas no mês e o valor por hora.

#Cálculo da jornada mensal: Calculamos a quantidade total de horas normais (8 horas por dia útil).
#Verificação de horas extras: Se o trabalhador trabalhou mais do que o esperado, calculamos as horas extras.
#Cálculo do valor das horas extras: A hora extra tem um acréscimo de 50%, então multiplicamos o valor da hora normal por 1.5.
#Cálculo do salário final: Somamos o salário das horas normais com o valor das horas extras (se houver).

#Exemplo:

#Se o trabalhador tem 22 dias úteis, trabalhou 180 horas e recebe R$ 15 por hora:
#Ele tem 16 horas extras.
#O valor da hora extra será R$ 22.50 (R$ 15 x 1.5).
#O salário final será a soma do salário das horas normais com o salário das horas extras.