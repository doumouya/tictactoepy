import random


board = [
        ['1', '2', '3'],
        ['4', 'X', '6'],
        ['7', '8', '9']
        ]
          
pos_dispos = ['1', '2', '3', '4', '6', '7', '8', '9']

class Player:
    def __init__(self, pseudo, sign):
        self.pseudo = pseudo
        self.sign = sign

    def chose_pos(self, li_dispos = pos_dispos):
        if self.pseudo == 'user':
            choice = input('Choisissez une position\n')
            while choice not in li_dispos:
                choice = input('Choisissez une position available\n>')
            return choice
        return random.choice(li_dispos)

comp = Player('comp', 'X')
user = Player('user', 'O')

winner = False

def print_table(board):
    print(
        f"""
        [{board[0][0]}][{board[0][1]}][{board[0][2]}]
        [{board[1][0]}][{board[1][1]}][{board[1][2]}]
        [{board[2][0]}][{board[2][1]}][{board[2][2]}]

        Available position(s)
        {pos_dispos}
        """
        )

def check_row(test_table):
    global winner
    if test_table[0] == test_table[1] and test_table[1] == test_table[2]:
        print(test_table[0], 'win!')
        winner = True
        return True
    else:
        return False

def check_board(board):
    row_table =[]
    col_table =[]
    diag_table =[]
    
    for i in range(3):
        row_table = board[i]
        if check_row(row_table) == False:
            continue
        else:
            return True
            
    if check_row(row_table) == False:
        for j in range(3):
            col_table = [board[0][j], board[1][j], board[2][j]]
            if check_row(col_table) == False:
                continue
            if check_row(row_table):
                return True
                
    if check_row(col_table) == False:
        diag_table = [board[0][0], board[1][1], board[2][2]]
        if check_row(diag_table) == False:
            diag_table = [board[2][0], board[1][1], board[0][2]]
        if check_row(diag_table):
            return True
    
    return False

def play_game(player = 'comp', choice = 5, board = board, li_dispos = pos_dispos):
    found_pos = False
    for i in range(3):
        if found_pos == False:
            for j in range(3):
                if found_pos == False:
                    if board[i][j] == choice:
                        li_dispos.remove(choice)
                        if player == 'user' and winner == False:
                            board[i][j] = user.sign
                        else:
                            board[i][j] = comp.sign
                        found_pos = True
                
def launch_game(i):
    if i%2 == 0:
        choice = comp.chose_pos()
        player = comp.pseudo
    else: 
        choice = user.chose_pos()
        player = user.pseudo
    play_game(player = player, choice = choice)

def main():
    i = 1
    play_game()
    print_table(board)
    score = False
    while len(pos_dispos)>=0 and winner == False:
        score = check_board(board)
        if score == False:
            launch_game(i)
            print_table(board)
            i+=1
    if len(pos_dispos) == 0 and winner == False:
        print('DRAW')

main()