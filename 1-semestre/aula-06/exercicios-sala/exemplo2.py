#dado um número inteiro positivo n, escreva um algoritmo que imprime a tabuada de n até o valor 10. solução: supondo que o valor digitado seja n = 6, seu programa deverá imprimir:

n = int(input("Valor da tabuada: "))
x = 1

#enquanto x menor ou igual a 10 faça
while x <= 10:
    print(f"{n} X {x} = {n * x}")
    x = x + 1

print("Terminou a tabuada")