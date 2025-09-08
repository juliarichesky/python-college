#escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. seu algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim de 2024. por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu programa deverá imprimir: Fulano de tal tem (ou terá) 34 anos.

nome = input("Escreva o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = 2024 - ano_nascimento

print(f"{nome} tem (ou terá) {idade} anos.")