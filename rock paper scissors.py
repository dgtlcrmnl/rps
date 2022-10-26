import random

rock_design = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_design = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_design = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


a = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0
draws = 0

# This loop the enables the user to play. Q will quit, anything else other than rock paper or scissors will ask them if they want to play again.
while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ')
    if user_input == 'q':
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        continue

# The computer will randomly rock paper or scissors from table a. It will print what the computer drew.
    comp_action = random.choice(a)
    print('You chose ' + user_input + ' and the computer chose ' + comp_action + '!')


# Defines what wins/loses and ties. Each win adds a point. Ties are neutral.
    if comp_action == 'rock' and user_input == 'rock':
        print(rock_design + 'vs.' + rock_design + '\nIt was a draw :/')
        draws += 1

    elif comp_action == 'paper' and user_input == 'paper':
        print(paper_design + '\nvs.' + paper_design + '\nIt was a draw :/')
        draws += 1

    elif comp_action == 'scissors' and user_input == 'scissors':
        print(scissors_design + '\nvs.' + scissors_design + '\nIt was a draw :/')
        draws += 1

    elif comp_action == 'paper' and user_input == 'rock':
        print(paper_design + '\nvs.' + rock_design + '\nYou lost. :(')
        computer_wins += 1

    elif comp_action == 'scissors' and user_input == 'paper':
        print(scissors_design + '\nvs.' + paper_design + '\nYou lost. :(')
        computer_wins += 1

    elif comp_action == 'rock' and user_input == 'scissors':
        print(rock_design + '\nvs.' + scissors_design + '\nYou lost. :(')
        computer_wins += 1

    elif comp_action == 'rock' and user_input == 'paper':
        print(rock_design + 'vs.' + paper_design + '\nYou won!')
        user_wins += 1

    elif comp_action == 'scissors' and user_input == 'rock':
        print(scissors_design + 'vs.' + rock_design + '\nYou won!')
        user_wins += 1

    elif comp_action == 'paper' and user_input == 'scissors':
        print(paper_design + 'vs.' + scissors_design + '\nYou won!')
        user_wins += 1
print(f'wins: {user_wins}\nlosses: {computer_wins}\ndraws: {draws}')
