import random

a = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

# This loop the enables the user to play. Q will quit, anything else other than rock paper or scissors will ask them if they want to play again.
while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ')
    if user_input == 'q':
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        continue

# The computer will randomly rock paper or scissors from table a. It will print what the computer drew.
    comp_action = random.choice(a)
    print('The computer drew ' + comp_action + '!')

# Defines what wins/loses and ties. Each win adds a point. Ties are neutral.
    if comp_action == 'rock' and user_input == 'rock':
        print('It was a tie :/')

    elif comp_action == 'paper' and user_input == 'paper':
        print('It was a tie :/')

    elif comp_action == 'scissors' and user_input == 'scissors':
        print('It was a tie :/')

    elif comp_action == 'paper' and user_input == 'rock':
        print('You lost. :(')
        computer_wins += 1

    elif comp_action == 'scissors' and user_input == 'paper':
        print('You lost. :(')
        computer_wins += 1

    elif comp_action == 'rock' and user_input == 'scissors':
        print('You lost. :(')
        computer_wins += 1

    elif comp_action == 'rock' and user_input == 'paper':
        print('You won!')
        user_wins += 1

    elif comp_action == 'scissors' and user_input == 'rock':
        print('You won!')
        user_wins += 1

    elif comp_action == 'paper' and user_input == 'scissors':
        print('You won!')
        user_wins += 1

# Prints how many wins the user had and how many the computer had over the session.
print('User wins:', user_wins)
print('Computer wins:', computer_wins)
print('Thanks for playing!')