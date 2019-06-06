


def test_dummy_proof():
    assert 2 == 2

from game import my_message

def test_my_message():
    x = my_message()
    assert x == "Hello!"

# from game import determine_winner

# def test_determination_of_the_winner():
#     assert determine_winner("rock", "rock") == None # represents a tie
#     assert determine_winner("rock", "paper") == "paper"
#     assert determine_winner("rock", "scissors") == "rock"

#     assert determine_winner("paper", "rock") == "paper"
#     assert determine_winner("paper", "paper") == None # represents a tie
#     assert determine_winner("paper", "scissors") == "scissors"

#     assert determine_winner("scissors", "rock") == "rock"
#     assert determine_winner("scissors", "paper") == "scissors"
#     assert determine_winner("scissors", "scissors") == None # represents a tie