'''
Tic-Tac-Toe: Solution
Author: Sergio Benavides Reyes
'''

board = [
    "1","2","3",
    "4","5","6",
    "7","8","9"
]

playerone = "X"
champ = None
game = True



def main():
    while game:
        print_board(board)
        player(board)
        winner()
        playerchange()

def print_board(board):
    print (board[0] + "," + board[1] + "," + board[2])
    print (board[3] + "," + board[4] + "," + board[5])
    print (board[6] + "," + board[7] + "," + board[8]) 

def player(board):
    choose = int(input( f"{playerone}'s turn to choose a square (1-9): ")) 
    if choose >= 1 and choose <= 9:
        board[choose-1] = playerone

def playerchange():
    global playerone
    if playerone == "X":
        playerone = "O"
    else: playerone = "X"


def winnerhorizont(board):
    global champ
    if board[0] ==  board[1] == board[2]:
        champ = board[0]
        return True
    elif board[3] ==  board[4] == board[5]:
        champ = board[3]
        return True
    elif board[6] ==  board[7] == board[8]:
        champ = board[6]
        return True

def winnercolum(board):
    global champ
    if board[0] ==  board[3] == board[6]:
        champ = board[0]
        return True
    elif board[1] ==  board[4] == board[7]:
        champ = board[1]
        return True

    elif board[2] ==  board[5] == board[8]:
        champ = board[2]
        return True

def winnerdiag(board):
    global champ
    if board[0] ==  board[4] == board[8]:
        champ = board[0]
        return True
    elif board[2] ==  board[4] == board[6]:
        champ = board[2]
        return True

def winner():
    global game
    if winnercolum(board) or winnerdiag(board) or winnerhorizont(board):
        print(f"Congratulation player {champ}")
        game = False

if __name__ == "__main__":
    main()