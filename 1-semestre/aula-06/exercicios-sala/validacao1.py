#em muitos dos algoritmos devemos fazer validações dos dados de entrada. com os comandos de repetição, temos condições de garantir que a informação esteja correta antes do algoritmo prosseguir. vejamos o seguinte problema:

#problema 4.4: escreva um programa que, dadas duas notas de 0 a 10, calcula a média aritmética entre elas

nota1 = float(input("Digite a nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota inválida! Digite novamente: "))

#print(f"A 1 nota informada foi {nota1}")

nota2 = float(input("Digite a nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Nota inválida! Digite novamente: "))

media = (nota1 + nota2) / 2
print(f"A media é {media}")