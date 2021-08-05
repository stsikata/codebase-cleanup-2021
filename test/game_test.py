
# # TODO: import some code

#getting into test driven development (write test first then update the app)

from app.game import determine_winner

# determine_winner = 


# u = "rock"
# c = "scissors"
# winner = "USER" # / rock

def test_enlarge():
    assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    assert determine_winner(user_choice="rock", computer_choice="rock") == None
    assert determine_winner(user_choice="rock", computer_choice="scissors") == "rock"
    # assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    # assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    # # assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"

# def my_func():
# def enlarge (i):
#     return i * 100
# # TODO: test the code


