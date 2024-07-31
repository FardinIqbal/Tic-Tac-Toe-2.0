def validate_move(board, row, col):
    """
    Validates whether a move is valid (i.e., within bounds and on an empty spot).

    Parameters:
    board (list): The game board.
    row (int): The row number.
    col (int): The column number.

    Returns:
    bool: True if the move is valid, False otherwise.
    """
    if row in range(3) and col in range(3) and board[row][col] == ' ':
        return True
    return False


def format_board(board):
    """
    Formats the board into a string for better display.

    Parameters:
    board (list): The game board.

    Returns:
    str: Formatted string representing the board.
    """
    board_str = "  0 1 2\n"
    for idx, row in enumerate(board):
        board_str += f"{idx} {' '.join(row)}\n"
    return board_str
