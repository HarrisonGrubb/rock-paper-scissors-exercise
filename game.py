# game.py
import random

rock_paper_scissors = ['rock', 'paper', 'scissors']
# CAPTURE User Inputs

user_choice = input("Please choose 'rock', 'paper', or 'scissors' (don't include the quotes)")

print("_____________________________")
print('YOU CHOSE:', user_choice)

#Validating the inputs

if user_choice not in rock_paper_scissors:
    print('_____________________________')
    print('bad choice: please pick something in the game')
    exit()    

#GENERATE COMPUTER SELECTION
print("Generating...")

computer_choice = random.choice(rock_paper_scissors)
print('Computer choice:', computer_choice)

#FIND WINNER

# if computer_choice == user_choice:
#     print("IT'S A TIE!")
#     exit
# elif computer_choice

#DISPLY FINAL OUTCOMES