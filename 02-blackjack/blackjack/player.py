DEALER = 'DEALER'
HIT = 'HIT'
STAY = 'STAY'


class Player():
    def __init__(self, name, initial_balance=100):
        self.name = name
        self.balance = initial_balance
        self.hand = None

    def give_cards(self, hand):
        self.hand = hand

    def game_over(self):
        self.hand = None

    def give_money(self, amount):
        self.balance += amount

    def has_enough_money(self, amount):
        return self.balance >= amount

    def make_stake(self, amount):
        if self.has_enough_money(amount):
            self.balance -= amount
        else:
            raise RuntimeError(f"{self.name} does not have enough money; stake={amount}, balance={self.balance}")

    def take_turn(self):
        raise NotImplementedError("You must inherit Player and implement take_turn method")

    def __str__(self):
        return f'{self.name}(${self.balance}): {self.hand}'


class HumanPlayer(Player):

    def take_turn(self):
        inp = input("Hit or Stay? ")[0].lower()
        if inp == 'h':
            return HIT
        else:
            return STAY


class DumbComputerPlayer(Player):

    def take_turn(self):
        return HIT
