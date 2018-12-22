from blackjack.deck import Deck
from blackjack.hand import Hand
from blackjack.player import DEALER, HIT, STAY


class Game():

    def __init__(self, stake, players):
        self.stake = stake
        self.bank = 0
        self.players = players
        self.winner = None
        self.busted_players = []
        self.deck = None

    def start(self, deck=None):
        if self.winner != None:
            raise RuntimeError("Game is over")

        enough_money = True
        for p in self.players:
            enough_money = p.has_enough_money(self.stake)
        if not enough_money:
            raise RuntimeError("One of the players does not have enought money to make a stake!")

        for p in self.players:
            p.make_stake(self.stake)
            p.give_cards(Hand())
            self.bank += self.stake

        if deck == None:
            self.deck = Deck()
            self.deck.shuffle()
        else:
            self.deck = deck

        for _ in range(0, 2):
            for p in self.players:
                p.hand.add(self.deck.pop())

    def next_turn(self):
        if self.winner != None:
            raise RuntimeError("Game is over")
        current_player = self.players[0]

        if current_player.take_turn() == STAY:
            self.__next_player()
        else:
            current_player.hand.add(self.deck.pop())
            self.__update_game_state()

    def finish(self):
        if self.winner == None:
            raise RuntimeError("Game has not finished yet")

        self.winner.game_over()
        self.winner.give_money(self.bank)
        self.bank = 0

        for p in self.players + self.busted_players:
            p.game_over()

    def __next_player(self):
        self.players.append(self.players.pop(0))

    def __update_game_state(self):
        active_players = []

        for p in self.players:
            hand_value = p.hand.best_value()
            if hand_value == 21:
                self.winner = p
                active_players.append(p)
            elif hand_value < 21:
                active_players.append(p)
            else:
                self.busted_players.append(p)

        self.players = active_players
        if len(self.players) == 1:
            self.winner = self.players.pop(0)

    def __str__(self):
        res = f'Game for ${self.bank}\n'
        if self.deck == None:
            return f'{res}  Has not started yet.'

        if self.winner:
            res += f'  {self.winner}\n'

        for p in (self.players + self.busted_players):
            res += f'  {p}\n'

        return res
