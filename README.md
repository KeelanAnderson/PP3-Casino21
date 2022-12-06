# Blackjack Game

This is my third project on the Full Stack Web Developer at Code Institute course. The aim was to build a command-line application that allows your users to manage a common dataset about a particular domain. I decided to go with my own idea for this project after examining the brief and create a game of Blackjack.
Its one of my favourite card games and I was very excited to build it for my project. Blackjack is a python terminal game, which runs in the Code Institue mock terminal on Heroku.
Users will play against the computer who will be the dealer in a game of blackjack, also known as 21. They will be given a starting pot of $1000 from which they can make bets and then play a round of blackjack until they either lose all of their money or cash out and "Leave the Casino".

[Here is the live version of my project](https://blackjack-keelananderson.herokuapp.com/)

## How to play Blackjack

The game follows the traditional rules of Blackjack. you csn find out more abouit it on https://www.blackjackapprenticeship.com/how-to-play-blackjack/

In this game the user will be given a starting pot of $1000 from which they can place bets. Minimum bets allowed are $50. if a player has less than $50 they wont be able to place another bet and will be kicked out of the casino. Once they have placed a bet, the game will begin and 2 cards will be given to the player and to the dealer. the dealers first card is hidden. from these 2 cards the player must decide with to hit or stay. If they hit they will be dealt another card. If they stay it will be the dealers turn to play. if either players score goes above 21 they will bust and lose. if they have the same score its a draw. if they have 21 its blackjack, whoever has the highest score is the winner unless they bust. if both have 21 its a draw. once the winner has been choosen the bets will go to the winner and the user can play another if they wish or they can chooose the cash in their bets and which point their Final pot wil be displayed on screen and the program will finish. The aim of the game is to make as much money as possible.

## Features
### Existing Features

#### Introduction

When the prgram is run first it will print "Welcome to Blacljack!!!" with the pyfiglet library
then in normal text it will display the starting pot amount and prompy the user to enter their name. There is no restriction on the names than can be entered here. 

#### Place bet

next the user user will be prompted to place a bet. the pyinputplus library is used here to hanlde invalid input. The minimum bet is $50 and the maximum is whatever amount is in the pot at the time. If anything else is typed in the user will be promped to enter in a number that iss valid. One the bet has been validated by the accept_bet function it will show that the bet was placed , the money lwft in the pot after the bet, and the dealer will begin shuffling the deck and deal 2 cards to both the dealer and the player and the game will begin. the cards dealt will be displayed except for the dealers first card which isnt revealed until the dealer starts playing.

#### Player Hand

The players hand is all the cards in possesion of the player at any time. The first hand will be the first 2 cards dealt and each card will be displayed on screen along with the value of this cards added together. From this the player with understand very easily the value of their hand and can decided whether they want to gamble on improving this hand or keep it.

#### Hit or Stay

The user will be promped with a message saying "Do you want to hit or stay?" they must enter 'h' if they wish to hit and be dealt another card to their hand or 's' if they wish to stay with the hand they have. This message will keep poping up each time the user hits until thet decide to stay with the hand they have, At which point the dealer will begin to play. if at any time the value of the players hand goes above 21 the player will go bust and the dealer automatically wins.

#### Dealer Hand

After the player has stayed its the dealers turn to play. the dealer has the advantage knowing the players score. the dealers hand will be displayed every time they hit with a 3 seconds pause each time so the user can keep track. If the dealers hand is less than the player hand in value the dealer will hit. they will keep hitting until their value is higher than the players or the same for a draw. The dealer will lose if they go bust trying to beat the player.

#### Result

The outcome of the game be displayed at the end. There are 5 different outcomes in this game and 3 different result. Either the play or the dealer can bust which results in the opposite side winning. Either player can win be obtaining a higher score than their opponent or if their hands values are the same they will draw. if the player wins they win back their bet and the amount of their bet. If they lose the dealer keeps the bets and if its a draw the bet placed is returned to be player. When the game is over the winner is displayed and the ammount thats in the players pot.

#### Next Round

The game will then ask the user "Would you like to play another round or cash in your bets?". It then prompts the user to enter 'play' or 'cash'. if the user enters 'play' a new round will begin starting with the bets. if the user enters 'cash' the game will display the ammount the players had in their pot and thank them for playing and the program finishes. For example,  $$$ you won $12345 Thanks for playing! $$$ . If the user decides to play but has less than $50 they will be kicked out of the casino and the message "You Went Broke, Better Luck Next Time!" will be displayed on screen and the program will end. If the user enters anython others than 'play' or 'cash' they will be prompted to try again. They must enter 'play' or 'cash' to continue.

### Future Features

some future features I would like to include would be a high scores leaderboard displaying the top 10 players that cashed out with the highest ammount. Another feature I would like to include would be a menu where the user could choose from multiple different cards games to play from which would make the app like an online casino. 

## Data Model

## Tesing

### Bugs
#### solved bugs
#### unsolved bugs

#### Validator testing

## Deployment

This project was deployed using code institues mock terminal for heroku

#### Steps for deployment:

- fork or clone this repository
- Create a new Heroku app
- Set buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy

## Credits

- To my mentor, Andre Aquilina , for guiding me through the process and offering assistance when neccesary to point me in the right direction.
- The Slack community. The help a student is able to receive from the other students is a really great tool to have.
- To all at Code Institute, the videos and information I received helped me create my third portfolio project.
- https://www.blackjackapprenticeship.com/how-to-play-blackjack/ for the details about the game of Blackjack.
- https://www.youtube.com/watch?v=8QTsK1aVMI0&t=1447s this youtube tutorial was very helpful in my project especially in helping me to create my classes for the game to make it object-orriented.
- python libaries pyfiglet and pyinputplus which are external libaries installed and both used in my project for the intro and with handling invalid input in place bets function.
- To Heroku for the live version of the deployed project
- To Gitpod and Github where I coded the program and held this Repository
- To StackOverflow which helped be to solve bugs in my code and helped with my understanding of python.