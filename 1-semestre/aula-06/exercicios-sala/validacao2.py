#escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números inteiros entre 1 e n. por exemplo, se n = 10 então deverá ser calculado:

#1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 =

aux = input ("Digite um inteiro positivo: ")
n = int (aux)

while n < 0:
    aux = input ("Erro ! Digite um inteiro positivo : ")
    n = int (aux)

soma = 0;
i = 1
while i <= n:
    soma = soma + i
    i = i + 1

print ("Valor da soma vale ", soma )