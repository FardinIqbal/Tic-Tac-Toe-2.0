from tictactoe.utils import validate_move, format_board

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        print(format_board(self.board))

    def get_move(self):
        while True:
            try:
                row = int(input(f"Player {self.current_player}, enter the row (0, 1, 2): "))
                col = int(input(f"Player {self.current_player}, enter the column (0, 1, 2): "))
                if validate_move(self.board, row, col):
                    self.board[row][col] = self.current_player
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Invalid input, please enter numbers.")

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

    def play(self):
        self.print_board()
        while True:
            self.get_move()
            self.print_board()
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                break
            if self.check_draw():
                print("It's a draw!")
                break
            self.switch_player()
