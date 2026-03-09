class Card:
    def __init__(self, valor: int, naipe: str):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor}{self.naipe}"