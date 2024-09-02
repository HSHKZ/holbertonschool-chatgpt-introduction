#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)  # Corrected to match the board's width


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please try again.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        board[row][col] = player
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("The game is a draw!")
            break
        player = "O" if player == "X" else "X"


tic_tac_toe()
