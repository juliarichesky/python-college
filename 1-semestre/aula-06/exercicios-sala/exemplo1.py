#dados uma sequência de 5 números inteiros. calcule a soma de todos os números da sequência. vamos resolver esse nosso primeiro problema usando a linguagem Python utilizando apenas duas variáveis.

soma = 0
contador = 0

#while <condicao booleana>:
while contador < 5:
    num = float(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1

#num = float(input("Digite um número: "))
#soma = soma + num

#num = float(input("Digite um número: "))
#soma = soma + num

print(f"Resultado: {soma}")