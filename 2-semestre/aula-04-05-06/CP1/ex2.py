def busca_binaria(lista: list, valor) -> int:
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] < valor:
            ini = meio + 1
        elif lista[meio] > valor:
            fim = meio - 1
        else:
            return meio
            
    return -1
    