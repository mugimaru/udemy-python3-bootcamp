import unittest
from blackjack.deck import Deck


class DeckTest(unittest.TestCase):

    def test_shuffle_changes_cards_order(self):
        d = Deck()

        for _ in range(0, 4):
            deck_before = d.deck.copy()
            self.assertEqual(None, d.shuffle())
            self.assertNotEqual(d.deck, deck_before)

    def test_pop_takes_first_card_from_deck(self):
        d = Deck()

        first_card = d.deck[0]
        self.assertEqual(first_card, d.pop())
        self.assertNotEqual(first_card, d.deck[0])

    def test_len_of_deck(self):
        d = Deck()
        self.assertEqual(len(d), len(d.deck))
        d.pop()
        self.assertEqual(len(d), len(d.deck))

    def test_pop_retruns_non_for_empty_deck(self):
        d = Deck()

        for _ in range(0, Deck.size):
            self.assertNotEqual(d.pop(), None)

        self.assertEqual(len(d), 0)
        self.assertEqual(None, d.pop())

    def test_deck_to_string(self):
        d = Deck()
        d.pop()

        self.assertEqual("Deck(51/52)", str(d))
