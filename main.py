import tic_tac_toe.term as term 
from tic_tac_toe.board import Board
from tic_tac_toe.util import *

while True:
    
    term.banner()

    if input("(h for help, enter to continue)").lower() == 'h':
        term.help()

    player = term.first_player_select()
    board = Board(player)

    # Playing the game
    while True:

        term.print_board(parse_positions(board))
        term.parse_position(board)

        if board.game_over():
            term.print_board(parse_positions(board))
            
            if board.has_winner():
                term.print_winner('X' if board.get_winner() == 1 else 'O')
            
            else:
                print("the game is tied.")
            break
    
    if not term.play_again():
        break