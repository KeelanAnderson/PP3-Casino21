import random
import time
import itertools

values= ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

deck = list(itertools.product(values, suits))
random.shuffle(deck)

starting_pot = 1000

def game_intro():
    """ Gives introduction to the game. Shows players starting pot.
    prompts user to enter their name. """

    print('Welcome To BlackJack!!!')
    print(f"Your Starting Pot is ${starting_pot}")
    input('Please Enter Your Name: ')

game_intro()


def place_bet():
    """ Prompts user to input their bet amounts """
    print('Minimum bets are $50')
    while True:
        bet = int(input('Place your Bet: $'))
        if accept_bet(bet, starting_pot):
            remaining_pot = starting_pot - bet 
            print('Bet placed!')
            print(f"Pot: ${remaining_pot}")
            start_round(deck)
            break


def accept_bet(bet_amount, pot):
    """ verifies if the bet amount is valid """
    try:
        if bet_amount > pot or bet_amount < 50:
            raise ValueError(
                f"\nYou tried to bet ${bet_amount}\nYour Pot is ${pot}\nMinimum bets are $50\n"
            )
    except ValueError as error:
        print(error)
        print('Please try again...')
        return False

    return True

def start_round(deck):
    print('Dealer Shuffling Deck...')
    random.shuffle(deck)
    time.sleep(3)
    deal_card()
    
    

def deal_card():
    """ deals a single card from shuffled deck"""
    print('Player')
    for i in range(2):
        print(deck[i][0], 'of', deck[i][1])


place_bet()
