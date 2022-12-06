def hit_or_stay(hand, deck):
    """ gives the player the option to hit or stay """

    global playing

    while True:
        option = input("\nDo you want to HIT or STAY ? Enter 'h' or 's': ")
        deck.shuffle()

        if option.lower() == 'h':
            hit(hand, deck)
            show_players_hand()
        elif option.lower() == 's':
            print('Dealer is playing...')
            time.sleep(3)
            playing = False
        else:
            print("Enter 'h' to HIT or 's' to Stay: ")
            continue
        break


def next_round(pot):
    """ offers the user the chance to play another round or cash in their bets """
    play_again = input(
                "\nWould you like to play another round or "
                "cash in your bets? Enter 'play' or 'cash': \n")

    while True:
        
        if play_again.lower() == 'play':
            place_bet(player_pot)
            deal_first_hands(player_hand, dealer_hand)
            game_play()
        elif play_again.lower() == 'cash':
            print(f" $$$ you won ${pot.show_pot()}. Thanks for playing! $$$ ")
            quit()
        else:
            print("Enter 'play' to Play another round or 'cash' to Leave the Casino: ")
            continue
        break


# game outcomes


def dealer_busts():
    """ player wins, award winnings, offer next round """

    print('Dealer Busts')
    player_wins(player_pot)


def player_wins(pot):
    """ returns results if player wins """
    print('Player Wins!!!')
    player_pot.win_bet()
    print(f"Pot: ${pot.show_pot()}")


def dealer_wins(pot):
    """ returns results if player loses"""
    print('Dealer Wins!!!')
    pot.lose_bet()
    print(f"Pot: ${pot.show_pot()}")


def round_draw(pot):
    """ returns the results if a draw """
    print('Its a Draw!')
    print(f"Pot: ${pot.show_pot()}")


def player_busts():
    """ keep bets, dealer wins, offer next round """

    print('Player Busts')
    show_players_hand()
    dealer_wins(player_pot)


# game

print()
print('Welcome To BlackJack!!!')
print("Your Starting Pot is $1000")
input('Please Enter Your Name: ')


place_bet(player_pot)
deal_first_hands(player_hand, dealer_hand)



def game_play():
    playing = True
    while playing:

        hit_or_stay(player_hand, deck)

        if player_hand.value > 21:
            player_busts()  # keep bets dealer wins
            playing = False

        elif player_hand.value == 21:
            show_players_hand()
            print('Blackjack!!!\n')
            print('Dealer is playing...')
            time.sleep(3)
            break

        elif player_hand.value <= 21:

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
            
        next_round(player_pot)   


game_play()
