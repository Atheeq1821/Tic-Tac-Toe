# Importation
from flask import Flask,render_template,jsonify
from utils import choose,check_winner,possible
from minimax import minimax
app = Flask(__name__)

board = [["","",""],["","",""],["","",""]]
player='O'
opponent='X'
isMax=False

def make_move(board):
    bestVal=-1000
    bestMove=(-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j]=="":
                board[i][j]=player
                moveVal=minimax(board,0,isMax,opponent=opponent,player=player)
                board[i][j]=""
                if moveVal>bestVal:
                    bestVal=moveVal
                    bestMove=(i,j)

    return bestMove

@app.route("/start")
def start():
    global board,opponent,player,isMax
    value=""
    board = [["","",""],["","",""],["","",""]]
    opponent,player,isMax=choose()
    if player=='X':
        move=make_move(board)
        board[move[0]][move[1]]=player
        value='X'
    return render_template('index.html', opponent=opponent, player=player,val=value)


#making the player move
@app.route('/move/<string:index>')
def move(index):
    global opponent, board
    if len(index)==1:
        i=0
    else:
        i=int(index[0])
    j = int(index[-1])
    if board[i][j] == '':
        board[i][j]=opponent
        winner = check_winner(board)
        if winner==-10:
            return jsonify({'cell_values': board, "oppo":True, "play": False , "tie": False})
        if not possible(board):
            return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": True})
    return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": False})

@app.route("/aiMove")
def aiMove():
    global board
    move = make_move(board)
    board[move[0]][move[1]]=player
    winner = check_winner(board)
    if winner==10:
            return jsonify({'cell_values': board, "oppo":False, "play": True , "tie": False})
    if not possible(board):
        return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": True})
    return jsonify({'cell_values': board, "oppo":False, "play": False , "tie": False})

#Routing to home.html
@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()