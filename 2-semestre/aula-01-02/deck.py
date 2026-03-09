from card import Card
import random

class Deck:

    def __init__(self, tipo: str, cards: list):
        naipes = ["♦️", "♠️", "♣️", "❤️"]
        self.cards = cards
        for v in range(1, 14):
            for n in naipes:
                self.cards.append(Card(v, n))


    def embaralha(self):
        random.shuffle(self.cards)

    def compra(self) -> Card:
        return self.cards.pop()

    def distribui(self, qtd: int) -> list:
        mao = []
        for a in range(qtd):
            mao.append(self.compra())
        return mao        

    def print(self):
        for c in self.cards:
            print(c)

if __name__ == "__main__":            
    bar = Deck('Normal', [])
    bar.embaralha()
    c = bar.compra()
    print(c)

    mao = bar.distribui(3)
    for c in mao:
        print(c.valor, c.naipe)