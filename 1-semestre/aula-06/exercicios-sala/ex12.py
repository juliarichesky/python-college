def inverte(numero: int) -> int: #criando uma função que inverte os números
    reposta = 0
    while numero != 0:
        dig = numero % 10
        resposta *= 10 + dig
        numero //= 10
    return resposta


num = int(input("Digite um nº: ")) #º = alt+167

invertido = inverte(num)

if num == invertido:
    print(f'{num} é palindromo.')
else:
    print(f"{num} não é palíndromo.")