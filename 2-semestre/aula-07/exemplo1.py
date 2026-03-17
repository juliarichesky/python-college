try:
    numero = int(input("Informe um numero: "))
    print(f"O numero é {numero}")
except ValueError as erro:
    print("Algo deu errado: ", erro)

print("Continua o fluxo do algoritmo!")


