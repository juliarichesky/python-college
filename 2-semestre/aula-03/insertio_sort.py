def organiza(lista: list, i: int):
    aux = lista[i]
    while i > 0 and lista[i-1] > aux:
        lista[i] = lista[i-1]
        i = i - 1
    
    lista[i] = aux

def ordena(lista: list):
    for i in range(1, len(lista)):
        organiza(lista, i)


if __name__ == "__main__":
    dado = [5, 8, 2, 16, 2, 5, 4, 0, 23, 17, 43, 23, 9]
    print(dado)
    ordena(dado)
    print(dado)