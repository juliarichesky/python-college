#um número inteiro pode ser par ou ímpar. escreva um algoritmo que recebe um número inteiro e imprime na tela a informação sobre sua paridade.

entrada = input("Digite um número inteiro: ")
num = int(entrada)
resto = num % 2
if resto == 0:
    print(num, "e par")
else:
    print(num, "e impar")