#dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula e mostra o valor do desconto e o novo preço do produto dado o percentual. e se, ao invés de um desconto, fosse um aumento. o que muda no seu algoritmo?

preco = float(input("Digite o preço do produto: R$ "))
percentual = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco * (percentual / 100)

print(f"Valor do desconto: R$ {valor_desconto: }")

#cálculo do valor do aumento
valor_aumento = preco * (percentual / 100)
#cálculo do novo preço com aumento
novo_preco = preco + valor_aumento
print(f"Novo preço do produto: R$ {novo_preco: }")