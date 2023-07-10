#! -*- coding: utf-8 -*-
"""
MASTERMIND
"""
import os
import argparse

from mastermind import core


def game(params):
    print_welcome_screen(params)
    play(params)
    while play_again():
        play(params)


def play_again():
    again = input("Do you want to play again [y/n]? ")
    if again.lower() == 'y':
        return True
    elif again.lower() == 'n':
        print('Bye!')
        return False
    else:
        return play_again()


def play(params):
    attempts = 0
    invalid_guess = False
    board = []
    combination = core.generate_combination(params)

    while attempts < params.attempts:
        attempts += 1

        print_board(params, board)
        if not invalid_guess:
            guess = input("Enter your guess: ")
        else:
            guess = input("Invalid input. Enter your guess again:")
            invalid_guess = False

        # Check user input.
        if not core.is_guess_ok(guess, params.clenght,  params.irange):
            invalid_guess =True
            attempts -= 1
            continue

        response = core.response(combination, guess)
        board.append("{c} - {r}".format(c=guess, r=response))
        print_board(params, board)

        if guess == combination:
            print("That's right. You win!!")
            return True

    print_board(params, board)
    print("Game over. You lose. ({})".format(combination))


def print_board(params, board):
    os.system('clear')
    print("~~~ GUIU ~~~")
    print()
    row_lenght = params.clenght * 2 + 3
    print("-" * (row_lenght + 2))
    for attempt in range(params.attempts):
        try:
            guess = board[attempt]
        except IndexError:
            guess = " " * row_lenght
        print("|{guess}{fill}|".format(guess=guess, fill=" " * (row_lenght - len(guess)))),
    print("-" * (row_lenght + 2))
    print()


def print_welcome_screen(params):
    os.system('clear')


def main():
    parser = argparse.ArgumentParser()

    attemps = 8
    parser.add_argument('-a', '--attempts', type=int, default=attemps,
                        help='Attemps to guess the combination. '
                             'Default is {}.'.format(attemps))

    clenght = 4
    parser.add_argument('-l', '--clenght', type=int, default=clenght,
                        help='Combination lenght. Default is {}.'.format(clenght))

    irange = 6
    parser.add_argument('-i', '--irange', type=int, default=irange,
                        help='Items range. Default is {}.'.format(irange))

    params = parser.parse_args()

    game(params)


if __name__ == '__main__':
    main()
