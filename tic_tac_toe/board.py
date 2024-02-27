import errors

class Board:

    def __init__(self, player: bool) -> None:
        self.board = [0 for _ in range(9)]
        self.player = player

    def make_move(self, move):
        
        if not 0 <= move <= 8 and move not in self.list_free_moves():
            raise errors.IllegalMove
        
        self.board[move] = 1 if self.player else 2
        self.player = not self.player
        

    def list_free_moves(self):
        return [x for x in self.board if x == 0]

    def has_winner(self):
        pass

    def game_over(self):
        pass

    def get_player(self):
        pass

    def get_board(self):
        pass

    def make_copy(self):
        pass