import unittest
from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import Player, DumbComputerPlayer


class PlayerTest(unittest.TestCase):

    def test_player_has_a_name_and_balance(self):
        p = Player("Ivan", 500)

        self.assertAlmostEqual(p.name, "Ivan")
        self.assertEqual(p.balance, 500)

    def test_balance_operations_and_check(self):
        p = Player("Ivan", 500)

        p.give_money(42)
        self.assertEqual(p.balance, 542)

        p.make_stake(442)
        self.assertEqual(p.balance, 100)

        self.assertTrue(p.has_enough_money(100))
        self.assertFalse(p.has_enough_money(101))

    def test_hand_manipulation_methods(self):
        p = Player("Ivan")
        self.assertEqual(p.hand, None)

        hand = Hand()
        p.give_cards(hand)
        self.assertEqual(p.hand, hand)

        p.game_over()
        self.assertEqual(p.hand, None)
