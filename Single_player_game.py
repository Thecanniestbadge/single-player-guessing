# Name : Nicholas vickery
# Date : 9/1/2023
# Project : Single player game 
# Description : This game is a single player game. Like the Guessing game but only with one player against the computer.
#               The computer will select one number between 1 and 100. The player(user) will guess the number until they guess it correctly. 
#               At the end the program will print out how many guesses it took to guess the correct number.

import os 
import random

# Hide the number function
def Hide(): 
    os.system("cls")


# Computer chooses random number
mainNum = random.randint(1,100)

# Hide the number
Hide()


# Player's turn
guessed = False
tries = 0
while not guessed:
    tries += 1
    # Player guess the number
    guessNum = input("Player, please enter your guess: ")
    # If guess is too high, print too high
    if int(guessNum) > mainNum: 
        print("Sorry, too high try again.")
    # if guess is too low, print too low
    if int(guessNum) < mainNum: 
        print("Sorry, too low try again.")
    # If guess is correct, end game
    if int(guessNum) == mainNum: 
        print("Thats correct, Great guess")
        guessed = True

# Number of guess it took player to get to the correct number
print(f"Number of guesses : {tries}")