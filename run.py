import random
import time
import itertools

values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4,
          'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')

# deck = list(itertools.product(values, suits))
starting_pot = 1000


class Card:
    """ creates instance of cards in deck """                                                                               

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """ creates instances of a deck of playing cards """

    def __init__(deck):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        
        complete_deck = ''
        for card in self.deck:
            complete_deck += '\n ' + complete_deck
        return complete_deck

    def shuffle(self):
        random.shuffle(self.deck)


    def deal_card(self):
        single_card = self.deck.pop()
        print(single_card)


class Hand:
    """ shows the hands the the dealer and player have """

    def __init__(self):
        self.cards = []
        self.value = 0 
        self.aces = 0 # counts the aces in the hand so there can be adjusted if hand > 21

    def add_card(self, card):
        """ add a card to player or dealers hand """
        self.cards.append(card)
        self.values += values[card.rank]
        if (card.rank == 'Ace'):
            self.aces += 1

    def adjust_aces(self):
        """ changes the value of an ace in the hand if the score exceeds 21 """
        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1



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
    print('Dealer Shuffling Deck...\n')
    random.shuffle(deck)
    time.sleep(3)

place_bet()

# player_score  = []
# dealer_score = []


# def pull_card():
#     """ deals the next card from shuffled deck"""
#     random.shuffle(deck)
#     card_pulled = deck.pop()
#     card_value = values[card_pulled[0]]
    
#     card = card_pulled[0] + ' of ' + card_pulled[1]
#     print(f"    {card}")
#     del card_pulled
#     return deck and card_value and card_pulled


# def deal_dealer_card():
#     """ deals the next card from shuffled deck"""
#     random.shuffle(deck)
#     card_pulled = deck.pop()
#     card_value = values[card_pulled[0]]
#     dealer_score.append(card_value)
#     card = card_pulled[0] + ' of ' + card_pulled[1]
#     print(f"    {card}")
#     del card_pulled
#     return deck and card_value


# def deal_player_card():
#     """ deals the next card from shuffled deck"""
#     random.shuffle(deck)
#     card_pulled = deck.pop()
#     card_value = values[card_pulled[0]]
#     player_score.append(card_value)
#     card = card_pulled[0] + ' of ' + card_pulled[1]
#     print(f"    {card}")
#     del card_pulled
#     return deck and card_value
    

# def calculate_score(value):
#     """ calculate player score """
#     Sum = sum(value)
#     print(Sum)
