from utils import check_winner,possible

def minimax(board,depth,isMax,opponent,player):
    score=check_winner(board)
    if score==10:
        return score - depth
    if score==-10:
        return score+depth
    if not possible(board):
        return 0
    
    if isMax:
        best=-1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=="":
                    if player=='X':
                        board[i][j]=player
                    else:
                        board[i][j]=opponent
                    best=max(best,minimax(board,depth+1,not isMax,opponent,player))
                    board[i][j]=""
        return best
    else:
        best=1000
        for i in range(3):
            for j in range(3):
                if board[i][j]=="":
                    if player=='O':
                        board[i][j]=player
                    else:
                        board[i][j]=opponent
                    best = min(best,minimax(board,depth+1,not isMax,opponent,player))
                    board[i][j] = ""
        return best