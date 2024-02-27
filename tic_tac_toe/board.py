import errors

class Board:

    def __init__(self, player: bool) -> None:
        self.board = [0 for _ in range(9)]
        self.player = player

    def make_move(self, move):
        
        if not 0 <= move <= 8 and move not in self.list_free_moves():
            raise errors.IllegalMove
        
        self.board[move] = 1 if self.player else -1
        self.player = not self.player

    def list_free_moves(self):
        return [x for x in self.board if x == 0]

    def has_winner(self):
        
        # Checking rows
        rows = False
        for i in range(0, 9, 3):
            if self.board[i + 0] == self.board[i + 1] == self.board[i + 2]:
                rows = True

        # Checking columns
        columns = False
        for i in range(0, 9, 3):
            if self.board[i + 0] == self.board[i + 3] == self.board[i + 6]:
                columns = True

        # Checking diagonals
        diagonals = self.board[0] == self.board[4] == self.board[8] or \
                    self.board[2] == self.board[4] == self.board[6]
        
        return rows or columns or diagonals
    
    def game_over(self):
        return self.has_winner() or self.list_free_moves() == []

    def get_player(self):
        pass

    def get_board(self):
        pass

    def make_copy(self):
        pass