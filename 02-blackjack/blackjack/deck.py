import random


class Deck():
    HEARTS = '♡'
    SPADES = '♤'
    CLUBS = '♧'
    DIAMONDS = '♢'

    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING, ACE)
    suits = (HEARTS, SPADES, CLUBS, DIAMONDS)
    size = len(ranks) * len(suits)

    def __init__(self):
        self.deck = []

        for c in Deck.ranks:
            for s in Deck.suits:
                self.deck.append((c, s))

    def shuffle(self):
        random.shuffle(self.deck)

    def pop(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        return f"Deck({len(self)}/{Deck.size})"
