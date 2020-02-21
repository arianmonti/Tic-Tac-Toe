'''Hi! This program is a simple 2_player Tic-Tac-Toe 
   without graphical environment
'''

table, a, counter = [], [], 0
win = ((0, 1, 2),(0, 3, 6),(2, 4, 6),
       (3, 4, 5),(1, 4, 7),(2, 5, 8),          
       (6, 7, 8),(0, 4, 8))

import functions as f

for i in range(1, 10): table.append(i) # Add elements to table
f.Print_logo()

def main(counter):
    try:
        while True:
            f.Print_table(table)
            player_X = (int(input("Player X : ")) - 1)
            table[player_X] = "X"
            a.append(player_X)
            counter += 1
            if f.check_tk(a) == True : break
            if f.check_x_win(table, counter, main, a, win) == True : break
            if f.check_tie(counter, table, main, a) == True : break
            f.Print_table(table)
            player_O = (int(input("Player O : ")) - 1)
            table[player_O] = "O"
            a.append(player_O)
            counter += 1
            if f.check_tk(a) == True : break
            if f.check_o_win(table, counter, main, a, win) == True : break
            if f.check_tie(counter, table, main, a) == True : break
        
    except: print("Error")
main(counter)
quit = input()
