# game/game_logic.py

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        return "\n".join([" ".join(row) for row in self.board])

    def get_move(self, row, col):
        if self.validate_move(row, col):
            self.board[row][col] = self.current_player
            if self.check_winner():
                return f"Player {self.current_player} wins!"
            if self.check_draw():
                return "It's a draw!"
            self.switch_player()
            return None
        else:
            return "Invalid move, try again."

    def validate_move(self, row, col):
        return row in range(3) and col in range(3) and self.board[row][col] == ' '

    def check_winner(self):
        for i in range(3):
            if all([self.board[i][j] == self.current_player for j in range(3)]) or \
               all([self.board[j][i] == self.current_player for j in range(3)]):
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True
        return False

    def check_draw(self):
        return all([cell != ' ' for row in self.board for cell in row])

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
