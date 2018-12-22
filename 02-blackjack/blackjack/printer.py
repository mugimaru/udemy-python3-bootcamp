from blackjack.player import DEALER


def format_game_state(game):
    if game.deck == None:
        return f'{format_game_title(game)}. Has not started yet'

    formatted = ''
    if game.winner != None:
        formatted += f'\nWinner:\n  {format_player(game.winner, True, False)}\n'

    if len(game.players) > 0:
        formatted += '\nPlayers:\n'
        for p in game.players:
            formatted += ('  ' + format_player(p, game.winner != None, p.name == DEALER) + '\n')

    if len(game.busted_players) > 0:
        formatted += '\nBustedPlayers:\n'
        for p in game.busted_players:
            formatted += ('  ' + format_player(p, game.winner != None, False) + '\n')

    return formatted


def format_game_title(game):
    return f'Game with stake ${game.stake}'


def format_player(p, show_value, hide_first_card):
    return f'{p.name}: {format_hand(p.hand, show_value, hide_first_card)}'


def format_hand(hand, show_value, hide_first_card):
    if hand == None:
        return 'No cards'

    l = list(map(lambda card: f'{card[0]}{card[1]}', hand.cards))

    if hide_first_card:
        l[-1] = 'XX'

    formatted = ' '.join(l)
    if show_value:
        return f'{formatted} ({hand.best_value()})'
    else:
        return formatted
