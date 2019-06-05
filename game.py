# game.py

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE User Inputs

user_choice = input("Please choose 'rock', 'paper', or 'scissors' (don't include the quotes)")

print("_____________________________")
print('YOU CHOSE:', user_choice)

#Validating the inputs

if user_choice not in ['rock', 'paper', 'scissors']:
    print('_____________________________')
    print('bad choice: please pick something in the game')
    exit()    


#GENERATE COMPUTER SELECTION
print("Generating...")


#FIND WINNER

#DISPLY FINAL OUTCOMES