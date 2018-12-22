import unittest
from blackjack.deck import Deck
from blackjack.hand import Hand


class HandTest(unittest.TestCase):

    def test_add_card(self):
        h = Hand()
        card = (10, Deck.CLUBS)
        h.add(card)
        self.assertEqual(h.cards, [card])

    def test_values_return_possible_hand_values(self):
        h = Hand()
        h.add((10, Deck.CLUBS))
        h.add((Deck.ACE, Deck.CLUBS))

        values = h.values()
        values.sort()

        self.assertEqual(values, [11, 21])

    def test_best_value_returns_best_blackjack_hand_value(self):
        h = Hand()

        h.add((2, Deck.CLUBS))
        self.assertEqual(2, h.best_value())

        h.add((Deck.ACE, Deck.CLUBS))
        self.assertEqual(13, h.best_value())

        h.add((Deck.ACE, Deck.HEARTS))
        self.assertEqual(14, h.best_value())

    def test_hand_string_representation(self):
        h = Hand()

        h.add((2, Deck.CLUBS))
        h.add((Deck.ACE, Deck.CLUBS))

        self.assertEqual(f"A{Deck.CLUBS} 2{Deck.CLUBS}", str(h))
