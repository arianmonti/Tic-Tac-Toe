"""Tic-Tac-Toe game
two-player, sample, fun

Created: 2019
Updated: 2020
Author: arianmonti
"""

from os import system, name
import sys
import time
from termcolor import colored
import functions as func

table, a, counter = [], [], 0
win = (
    (0, 1, 2),
    (0, 3, 6),
    (2, 4, 6),
    (3, 4, 5),
    (1, 4, 7),
    (2, 5, 8),
    (6, 7, 8),
    (0, 4, 8),
)


for i in range(1, 10):
    table.append(i)  # Add elements to table

# showing logo for 1500ms


def main(counter):
    ''' Main function '''
    try:
        while True:
            system('cls') if name == "nt" else system('clear')
            func.Print_table(table)
            player_X = input("Player " + colored("X", "red") + " : ")
            if func.check_inp(player_X):
                break
            player_X = int(player_X) - 1
            table[player_X] = "X"
            a.append(player_X)
            counter += 1
            if func.check_tk(a):
                break
            if func.check_x_win(table, counter, main, a, win):
                break
            if func.check_tie(counter, table, main, a):
                break
            system('cls') if name == "nt" else system('clear')
            func.Print_table(table)
            player_O = input("Player " + colored("O", "green") + " : ")
            if func.check_inp(player_O):
                break
            player_O = int(player_O) - 1
            table[player_O] = "O"
            a.append(player_O)
            counter += 1
            if func.check_tk(a):
                break
            if func.check_o_win(table, counter, main, a, win):
                break
            if func.check_tie(counter, table, main, a):
                break

    except BaseException:
        sys.exit("Unexpected Error :)")


if __name__ == "__main__":
    func.Print_logo()
    time.sleep(1.5)
    main(counter)
