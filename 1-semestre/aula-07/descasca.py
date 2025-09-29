numero = int(input("Informe o número: "))

while numero != 0:
    digito = numero % 10
    print(digito)
    numero = numero // 10

#separa o numero digito por digito