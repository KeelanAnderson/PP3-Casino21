import random
import time
import itertools

values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4,
          'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 
          'King': 10}

suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

deck = list(itertools.product(values, suits))




# starting_pot = 1000

# def game_intro():
#     """ Gives introduction to the game. Shows players starting pot.
#     prompts user to enter their name. """

#     print('Welcome To BlackJack!!!')
#     print(f"Your Starting Pot is ${starting_pot}")
#     input('Please Enter Your Name: ')

# game_intro()


# def place_bet():
#     """ Prompts user to input their bet amounts """
#     print('Minimum bets are $50')
#     while True:
#         bet = int(input('Place your Bet: $'))
#         if accept_bet(bet, starting_pot):
#             remaining_pot = starting_pot - bet 
#             print('Bet placed!')
#             print(f"Pot: ${remaining_pot}")
#             start_round(deck)
#             break


# def accept_bet(bet_amount, pot):
#     """ verifies if the bet amount is valid """
#     try:
#         if bet_amount > pot or bet_amount < 50:
#             raise ValueError(
#                 f"\nYou tried to bet ${bet_amount}\nYour Pot is ${pot}\nMinimum bets are $50\n"
#             )
#     except ValueError as error:
#         print(error)
#         print('Please try again...')
#         return False

#     return True

# def start_round(deck):
#     print('Dealer Shuffling Deck...')
#     random.shuffle(deck)
#     time.sleep(3)
#     deal_card()


def deal_card():
    """ deals the next card from shuffled deck"""
    random.shuffle(deck)
    card_pulled = deck.pop()
    card_value = values[card_pulled[0]]
    card = card_pulled[0] + ' of ' + card_pulled[1]
    print(card)
    del card_pulled
    return deck and card_value


deal_card()

# player_score = []


# def calculate_player_score(value):
#     """ calculate player score """
#     player_score.append(value)
#     Sum = sum(player_score)
#     print(Sum)


# place_bet()
