def check_tic_tac_toe_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            if board[i][0] == 1:
                return "First player won"
            else:
                return "Second player won"
        if board[0][i] == board[1][i] == board[2][i] != 0:
            if board[0][i] == 1:
                return "First player won"
            else:
                return "Second player won"

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        if board[0][0] == 1:
            return "First player won"
        else:
            return "Second player won"
    if board[0][2] == board[1][1] == board[2][0] != 0:
        if board[0][2] == 1:
            return "First player won"
        else:
            return "Second player won"

    # If no winner and the board is full, it's a draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return "Draw!"

    # If no winner and the board is not full, the game is still ongoing
    return "Ongoing"


# Example usage
board = [[1, 2, 1], [2, 1, 2], [2, 1, 1]]
result = check_tic_tac_toe_winner(board)
print(result)
