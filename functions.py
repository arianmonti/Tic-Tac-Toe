from termcolor import colored
import os

def Print_logo():
    print(" ______________ ___  __________  ______________ ____________   __________    ______________  __________  __________      ")
    print("/_____   _____//  / /  _______/ /_____   _____//   _____    / /  _______/   /_____   _____/ / ______  / /  _______/      ")
    print("     /  /     /  / /  /              /  /     /   /    /   / /  /                /  /      / /     / / /  /______        ")
    print("    /  /     /  / /  /              /  /     /   /___ /   / /  /                /  /      / /     / / /  _______/        ")
    print("   /  /     /  / /  /_______       /  /     /   /___ /   / /  /_______         /  /      / /_____/ / /  /______          ")
    print("  /_ /     /_ / /__________/      /_ /     /___/    /___/ /__________/        /_ /      /_________/ /_________/          ")


def reset_table(table, counter, a):
    ''' This function reset table for next game'''
    table.clear()
    a.clear()
    counter = 0
    for i in range(1, 10):
        table.append(i)  


def Print_table(table):  # print tic-tac-toe table
    print(add_color(table[0]), "|", add_color(table[1]), "|", add_color(table[2]))
    print(add_color(table[3]), "|", add_color(table[4]), "|", add_color(table[5]))
    print(add_color(table[6]), "|", add_color(table[7]), "|", add_color(table[8]))


def add_color(index): # add color based on charecter
    if(index == "O"): return colored(index, "blue")
    if(index == "X"): return colored(index, "red")
    else: return index


def check_inp(inp): # user input validation
    c = False
    try:
        inp = int(inp)
        if(inp > 9 or inp < 1):
            c = True
            print("Error: Number is should be between 1 and ")
    except:
        c = True
        print("Error: Only Numbers")
    return c


def check_tie(counter, table, main, a):  # check if game tied or not
    tied = False
    if counter == 9:
        tied = True
    if (tied):
        Print_table(table)
        print("Tied")
        ask = input("Do you want to play again?(Y/n) ")
        ask = ask.upper()
        if (ask == 'Y'):
            reset_table(table, counter, a)
            main(counter)
    return tied


def check_tk(a):  # check if the number is'nt used before
    b = False
    for i in range(0, 9):
        if (a.count(i) > 1):
            b = True
    if b:
        print("Error: The Place is already full")
    return b


def check_x_win(table, counter, main, a, win):  # check if x win or not
    x_won = False
    for win_check in win:
        if table[win_check[0]] == "X" and table[win_check[1]
                                                ] == "X" and table[win_check[2]] == "X":
            x_won = True
    if x_won:
        os.system('clear')
        Print_table(table)
        print(colored("X", 'red') + " win")
        ask = input("Do you want to play again?(Y/n) ")
        ask = ask.upper()
        if (ask == 'Y'):
            reset_table(table, counter, a)
            main(counter)
    return x_won


def check_o_win(table, counter, main, a, win):  # check if o win or not
    o_win = False
    for win_check in win:
        if table[win_check[0]] == "O" and table[win_check[1]
                                                ] == "O" and table[win_check[2]] == "O":
            o_win = True
    if o_win:
        os.system('clear')
        Print_table(table)
        print(colored("O", 'blue') + " win")
        ask = input("Do you want to play again?(Y/n) ")
        ask = ask.upper()
        if (ask == 'Y'):
            reset_table(table, counter, a)
            main(counter)
    return o_win
