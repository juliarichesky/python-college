#escreva um algoritmo em python que recebe dois números inteiros e exibe: a soma desses dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma = num1 + num2
print(f"Soma: {soma}")

multiplicacao = num1 * num2
print(f"Multiplicação: {multiplicacao}")

divisao_inteira = num1 / num2
print(f"Divisão inteira: {divisao_inteira}")

resto_divisao = num1 % num2
print(f"Resto da divisão inteira: {resto_divisao}")