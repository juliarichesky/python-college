def esta_ordenado(lista: list, chave: str) -> bool:
    i = 0
    while i < len(lista) - 1:
        #print(lista[i][chave])
        if lista[i][chave] > lista[i+1][chave]:
            return False
        i = i + 1
    return True


def encontra_chave_ordenada(carros: list) -> str:
    chaves = ["placa", "modelo", "montadora", "ano"]
    for chave in chaves:
        resp = esta_ordenado(carros, chave)
        if resp:
            return chave

    return None

carros = [    
    {"placa": "BJU 8932","modelo": "Corcel","montadora": "Ford","ano": 1980},    
    {"placa": "CKR 0293","modelo": "Fusca","montadora": "Volkswagen","ano": 1984},
    {"placa": "ADF 5620","modelo": "BMW","montadora": "GM", "ano": 1994},
    {"placa": "HJW 0394","modelo": "Ram","montadora": "Dodge","ano": 2020},
    {"placa": "DHU 8282","modelo": "Virtus","montadora": "Volkswagen","ano": 2018}
]

resultado = encontra_chave_ordenada(carros)
if resultado:
    print("A chave que esta ordenada é", resultado)
else:
    print("Nenhuma chave esta ordenada!")

