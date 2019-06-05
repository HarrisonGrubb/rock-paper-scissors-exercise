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

computer_choice =  random.choice(rock_paper_scissors)
print('Computer choice:', computer_choice)

#FIND WINNER

# rock > scissors, paper > rock, scissors > paper, same = tie
user_win = 'THE USER WINS!!!'
comp_wins = 'THE COMPUTER WINS!!!'

if user_choice == computer_choice:
    print("IT'S A TIE!!!")
elif user_choice == 'rock' and computer_choice == 'paper':
    print(comp_wins)
elif user_choice == 'rock' and computer_choice == 'scissors':
    print(user_win)
elif user_choice == 'paper' and computer_choice == 'scissors':
    print(comp_wins)
elif user_choice == 'paper' and computer_choice == 'rock':
    print(user_win)
elif user_choice == 'scissors' and computer_choice == 'rock':
    print(comp_wins)
else:
    print(user_win)

#
#DISPLY FINAL OUTCOMES