"""
The player can play Rock Paper Scissors
"""


import random


def main():
    rounds = 0
    player_score = 0
    computer_score = 0

    player_name = input("What's your name?\nEnter here: ")
    print(f"Let's play Rock Paper Scissors {player_name}.\n")
    while rounds < 3:
        rounds += 1
        print(f'Round {rounds}')
        compare = compare_turns()
        if compare == 'Win':
            player_score += 1
        elif compare == 'Lose':
            computer_score += 1
        print(f'{player_name} has {player_score} points.\nComputer has {computer_score} points.\n')
    if player_score > computer_score:
        print('Player wins game.')
    else:
        print('Computer wins game.')
    play_again()


def player_turn():
    player_choice = input('Rock, Paper, Scissors\nChoose: ')

    if player_choice == 'Rock':
        print('Player chose rock.')
        return 'Rock'
    elif player_choice == 'Paper':
        print('Player chose paper.')
        return 'Paper'
    elif player_choice == 'Scissors':
        print('Player chose scissors.')
        return 'Scissors'
    else:
        print(f'{player_choice} is not a valid option.\nTry again.')
        player_turn()


def computer_turn():
    computer_choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(computer_choices)

    if computer_choice == 'Rock':
        print('Computer chose rock')
        return 'Rock'
    elif computer_choice == 'Paper':
        print('Computer chose paper')
        return 'Paper'
    elif computer_choice == 'Scissors':
        print('Computer chose scissors')
        return 'Scissors'


def compare_turns():
    player_choice = player_turn()
    computer_choice = computer_turn()

    if player_choice == computer_choice:
        print("It's a tie.")
        return 'Tie'
    elif player_choice == 'Rock':
        if computer_choice == 'Paper':
            print('Player loses.')
            return 'Lose'
        elif computer_choice == 'Scissors':
            print('Player wins.')
            return 'Win'
    elif player_choice == 'Paper':
        if computer_choice == 'Scissors':
            print('Player lose.')
            return 'Lose'
        elif computer_choice == 'Rock':
            print('Player wins.')
            return 'Win'
    elif player_choice == 'Scissors':
        if computer_choice == 'Rock':
            print('Player lose.')
            return 'Lose'
        elif computer_choice == 'Paper':
            print('Player wins.')
            return 'Win'


def play_again():
    again = input('Do you want to play again?\nY/N: ')

    if again == 'Y':
        main()
    elif again == 'N':
        print('Ok, bye.')
    else:
        print(f'{again} is not a valid option.\nTry again.')
        play_again()


main()
