# Blackjack Game

This is my third project on the Full Stack Web Developer at Code Institute course. The aim was to build a command-line application that allows your users to manage a common dataset about a particular domain. I decided to go with my own idea for this project after examining the brief and create a game of Blackjack.
Its one of my favourite card games and I was very excited to build it for my project. Blackjack is a python terminal game, which runs in the Code Institue mock terminal on Heroku.
Users will play against the computer who will be the dealer in a game of blackjack, also known as 21. They will be given a starting pot of $1000 from which they can make bets and then play a round of blackjack until they either lose all of their money or cash out and "Leave the Casino".

[Here is the live version of my project](https://blackjack-keelananderson.herokuapp.com/)

![ Blackjack Game ](/readme-images/blackjack-game.png "Text to show on mouseover")

## How to play Blackjack

The game follows the traditional rules of Blackjack. you csn find out more abouit it on https://www.blackjackapprenticeship.com/how-to-play-blackjack/

In this game the user will be given a starting pot of $1000 from which they can place bets. Minimum bets allowed are $50. if a player has less than $50 they wont be able to place another bet and will be kicked out of the casino. Once they have placed a bet, the game will begin and 2 cards will be given to the player and to the dealer. the dealers first card is hidden. from these 2 cards the player must decide with to hit or stay. If they hit they will be dealt another card. If they stay it will be the dealers turn to play. if either players score goes above 21 they will bust and lose. if they have the same score its a draw. if they have 21 its blackjack, whoever has the highest score is the winner unless they bust. if both have 21 its a draw. once the winner has been choosen the bets will go to the winner and the user can play another if they wish or they can chooose the cash in their bets and which point their Final pot wil be displayed on screen and the program will finish. The aim of the game is to make as much money as possible.

## Features
### Existing Features
#### Introduction

When the prgram is run first it will print "Welcome to Blacljack!!!" with the pyfiglet library
then in normal text it will display the starting pot amount and prompt the user to enter their name. There is no restriction on the names than can be entered here. 

![ Blackjack intro ](/readme-images/blackjack-intro.png "Text to show on mouseover")

#### Place bet

next the user user will be prompted to place a bet. the pyinputplus library is used here to hanlde invalid input. The minimum bet is $50 and the maximum is whatever amount is in the pot at the time. If anything else is typed in the user will be promped to enter in a number that iss valid. One the bet has been validated by the accept_bet function it will show that the bet was placed , the money lwft in the pot after the bet, and the dealer will begin shuffling the deck and deal 2 cards to both the dealer and the player and the game will begin. the cards dealt will be displayed except for the dealers first card which isnt revealed until the dealer starts playing.

![ place bet ](/readme-images/blackjack-place-bet.png "Text to show on mouseover")

#### Player Hand

The players hand is all the cards in possesion of the player at any time. The first hand will be the first 2 cards dealt and each card will be displayed on screen along with the value of this cards added together. From this the player with understand very easily the value of their hand and can decided whether they want to gamble on improving this hand or keep it.

![ player hand ](/readme-images/blackjack-place-bet.png "Text to show on mouseover")

#### Hit or Stay

The user will be promped with a message saying "Do you want to hit or stay?" they must enter 'h' if they wish to hit and be dealt another card to their hand or 's' if they wish to stay with the hand they have. This message will keep poping up each time the user hits until thet decide to stay with the hand they have, At which point the dealer will begin to play. if at any time the value of the players hand goes above 21 the player will go bust and the dealer automatically wins.

![ Hit or Stay ](/readme-images/blackjack-hit-or-stay.png "Text to show on mouseover")

#### Dealer Hand

After the player has stayed its the dealers turn to play. the dealer has the advantage knowing the players score. the dealers hand will be displayed every time they hit with a 3 seconds pause each time so the user can keep track. If the dealers hand is less than the player hand in value the dealer will hit. they will keep hitting until their value is higher than the players or the same for a draw. The dealer will lose if they go bust trying to beat the player.

![ player hand ](/readme-images/blackjack-place-bet.png "Text to show on mouseover")

#### Result

The outcome of the game be displayed at the end. There are 5 different outcomes in this game and 3 different result. Either the player or the dealer can bust which results in the opposite side winning. Either player can win be obtaining a higher score than their opponent or if their hands values are the same they will draw. if the player wins they win back their bet and the amount of their bet. If they lose the dealer keeps the bets and if its a draw the bet placed is returned to be player. When the game is over the winner is displayed and the ammount thats in the players pot.

##### Its a Draw
![ draw ](/readme-images/blackjack-draw.png "Text to show on mouseover")
##### Player busts, Dealer wins
![ player busts ](/readme-images/blackjack-player-busts.png "Text to show on mouseover")
##### Dealer busts, Player wins
![ dealer bust ](/readme-images/blackjack-dealer-busts.png "Text to show on mouseover")


#### Next Round

The game will then ask the user "Would you like to play another round or cash in your bets?". It then prompts the user to enter 'play' or 'cash'. If the user enters 'play' a new round will begin starting with the bets. If the user enters 'cash' the game will display the ammount the user had in their pot and thank them for playing and the program finishes. For example,  $$$ you won $12345 Thanks for playing! $$$ . If the user decides to play but has less than $50 they will be kicked out of the casino and the message "You Went Broke, Better Luck Next Time!" will be displayed on screen and the program will end. If the user enters anything other than 'play' or 'cash' they will be prompted to try again. They must enter 'play' or 'cash' to continue.

![ play ](/readme-images/blackjack-play.png "Text to show on mouseover")
![ cash ](/readme-images/blackjack-cash.png "Text to show on mouseover")
![ broke ](/readme-images/blackjack-broke.png "Text to show on mouseover")

### Future Features

Some future features I would like to include would be a high scores leaderboard displaying the top 10 players that cashed out with the highest ammount. Another feature I would like to include would be a menu where the user could choose from multiple different cards games to play from which would make the app like an online casino. 

## Data Model

I have 4 different classes in my project. The pot class, card class, decl class and hand class. the pot class creates an instance of the players pot. The pot class stores the ammount in the players pot and the ammount the player bets. This class also has methods including win_bet, lose_bet and show_pot. The win_bet method will add the winnings to players pot. The lose_bet method will takes the betted ammount from the pot and the show_pot method will print out the ammount in the players pot at any given time.
the card class creates an instance of a single card. it stores the ranks and suits of the cards. The deck class creates an instance of a deck of 52 playing cards. It stores an the cards of the deck in a list. it has method to shuffle the deck and deal a single card from the deck and remove it from the list and into the game.
the hand class creates 2 instances of players hand and dealers hand. it stores the cards of each hand in a list, the value of the hand and the value of the aces in the hand. It has the methods add_card which adds a card from the deck to the hand and the adjust_aces method which chances the value of an ace in the hand from 11 to 1 if the value of the hand was to go above 21. 

## Tesing

I have manually tested this project be doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs strings when numbers are expected and vice versa, empty inputs, out of bounds inputs and same inputs twice
- Tested the program in my local terminal and the Code Institute Heroku terminal.

![ python linter ](/readme-images/blackjack-linter.png "Text to show on mouseover")

### Bugs
#### solved bugs

- I really struggled at the end of the project trying to get the game to enter into another round after the first one i tried using too many while loops and wasnt making any progress. This was very frustrating and I spoken to my mentor about it. He showed me how to use breakpoints and the run and debug section in gitpod so i could see how my code was executing line by line. This was a massive help and a push in the right direction. I scraped all the new code i had written and went back to the point in my program that was running smoothly. Then executing the code line by line and writing new code as I went. I was able to make progress a lot easier and more quickly. In future this is how I will write my code, before I was guilty of trying to do to many things at once and makeing a mess of my code. This is something I need to work on to make life easier. 

- When I first made the game loop into the next round the player and dealer hands werent clearing from the round before. This was obviously a problem because we needed to start from scatch for thr next round. To solve this Imade the reset function when initialises the hand and deck class instances and also reshiffles the deck. This function was called before the new game was started and seems to have fixed the problem.  

- when testing the game by playing it I was dealt the rare first hand of double aces which displayed a score of 22 on screen. I quickly realised I had not called my adjust_aces method at the start of the game and this was a problem. I added the adjust_aces method for the player and dealer hands under where I added the cards at the start but the problem was not solved so I added the methods to the start of my hit_or_stay function and this solved the problem. I was lucky to have noticed this as the chances of drawing this hand at the beginning of the game are very low and it could have easilt went unoticed.  

#### unsolved bugs

- "You went broke" message printing the same number of times as rounds played. I decided to left this untouched for now as I think it looks like a nice feature.

#### Validator testing
##### PEP8
- No errors were returned from https://pep8ci.herokuapp.com/

## Deployment

This project was deployed using code institues mock terminal for heroku

#### Steps for deployment:

- fork or clone this repository
- Login to Heroku app
- Create a new Heroku app
- Only 'Deploy' and 'Settings' are relevant from the menu section. Starting with the 'Settings' first.
- Set buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository on Github
- Enter the name of the repository we want to connect it with and click 'Connect'
- The choice appears now to either deploy using automatic deploys or manual deployment, which deploys the current state of the branch.
- Click on Deploy

[Here is the live version of my project](https://blackjack-keelananderson.herokuapp.com/)

## Credits

- To my mentor, Andre Aquilina , for guiding me through the process and offering assistance when neccesary to point me in the right direction.
- The Slack community. The help a student is able to receive from the other students is a really great tool to have.
- To all at Code Institute, the videos and information I received helped me create my third portfolio project.
- https://www.blackjackapprenticeship.com/how-to-play-blackjack/ for the details about the game of Blackjack.
- https://www.youtube.com/watch?v=8QTsK1aVMI0&t=1447s this youtube tutorial was very helpful in my project especially in helping me to create my classes for the game to make it object-orriented. Some of the code in this tutorial was used in my project.
- To Heroku for the live version of the deployed project
- To Gitpod and Github where I coded the program and held this Repository
- To StackOverflow which helped be to solve bugs in my code and helped with my understanding of python.
- To Code institute https://pep8ci.herokuapp.com/# for code validator
- GeeksForGeeks helped me chose which external library to import
- python libaries pyfiglet and pyinputplus which are external libaries installed and both used in my project for the intro and with handling invalid input in place bets function.
- the images for the README file were cropped and edited using paint