import random

player='O'
opponent='X'
isMax=False


# Choosing which player is 'O' and 'X' randomly
def choose():
    global opponent,player,isMax
    num=random.randint(0,1)
    if num==0:
        opponent='O'
        player='X'
        isMax=True
    elif num==1:
        opponent='X'
        player='O'
        isMax=False
    return opponent,player,isMax

# Checking the winner


def check_winner(b):
    # Checking for Rows for X or O victory.
    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2] != '':
            if b[row][0] == player:
                return 10
            elif b[row][0] == opponent:
                return -10
                
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != '':
            if b[0][col] == player:
                return 10
            elif b[0][col] == opponent:
                return -10

    # Checking for Diagonals for X or O victory.
    if b[0][0] == b[1][1] == b[2][2] != '':
        if b[0][0] == player:
            return 10
        elif b[0][0] == opponent:
            return -10

    if b[0][2] == b[1][1] == b[2][0] != '':
        if b[0][2] == player:
            return 10
        elif b[0][2] == opponent:
            return -10

    # If none of the winning conditions are met, return 0 (game still ongoing)
    return 0

#Check whether there is a move to make
def possible(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                return True
    return False