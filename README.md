# Last Pencil Game

Welcome to the Last Pencil game! This is a simple text-based game where a player and a bot take turns removing pencils from a pile. The goal is to avoid being the one to take the last pencil.

## How to Play

1. Run the `game.py` script to start the game.
2. Enter the number of pencils you want to use for the game.
3. Choose who goes first: the player or the bot.
4. Take turns with the bot to remove 1 to 3 pencils from the pile.
5. The one who takes the last pencil loses the game.

## Bot Strategy

The bot has two strategies based on its position:
- In a losing position the bot either takes a random allowed number of pencils or the last pencil.
- In a winning position (e.g., when there are 4, 8, 12... or 3, 7, 11... pencils left), the bot aims to force the opponent into a losing position.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.11.4 or above installed.
3. Run the game by executing `python game.py` in your terminal.

## Example Gameplay
```
How many pencils would you like to use:0
The number of pencils should be positive.
How many pencils would you like to use:five
The number of pencils should be numeric.
How many pencils would you like to use:6
Who will be the first (John, Bot):Mary
Choose between John and Bot.
Who will be the first (John, Bot):Bot
||||||
Bot's turn:
1
|||||
John's turn:
2
|||
Bot's turn:
2
|
John's turn:
0
Possible values: '1', '2' or '3'.
|
John's turn:
1
Bot won!
```
