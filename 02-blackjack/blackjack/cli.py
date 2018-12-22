import sys
from blackjack.game import Game
from blackjack.player import HumanPlayer, DumbComputerPlayer, DEALER
from blackjack.printer import format_game_state


def format_players_balance(players):
    return ', '.join(map(lambda p: f'{p.name}(${p.balance})', players))


def check_players_balance(stake, players):
    for p in players:
        if not p.has_enough_money(stake):
            return False
    return True


def ask_replay(players):
    inp = input(f'Play again? (Y/N)\n')[0].upper()

    if inp == 'Y':
        ask_stake_and_play(players)
    elif inp == 'N':
        pass
    else:
        ask_replay(players)


def ask_stake_and_play(players):
    try:
        stake = int(input("Choose a stake: "))
    except ValueError:
        print("You must enter a whole number!")
        ask_stake_and_play(players)
    else:
        if check_players_balance(stake, players):
            play(stake, players)
        else:
            print(
                f"Seems line at least one of the players does not have enough money to play...\n  {format_players_balance(players)}")
            ask_stake_and_play(players)


def play(stake, players):
    game = Game(stake, players)
    print(f"\nGoing to start with ${stake} stake and {len(players)} players")
    game.start()

    r = 1
    while game.winner == None:
        print(f'Round {r}; current player - {game.players[0].name}')
        print(format_game_state(game))
        r += 1
        game.next_turn()

    print(format_game_state(game))
    winner_name = game.winner.name
    game.finish()
    print(f'{winner_name} has won the game!\n  Players: {format_players_balance(players)}')

    for p in players:
        if p.balance == 0:
            print(f"{p.name} does not have enough money to continue...")
            sys.exit(0)

    ask_replay(players)


print("Hello! Let's play blackjack.")


def main(initial_balance=100):
    try:
        name = input("Enter your name: ")
        human_player = HumanPlayer(name, initial_balance)
        dealer = DumbComputerPlayer(DEALER, initial_balance)

        ask_stake_and_play([human_player, dealer])
    except KeyboardInterrupt:
        sys.exit(0)
