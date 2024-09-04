#!/usr/bin/python3
def print_board(board):
    """
    Print the current state of the tic-tac-toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the tic-tac-toe board.
    """
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Check if the game is a draw (i.e., the board is full and there is no winner).
    """
    for row in board:
        if " " in row:
            return False
    return not check_winner(board)

def tic_tac_toe():
    """
    Play a game of tic-tac-toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print("Player " + player + "'s turn.")
        
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input. Row and column must be 0, 1, or 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter integers only.")
        
        board[row][col] = player
        
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
