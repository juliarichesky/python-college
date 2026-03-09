import time

def busca(lista: list, x: float) -> int:
    i = 0
    while i < len(lista) and lista[i] != x:
        i = i + 1
    if i == len(lista):
        return -1
    else:
        return i

def busca_bin(lista: list, x: float) -> int:
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:  
        meio = (ini + fim) // 2
        if lista[meio] > x:
            fim = meio - 1
        elif lista[meio] < x:
            ini = meio + 1
        else:
            return meio
    return -1


conjunto = [ 2 * x for x in range(100_000_000)]

t_ini = time.time()
ret = busca(conjunto, 1)
t_fim = time.time()
print(f"{ret} -> tempo simples: {t_fim - t_ini}")

t_ini = time.time()
ret = busca_bin(conjunto, 1)
t_fim = time.time()
print(f"{ret} -> tempo binaria: {t_fim - t_ini}")