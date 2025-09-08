#neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual de aumento. você deverá escrever um algoritmo que recebe 2 números reais representando os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que João obteve.

salario_antes = float(input("Digite o salário antes do aumento: "))
salario_depois = float(input("Digite o salário depois do aumento: "))

percentual_aumento = ((salario_depois - salario_antes) / salario_antes) * 100

print(f"O percentual de aumento foi de {percentual_aumento}%.")