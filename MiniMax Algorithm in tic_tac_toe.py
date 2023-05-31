from typing import List, Tuple


board: List[List[str]] = [['-', '-', '-'],
                          ['-', '-', '-'],
                          ['-', '-', '-']]

	
def check_win(board: List[List[str]], player: str) -> bool:
    """
    Check if a player has won the game.

    Args:
        board: The current state of the Tic-Tac-Toe board.
        player: The player to check for a win ('X' or 'O').

    Returns:
        True if the player has won, False otherwise.
    """
    
    for i in range(3): # Check rows
        if all(board[i][j] == player for j in range(3)):
            return True

    for j in range(3): # Check columns
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def game_over(board: List[List[str]]) -> bool:
    """
    Check if the game is over.

    Args:
        board: The current state of the Tic-Tac-Toe board.

    Returns:
        True if the game is over, False otherwise.
    """
    return check_win(board, 'X') or check_win(board, 'O') or all(board[i][j] != '-' for i in range(3) for j in range(3))

def evaluate(board: List[List[str]]) -> int:
    """
    Evaluate the current state of the board.

    Args:
        board: The current state of the Tic-Tac-Toe board.

    Returns:
        1 if 'X' wins, -1 if 'O' wins, 0 if it's a draw.
    """
    if check_win(board, 'X'):
        return 1  # X wins
    elif check_win(board, 'O'):
        return -1  # O wins
    else:
        return 0  # It's a draw

def minimax(board: List[List[str]], depth: int, maximizing_player: bool) -> int:
    """
    Perform the minimax algorithm to determine the best move for a player.

    Args:
        board: The current state of the Tic-Tac-Toe board.
        depth: The current depth of the minimax search.
        maximizing_player: True if the player is maximizing, False if minimizing.

    Returns:
        The evaluation score of the board state.
    """
    if game_over(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval_score = minimax(board, depth - 1, False)
                    board[i][j] = '-'
                    max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval_score = minimax(board, depth - 1, True)
                    board[i][j] = '-'
                    min_eval = min(min_eval, eval_score)
        return min_eval

def make_move(board: List[List[str]]) -> None:
    """
    Make the best move for the maximizing player using the minimax algorithm.

    Args:
        board: The current state of the Tic-Tac-Toe board.
    """
    best_eval = float('-inf')
    best_move: Tuple[int, int] = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                eval_score = minimax(board, 9, False)
                board[i][j] = '-'
                if eval_score > best_eval:
                    best_eval = eval_score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = 'X'

def print_board(board: List[List[str]]) -> None:
    """
    Print the current state of the Tic-Tac-Toe board.

    Args:
        board: The current state of the Tic-Tac-Toe board.
    """
    for row in board:
        print(' '.join(row))
    print()

# Play the game
while not game_over(board):
    print_board(board)
    make_move(board)
    if not game_over(board):
        print_board(board)
        user_row = int(input("Enter the row (0-2): "))
        user_col = int(input("Enter the column (0-2): "))
        board[user_row][user_col] = 'O'

print_board(board)
if check_win(board, 'X'):
    print("You lost!")
elif check_win(board, 'O'):
    print("You won!")
else:
    print("It's a draw!")
