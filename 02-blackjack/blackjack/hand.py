from blackjack.deck import Deck
from itertools import combinations_with_replacement
from functools import reduce


class Hand():

    def __init__(self):
        self.cards = []

    def add(self, card):
        try:
            card_rank, card_suit = card
            assert card_rank in Deck.ranks
            assert card_suit in Deck.suits
        except:
            raise TypeError("`card` is expected to be a card in (rank, suite) form.")
        else:
            self.cards.append(card)

    def values(self):
        v = 0
        number_of_aces = 0

        for (c, _) in self.cards:
            if isinstance(c, int):
                v += c
            elif c == Deck.ACE:
                number_of_aces += 1
            else:
                v += 10

        if number_of_aces == 0:
            return [v]
        else:
            return list(map(lambda values: v + sum(values), combinations_with_replacement([1, 11], number_of_aces)))

    def best_value(self):
        values = self.values()
        if len(values) == 1:
            return values[0]

        best = values.pop()

        if best == 21:
            return best

        for v in values:
            v_diff = 21 - v
            b_diff = 21 - best

            if v_diff == 0:
                return 21

            if (b_diff < 0 and v_diff > 0) or (b_diff > 0 and v_diff > 0 and b_diff > v_diff) or (b_diff < 0 and v_diff < 0 and b_diff < v_diff):
                best = v

        return best

    def __len__(self):
        len(self.cards)

    def __str__(self):
        return ' '.join(map(lambda card: f'{str(card[0])}{str(card[1])}', self.cards[::-1]))
