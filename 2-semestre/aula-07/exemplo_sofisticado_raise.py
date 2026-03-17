produtos = [
    {"prod": "Patinete", "qtd": 20, "valor": 5700},
    {"prod": "PS5", "qtd": 100, "valor": 3500},
    {"prod": "Guarda-chuva", "qtd": 38, "valor": 42.40}
]


def venda_produto(produto: str, unidades: int) -> dict:
    for item in produtos:
        if item['prod'] == produto:  #encontrei o produto
            if item['qtd'] >= unidades:   #tenho estoque suficiente 
                pedido = {"numero": 2343, "produto": produto, "valor_unitario": item['valor'], "valor_total": item['valor'] * unidades}
                item['qtd'] = item['qtd'] - unidades
                return pedido
            else:
                raise Exception(f"Estoque insuficiente: {produto}")

    raise Exception(f"Produto {produto} não encontrado")


if __name__ == "__main__":
    try:
        pedido = venda_produto("Guarda-sol", 1000)
    except Exception as erro:
        print(erro)
    else:
        print(pedido)