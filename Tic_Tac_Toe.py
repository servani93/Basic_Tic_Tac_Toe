# players playing Tic-Tac-Toe
player1 = input("player1 name:")
player2 = input("player2 name:")
    
print()
print(player1, "vs", player2,":", "Let's play Tic-Tac-Toe")
print()

# Tic-Tac-Toe board
def display_board(board):
    for i in range(3):
        if i < 2:
            print("_", end="")
        else:
            print(" ", end="")
            
        print("|".join(board[i*3:(i+1)*3]), end="")
        
        if i < 2:
            print("_")

# board Initiation
def create_board():
    return ['_' if _ < 6 else ' ' for _ in range(9)]


def check_winner(board):
    # Winning combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for line in win_conditions:
        if board[line[0]] == board[line[1]] == board[line[2]] and ((board[line[0]] != ' ') and (board[line[0]] != '_')):
            return board[line[0]]
    return None

def is_draw(board):
    return ' ' not in board and '_' not in board


# Main game loop
def tic_tac_toe(player1, player2):
    board = create_board()
    display_board(board)

    while True:
        # player1's turn
        print()
        print()
        player1_move = int(input(f"{player1}'s move(0-8)"))
        while board[player1_move] != ' ' and board[player1_move] != '_':
            print("Position Occupied, give another Input")
            player1_move = int(input(f"{player1}'s move(0-8)"))
        print()
        if board[player1_move] == ' ':
            board[player1_move] = 'X'
        elif board[player1_move] == '_':
            board[player1_move] = 'X'

        display_board(board)

        if check_winner(board) == "X":
            print()
            print(f"{player1} won! congratulations!")
            break
        elif check_winner(board) == "O":
            print()
            print(f"{player2} won! congratulations!")
            break
        if is_draw(board):
            print()
            print("It's a draw!")
            break
    
    
        # player2's turn
        print()
        print()
        player2_move = int(input(f"{player2}'s move(0-8)"))
        while board[player2_move] != ' ' and board[player2_move] != '_':
            print("Position Occupied, give another Input")
            player2_move = int(input(f"{player2}'s move(0-8)"))
        print()
        if board[player2_move] == ' ':
            board[player2_move] = 'O'
        elif board[player2_move] == '_':
            board[player2_move] = 'O'

        display_board(board)

        if check_winner(board) == "X":
            print()
            print(f"{player1} won! congratulations!")
            break
        elif check_winner(board) == "O":
            print()
            print(f"{player2} won! congratulations!")
            break
        if is_draw(board):
            print()
            print("It's a draw!")
            break


tic_tac_toe(player1, player2)