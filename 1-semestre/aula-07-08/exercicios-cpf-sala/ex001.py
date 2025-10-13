#faça um programa que recebe um inteiro representando os números de um CPF e imprime ele formatado. por exemplo, se o número for 12345678910, seu programa deverá imprimir 123.456.789-10.

#USAREMOS ESSE EXEMPLO: 209.875.476-22

cpf = int(input("Digite seu CPF sem pontos nem hífen: "))

digitos = cpf % 100
cpf = cpf // 100

parte3 = cpf % 1000
cpf = cpf // 1000

parte2 = cpf % 1000
cpf = cpf // 1000

print(f"{cpf}.{parte2}.{parte3}-{digitos}")