def contagem(lista: list, valor: object):
    ocorrencias = 0
    i = 0
    while i < len(lista):
        if valor == lista[i]:
            ocorrencias = ocorrencias + 1
        i = i + 1
    
    print(ocorrencias)

frutas = ['uva', 'uva', 'caqui', 'pequi', 'uva', 'laranha']
contagem(frutas, 'uva')
