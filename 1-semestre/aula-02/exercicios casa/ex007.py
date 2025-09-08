#uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. escreva um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. seu algoritmo deverá ler o número de camisas, o número de calças e o número de pares de sapato.

x = int(input("Digite o número de camisas: "))
y = int(input("Digite o número de calças: "))
z = int(input("Digite o número de pares de sapato: "))

maneiras_de_se_vestir = x * y * z

print(f"O número de maneiras de se vestir é: {maneiras_de_se_vestir}")