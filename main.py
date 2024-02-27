import tic_tac_toe.term as term 
from tic_tac_toe.board import Board
from tic_tac_toe.util import *

from game_ai.beginner import Beginner

while True:
    
    term.banner()

    if input("(h for help, enter to continue) ").lower() == 'h':
        term.help()

    # Choose game mode
    mode = term.game_mode_select()

    if mode == 'c':
        level = term.ai_level_select()
        ai_player = not term.player_select()
        ai = Beginner(ai_player)
        
    player = term.first_player_select()
    board = Board(player)

    # Playing the game
    while True:

        # Letting ai play mode if its selected
        if board.player == ai.player:
            print(f"{'X' if board.player else 'O'} playing a move")
            board.make_move(ai.make_move(board))

        # Player playing the move
        else:
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