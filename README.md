# Python-Solitaire-Game

How to Run (English Translation):

Unpack the contents of the file 16-18_Python_Marcin_Radzewicz.rar to a location of your choice. The file should contain only a folder named 16-18_Python_Marcin_Radzewicz, which holds all the files. Please check that the files in the folder are working correctly (open them, check they are not empty, and close them without saving).

v

Open the newly unpacked folder and ensure the following files are present:

Pasjans.py

ranking.txt

README.txt

zasady.txt

requirements.txt

v

Make sure you have Python installed (the version I tested the program on is: 3.13.3). Type the command python in the command line to check.

v 2 methods for running the program itself:

=====================

1.v

Open the terminal in the project folder (option 1: Use the command line and navigate to the folder with the cd command | option 2: With the project folder open, type CMD in the file path bar; the command line should open with the correct folder location).

1.v

In the command line with the project folder location open, type the command:

python Pasjans.py

=====================

2.v

Run the Pasjans.py program in an application that allows Python code editing and execution, such as Visual Studio Code (VSC) or another Python-compatible editor.

2.v

In the selected application, run the program in the terminal.

=====================

Gameplay Instructions:

The game starts in console mode and displays an options menu:

[1] Start Game

[2] Game Rules

[3] Card Symbol Description

[4] Display Shuffled Deck

[0] Settings

Enter the selected option using the corresponding number, e.g., [1] "Start Game". The "Settings" option appears multiple times and allows you to quit the game or start a new one.

Game Mode: The game has two difficulty levels:

Easy - Only 1 card is drawn to the deck at this level.

Hard - 3 cards are drawn to the deck at this level.

After starting the game, an interface with card columns and the pile is visible.

The player can perform actions by selecting from the menu:

[1] Move a card or a set of cards between columns

[2] Move a card to the destination pile

[3] Shuffle a card from the deck

[4] Draw a card from the deck

[5] Undo move (max 3 moves)

[0] Settings (quit / restart)

Controls: All actions are performed by typing numbers and confirming with Enter. Error messages/hints are displayed automatically after an incorrect move.

The game ends in a win when all cards have been moved to the final piles. The player may lose if no more moves are possible, at which point the only option is to surrender.

=====================
