#escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se houve um empate.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1>num2:
    print(f"{num1} é maior que {num2}!")
elif num1<num2:
    print(f"{num2} é maior que {num1}!")
else:
    print(f"Houve um empate! Os números são iguais.")