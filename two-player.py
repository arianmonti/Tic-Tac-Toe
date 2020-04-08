"""Tic-Tac-Toe game
two-player, sample, fun

Created: 2019
Updated: 2020
Author: Arian Montazeri
"""

import os
import functions as func
table, a, counter = [], [], 0
win = ((0, 1, 2), (0, 3, 6), (2, 4, 6),
       (3, 4, 5), (1, 4, 7), (2, 5, 8),
       (6, 7, 8), (0, 4, 8))


for i in range(1, 10):
    table.append(i)  # Add elements to table
func.Print_logo()


def main(counter):
    try:
        while True:
            os.system('clear')
            func.Print_table(table)
            player_X = (int(input("Player X : ")) - 1)
            table[player_X] = "X"
            a.append(player_X)
            counter += 1
            if func.check_tk(a):
                break
            if func.check_x_win(table, counter, main, a, win):
                break
            if func.check_tie(counter, table, main, a):
                break
            os.system('clear')
            func.Print_table(table)
            player_O = (int(input("Player O : ")) - 1)
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
        print("Unexpected Error :)")


main(counter)
quit = input()
