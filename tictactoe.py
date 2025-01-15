import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def bot_move(board):
    # Improved bot logic: Try to win or block the player
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

    # Check if the bot can win
    for row, col in empty_cells:
        board[row][col] = 'O'
        if check_winner(board) == 'O':
            return (row, col)
        board[row][col] = ' '

    # Block the player from winning
    for row, col in empty_cells:
        board[row][col] = 'X'
        if check_winner(board) == 'X':
            board[row][col] = ' '
            return (row, col)
        board[row][col] = ' '

    # If no immediate win or block, pick a random move
    return random.choice(empty_cells)

def get_player_input(board):
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                print(f"Player chose row {row}, column {col}")
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

def tic_tac_toe():
    print("Starting Tic Tac Toe...")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        if current_player == 'X':
            print("Player's turn")
            row, col = get_player_input(board)
        else:
            print("Bot's turn")
            row, col = bot_move(board)
            print(f"Bot chose row {row}, column {col}")

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
