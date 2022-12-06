![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Blackjack Game

This is my third project on the Full Stack Web Developer at Code Institute course. The aim was to build a command-line application that allows your users to manage a common dataset about a particular domain. I decided to go with my own idea for this project after examining the brief and create a game of Blackjack.
Its one of my favourite card games and I was very excited to build it for my project. Blackjack is a python terminal game, which runs in the Code Institue mock terminal on Heroku.
Users will play against the computer who will be the dealer in a game of blackjack, also known as 21. They will be given a starting pot of $1000 from which they can make bets and then play a round of blackjack until they either lose all of their money or cash out and "Leave the Casino".

## How to play Blackjack

The game follows the traditional rules of Blackjack. you csn find out more abouit it on https://www.blackjackapprenticeship.com/how-to-play-blackjack/

In this game the user will be given a starting pot of $1000 from which they can place bets. Minimum bets allowed are $50. if a player has less than $50 they wont be able to place another bet and will be kicked out of the casino. Once they have placed a bet, the game will begin and 2 cards will be given to the player and to the dealer. the dealers first card is hidden. from these 2 cards the player must decide with to hit or stay. If they hit they will be dealt another card. If they stay it will be the dealers turn to play. if either players score goes above 21 they will bust and lose. if they have the same score its a draw. if they have 21 its blackjack, whoever has the highest score is the winner unless they bust. if both have 21 its a draw. once the winner has been choosen the bets will go to the winner and the user can play another if they wish or they can chooose the cash in their bets and which point their Final pot wil be displayed on screen and the program will finish. The aim of the game is to make as much money as possible.

## Features
### Existing Features

### Future Features

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