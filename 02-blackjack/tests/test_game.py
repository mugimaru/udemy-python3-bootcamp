import unittest

from blackjack.deck import Deck
from blackjack.game import Game
from blackjack.player import Player, HIT, STAY


def play(game, deck):
    game.start(deck)
    while game.winner == None:
        game.next_turn()

    game.finish()


class FakePlayer(Player):
    def __init__(self, name, balance=100, turns=[]):
        Player.__init__(self, name, balance)
        self.turns = turns

    def take_turn(self):
        if len(self.turns) == 0:
            return HIT
        else:
            return self.turns.pop(0)


class GameTest(unittest.TestCase):

    def test_game_finishes_if_player_collects_21(self):
        p1 = FakePlayer("p1", 100, [STAY, STAY])
        p2 = FakePlayer("DEALER", 100)

        game = Game(50, [p1, p2])
        deck = Deck()
        deck.deck = [
            (2, Deck.HEARTS),       # p1
            (8, Deck.CLUBS),        # p2
            (3, Deck.HEARTS),       # p1
            (2, Deck.CLUBS),        # p2
            (Deck.ACE, Deck.CLUBS),  # p2
            (Deck.ACE, Deck.HEARTS)  # game must be finished here
        ]

        play(game, deck)
        self.assertEqual(game.winner, p2)
        self.assertEqual(p2.balance, 150)
        self.assertEqual(p1.balance, 50)

    def test_game_finishes_when_one_player_left(self):
        p1 = FakePlayer("p1", 100)
        p2 = FakePlayer("p2", 100)

        game = Game(50, [p1, p2])
        deck = Deck()
        deck.deck = [
            (9, Deck.HEARTS),               # p1
            (8, Deck.CLUBS),                # p2
            (8, Deck.HEARTS),               # p1
            (2, Deck.CLUBS),                # p2
            (Deck.JACK, Deck.CLUBS),        # p2
            (Deck.ACE, Deck.HEARTS)         # game must be finished here
        ]

        play(game, deck)

        self.assertEqual(game.winner, p2)
        self.assertEqual(p2.balance, 150)
        self.assertEqual(p1.balance, 50)
