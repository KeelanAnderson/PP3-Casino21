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
        return self.pot
        
    def lose_bet(self):
        """ takes bet if player loses """
        self.pot -= self.bet
        return self.pot

    def show_pot(self):
        """ Displays player pot """
        return self.pot


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
            complete_deck += '\n ' + card.__str__()
        return 'The Deck has: ' + complete_deck

    def shuffle(self):
        """ shuffles the deck of cards """
        random.shuffle(self.deck)

    def deal_card(self):
        """ deals a single card from the deck """
        single_card = self.deck.pop()
        return single_card


class Hand:
    """ shows the hands the the dealer and player have """

    def __init__(self):
        self.cards = []
        self.value = 0 
        self.aces = 0 # counts the aces in the hand so they can be adjusted if hand > 21

    def add_card(self, card):
        """ add a card to player or dealers hand """
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_aces(self):
        """ changes the value of an ace in the hand if the score exceeds 21 """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# functions

deck = Deck()
deck.shuffle()
player_pot = Pot()
pot = Pot().show_pot()
player_hand = Hand()
dealer_hand = Hand()
dealer_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())
player_hand.add_card(deck.deal_card())
player_hand.add_card(deck.deal_card())

# Betting

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

# game

    
def start_round(deck):
    """ shuffles the deck and starts the game """
    print('Dealer Shuffling Deck...\n')
    
    time.sleep(3)


def deal_first_hands(player, dealer):
    """ shows the first 4 cards dealt in the game """

    print('\nDealer Hand:')
    print('<Card Hidden>')
    print(dealer.cards[1])

    print('\nPlayer Hand:  ', *player.cards, sep='\n')
    print('Player Score = ', player.value)


def show_dealers_hand():
    """ reveals dealer hand and score to determine the winner """
    print('\nDealer Hand:  ', *dealer_hand.cards, sep='\n')
    print('Dealer Score = ', dealer_hand.value)


def show_players_hand():
    """ reveals dealer hand and score to determine the winner """
    print('\nPlayer Hand:  ', *player_hand.cards, sep='\n')
    print('Player Score = ', player_hand.value, '\n')


def hit(hand, deck):
    """ deals card if to player or dealer if they hit and calls adjusts any aces of score > 21 """
    hand.add_card(deck.deal_card())
    hand.adjust_aces()


def hit_or_stay(hand, deck):
    """ gives the player the option to hit or stay """
    
    global playing

    while True:
        option = input("\nDo you want to HIT or STAY ? Enter 'h' or 's': ")
        if option.lower() == 'h':
            hit(hand, deck)
        elif option.lower() == 's':
            playing = False
            print('Dealer is playing...')
            time.sleep(3)
        else:
            print("Enter 'h' to HIT or 's' to Stay: ")
            continue
        break

# game loop to next round


def next_round(pot):
    """ offers the user the chance to play another round or cash in their bets """

    while True:
        play_again = input("\nWould you like to play another round or cash in your bets? Enter 'play' or 'cash': ")
        if play_again.lower() == 'play':
            place_bet(pot)

            # clear

        elif play_again.lower() == 'cash':
            print(f" $$$ you won ${pot.show_pot()}. Thanks for playing! $$$ ")
            exit()
        else:
            print("Enter 'play' to Play another round or 'cash' to Leave the Casino: ")
            continue
        break

# game outcomes


def player_busts():
    """ keep bets, dealer wins, offer next round """

    print('Player Busts')
    show_players_hand()
    dealer_wins(player_pot)
    next_round(player_pot)


def dealer_busts():
    """ player wins, award winnings, offer next round """

    print('Dealer Busts')
    player_wins(player_pot)
    next_round(player_pot)


def player_wins(pot):
    """ returns results if player wins """
    print('Player Wins!!!')
    player_pot.win_bet()
    print(f"Pot: ${pot.show_pot()}")
    next_round(player_pot)


def dealer_wins(pot):
    """ returns results if player loses"""
    print('Dealer Wins!!!')
    pot.lose_bet()
    print(f"Pot: ${pot.show_pot()}")
    next_round(player_pot)


def round_draw(pot):
    """ returns the results if a draw """
    print('Its a Draw!')
    print(f"Pot: ${pot.show_pot()}")
    next_round(player_pot)
 
# gameplay

playing = True

print()
print('Welcome To BlackJack!!!')
print("Your Starting Pot is $1000")
input('Please Enter Your Name: ')
place_bet(player_pot)



while playing:
    deal_first_hands(player_hand, dealer_hand)
    hit_or_stay(player_hand, deck)

    if player_hand.value > 21:
        player_busts()  # keep bets dealer wins
        break

    if player_hand.value == 21:
        print('Blackjack!!!\n')
        playing = False
        print('Dealer is playing...')
        time.sleep(3)
            

if player_hand.value <= 21:

    while dealer_hand.value < player_hand.value:
        hit(dealer_hand, deck)
    
    show_dealers_hand()

    if dealer_hand.value > 21:
        dealer_busts()

    elif dealer_hand.value == 21:
        print('blackjack') 
        if player_hand.value == 21:
            round_draw(player_pot)
        else:
            dealer_wins(player_pot)

    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_pot)

    elif dealer_hand.value == player_hand.value:
        round_draw(player_pot)

        




 