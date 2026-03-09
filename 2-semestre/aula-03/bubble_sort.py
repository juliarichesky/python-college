def subir(lista: list, pos: int):
    i = len(lista) - 1
    while i > pos:
        if lista[i] < lista[i-1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        i = i - 1

def ordena(lista: list):
    for i in range(len(lista)):
        subir(lista, i)

lst = [4, 6, 15, 8, 7, 3, 5, 9]
ordena(lst)
print(lst)