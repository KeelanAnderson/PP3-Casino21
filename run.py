import random

player_pot = 1000

def game_intro():
    """ Gives introduction to the game. Shows players starting pot.
    prompts user to enter their name. """

    print('Welcome To BlackJack!!!')
    print(f"Your Starting Pot is ${player_pot}")
    input('Please Enter Your Name: ')

game_intro()


def place_bet():
    """ Prompts user to input their bet amounts """
    print('Minimum bets are $50')

    bet = int(input('Place your Bet: $'))

    accept_bet(bet)



def accept_bet(player_bet):
    """ verifies if the bet amount is valid """
    try:
        if player_bet > player_pot or player_bet < 50:
            raise ValueError(
                f"You tried to bet ${player_bet}\nYour Pot is ${player_pot}\nMinimum bets are $50"
            )
    except ValueError as e:
        print(e)
        print('Please try again...')


place_bet()