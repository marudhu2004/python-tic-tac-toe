class Board:

    def __init__(self, player: bool) -> None:
        self.board = [0 for _ in range(9)]
        self.player = player

    def make_move(self, move):
        pass

    def list_free_moves(self):
        pass

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