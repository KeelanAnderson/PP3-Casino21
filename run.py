import random
import time

values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4,
          'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')


# Classes

class Pot:
    """ creates instance of players pot """

    def __init__(self):
        self.pot = 1000
        self.bet = 0

    def win_bet(self):
        """ adds bet to pot if player wins """
        self.pot += self.bet
        
    def lose_bet(self):
        """ takes bet if player loses """
        self.pot -= self.bet


class Card:
    """ creates instance of cards in deck """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """ creates instances of a deck of playing cards """

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        complete_deck = ''
        for card in self.deck:
            complete_deck += '\n ' + complete_deck
        return complete_deck

    def shuffle(self):
        """ shuffles the deck of cards """
        random.shuffle(self.deck)

    def deal_card(self):
        """ deals a single card from the deck """
        single_card = self.deck.pop()
        print(single_card)


class Hand:
    """ shows the hands the the dealer and player have """

    def __init__(self):
        self.cards = []
        self.value = 0 
        self.aces = 0 # counts the aces in the hand so they can be adjusted if hand > 21

    def add_card(self, card):
        """ add a card to player or dealers hand """
        self.cards.append(card)
        self.value += values[card.ranks]
        if (card.rank == 'Ace'):
            self.aces += 1

    def adjust_aces(self):
        """ changes the value of an ace in the hand if the score exceeds 21 """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# functions

deck = Deck()
player_pot = Pot()
player_hand = Hand()
dealer_hand = Hand()


def place_bet(pot):
    """ Prompts user to input their bet amounts """
    print('Minimum bets are $50')
    while True:
        player_pot.bet = int(input('Place your Bet: $'))
        if accept_bet(player_pot.bet, player_pot.pot):
            remaining_pot = player_pot.pot - player_pot.bet 
            print('Bet placed!')
            print(f"Pot: ${remaining_pot}")
            start_round(deck)
            break


def accept_bet(bet, pot):
    """ verifies if the bet amount is valid """
    try:
        if bet > pot or bet < 50:
            raise ValueError(
                f"\nYou tried to bet ${bet}\nYour Pot is ${pot}\nMinimum bets are $50\n"
            )
    except ValueError as error:
        print(error)
        print('Please try again...')
        return False

    return True

def start_round(deck):
    print('Dealer Shuffling Deck...\n')
    deck.shuffle()
    time.sleep(3)



def deal_first_hands(player, dealer):
    """ shows the first 4 cards dealt in the game """

    print('\nDealer Hand:')
    print('  <Card Hidden>')
    print(dealer.card[1])

    print('\nPlayer Hand:')
    print()
    print()

# gameplay

print(dealer_hand.add_card(deck.deal_card()))
print('Welcome To BlackJack!!!')
print("Your Starting Pot is $1000")
input('Please Enter Your Name: ')
place_bet(player_pot)

deal_first_hands(player_hand, dealer_hand)

























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
