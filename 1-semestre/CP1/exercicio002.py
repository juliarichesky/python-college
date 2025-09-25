#Escreva um algoritmo que mostra TODAS as opções de pagamento de um produto, considerando o preço normal de etiqueta e as condições de pagamento presentes na tabela abaixo:

#CÓDIGO    |   CONDIÇÃO DE PAGAMENTO
#------------------------------------------------------------------
#1         |   A vista em dinheiro ou pix, recebe 10% de desconto
#2         |   A vista no débito, recebe 5% de desconto
#3         |   Em duas vezes, juros de 4%
#4         |   Em três vezes, juros de 8%

#Seu programa deverá receber o valor do produto e mostrar todas as opções de pagamento com o respectivo valor quando o pagamento for feito em apenas uma vez e os valores das parcelas já acrescido dos juros quando for dividir. Imagine a situação onde o caixa informa todas as opções de pagamento disponíveis para os clientes.

valor_produto = float(input("Digite o valor do produto: R$"))

#A VISTA COM 10% DE DESCONTO (DINHEIRO OU PIX)
valor_opcao1 = valor_produto - (valor_produto * 0.10)
print("-" * 30)
print(f"Para pagamentos em (Dinheiro/Pix): R${valor_opcao1:.2f} com 10% de desconto.")
print("-" * 30)

#A VISTA COM 5% DE DESCONTO (DÉBITO)
valor_opcao2 = valor_produto - (valor_produto * 0.05)
print(f"Para pagamentos no (Débito): R${valor_opcao2:.2f} com 5% de desconto.")
print("-" * 30)

#JUROS DE 4% (2 PARCELAS)
valor_opcao3 = valor_produto + (valor_produto * 0.04)
valor_parcela_opcao3 = valor_opcao3 / 2  
print(f"Para pagamentos em (2x) parcelados:")
print(f"O valor da parcela é: R${valor_parcela_opcao3:.2f}")
print(f"O valor total é: R${valor_opcao3:.2f} com 4% de juros.")
print("-" * 30)

#JUROS DE 8% (3 PARCELAS)
valor_opcao4 = valor_produto + (valor_produto * 0.08)
valor_parcela_opcao4 = valor_opcao4 / 3
print(f"Para pagamentos em (3x) parcelados:")
print(f"O valor da parcela é: R${valor_parcela_opcao4:.2f}")
print(f"O valor total é: R${valor_opcao4:.2f} com 8% de juros.")
print("-" * 30)