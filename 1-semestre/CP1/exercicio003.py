#Escreva um algoritmo que mostra TODAS as opções de pagamento de um produto, considerando o preço normal de etiqueta e as condições de pagamento presentes na tabela abaixo:

#FAIXAS DE CONSUMO      |   VALOR POR M³
#-----------------------------------------
#Até 20m³               |   R$2,00
#Acima de 20 até 35m³   |   R$3,50
#Acima de 35 até 50m³   |   R$5,50
#Acima de 50m³          |   R$7,00

#Devido a escassez de água que atinge a cidade, a Companhia decidiu premiar o consumidor que conseguir diminuir o consumo mensal em relação à média de consumo mensal do ano anterior. Além de menos m³ gastos, será concedido um desconto de 20% no valor da conta. Do mesmo modo, o consumidor cujo consumo mensal ultrapassar em mais de 10% a média de consumo do ano anterior, sofrerá uma multa de 30% no valor da conta.

#Sua tarefa é desenvolver um algoritmo que lê dois números reais, o primeiro número representa a média de consumo em m³ do ano anterior e o segundo representa o consumo em m³ do mês vigente. Após a leitura dos dados seu programa deverá mostrar o valor total da conta e o valor da multa ou desconto se houver.

#Por exemplo, suponha um consumo mensal de 40m³ e a média do ano anterior foi de 48m³, assim as operações seriam:

#Valor do Consumo: 220,00 (40 ∗ 5,50)
#Desconto: 44,00 (20% de 220,00)
#Total da Conta: 176,00

#Vamos ver um outro exemplo que resultará em pagamento de multa: consumo mensal 24m³ e média do ano anterior 20m³. Note que o consumo mensal excedeu em mais de 10% a média de consumo do ano anterior, nesta situação será aplicada a multa.

#Valor do Consumo: 84,00 (24 ∗ 3,50)
#Multa: 25,20 (30% de 84,00)
#Total da Conta: 109,20

media_consumo_anterior = float(input("Digite a média de consumo do ano anterior (em m³): "))
consumo_mes_atual = float(input("Digite o consumo do mês atual (em m³): "))

#VALOR BASE
valor_por_m3 = 0
if consumo_mes_atual <= 20:
    valor_por_m3 = 2.00
elif consumo_mes_atual <= 35:
    valor_por_m3 = 3.50
elif consumo_mes_atual <= 50:
    valor_por_m3 = 5.50
else:
    valor_por_m3 = 7.00

valor_consumo_base = consumo_mes_atual * valor_por_m3
print("-" * 30)
print("Conta de Água:")
print("-" * 30)
print(f"O consumo base foi de ({consumo_mes_atual:.2f} m³).")
print(f"Valor total: R${valor_consumo_base:.2f}")
print("-" * 30)

#DESCONTO OU MULTA
if consumo_mes_atual < media_consumo_anterior:
    desconto = valor_consumo_base * 0.20
    valor_final_conta = valor_consumo_base - desconto
    print(f"Desconto de 20%: R${desconto:.2f}")
    print(f"Valor total da conta com desconto: R${valor_final_conta:.2f}")

#MULTA
elif consumo_mes_atual > media_consumo_anterior * 1.10:
    multa = valor_consumo_base * 0.30
    valor_final_conta = valor_consumo_base + multa
    print(f"Multa de 30%: R${multa:.2f}")
    print(f"Valor total da conta com multa: R${valor_final_conta:.2f}")

#SEM ALTERAÇÃO
else:
    valor_final_conta = valor_consumo_base
    print("Consumo dentro da média, sem alteração no valor.")
    print(f"Valor total da conta: R${valor_final_conta:.2f}")
print("-" * 30)