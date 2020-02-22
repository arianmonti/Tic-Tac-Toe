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
    for i in range(1, 10): table.append(i) # add nine elements to table

def Print_table(table): # print tic-tac-toe table
    print(table[0], "|" , table[1], "|", table[2])
    print(table[3], "|" , table[4], "|", table[5])
    print(table[6], "|" , table[7], "|", table[8])

def check_tie(counter, table, main, a): # check if game tied or not
    tied = False
    if counter == 9: tied = True
    if (tied == True): 
        Print_table(table)
        print("Tied")
        ask = input("Do you want to play again?(Y/n) ")
        ask = ask.upper()
        if (ask == 'Y'):
            reset_table(table, counter, a)
            main(counter)
    return tied

def check_tk(a): # check if player o enter same number or not
    b = False
    for i in range(0, 9): 
        if (a.count(i) > 1): b = True
    if b == True: print("Error")
    return b

def check_x_win(table, counter, main, a, win): # check if x win or not
    x_won = False
    for win_check in win:
        if table[win_check[0]] == "X" and table[win_check[1]] == "X" and table[win_check[2]] == "X":
           x_won = True
    if x_won == True:
        Print_table(table)
        print("X win")
        ask = input("Do you want to play again?(Y/n) ")
        ask = ask.upper()
        if (ask == 'Y'):
            reset_table(table, counter, a)
            main(counter)
    return x_won

def check_o_win(table, counter, main, a, win): # check if o win or not
    o_win = False
    for win_check in win:
        if table[win_check[0]] == "O" and table[win_check[1]] == "O" and table[win_check[2]] == "O":
            o_win = True
    if o_win == True:
        Print_table(table)
        print("O win")
        ask = input("Do you want to play again?(Y/n) ")
        ask = ask.upper()
        if (ask == 'Y'):
            reset_table(table, counter, a)
            main(counter)
    return o_win

