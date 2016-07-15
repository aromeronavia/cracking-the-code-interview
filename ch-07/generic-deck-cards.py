class CardDeck:
    def __init__(self, cards):
        self.cards = cards

class Card:
    def __init__(self, value, cardType):
        self.value = value
        self.type = cardType

    def __repr__(self):
        return str(self.value) + ' ' + self.type

class PockerDeck(CardDeck):
    def __init__(self, cards):
        super(cards)

cards = map(lambda x: Card(x, 'spades'),range(10))
print cards
