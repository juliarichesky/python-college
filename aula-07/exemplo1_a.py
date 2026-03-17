try:
    numero = int(input("Informe um numero: "))
    print(f"O numero é {numero}")
except ValueError as erro:
    print("Erro fatal aconteceu: ", erro)
    print("Encerrando a execução do código!")
    quit()

print("Continua o fluxo do algoritmo!")


