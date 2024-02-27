from . import errors


def help():
    print("If you don't know how to play the game, google it!\n")
    print("""   there is a 3x3 grid where you face your opponent
    and try and get 3 x or o on the same row, column or diagonal
    you take turns with the other player trying to outwit each other.
    If the board is full without a winner, consider it a draw""")
    input()
    

def banner():
    print("\nWelcome to Tic Tac Toe.\n")
    print("[x][o][x]")
    print("[o][x][x]")
    print("[o][o][o]\n")
    print("Developed by Marudhu2004 and Siddharth Tantri\n")


def print_board(x):

    row_1 = x[0:3]
    row_2 = x[3:6]
    row_3 = x[6:9]
    print()
    print(f"[ {row_1[0]} ][ {row_1 [1]} ][ {row_1 [2]} ]")
    print(f"[ {row_2[0]} ][ {row_2 [1]} ][ {row_2 [2]} ]")
    print(f"[ {row_3[0]} ][ {row_3 [1]} ][ {row_3 [2]} ]")
    print()


def print_over():
    print("The board is full, the game is a draw. Play Again if you want to. ")


def print_winner(x):
    print(f"Congrats! {x} is the winner. ")


def game_mode_select():
    difficulty = input("What difficulty would you like to play on? Beginner or Advanced Mode? : ")
    if difficulty == "Beginner":
        print("Welcome to Beginner Mode")
    elif difficulty == "Advanced":
        print("So you would like a challenge hmmm....????? Alright, suit yourself. WELCOME TO ADVANCED MODE.")
    else:
        print("Please enter a valid difficulty, not random information. ")

    
def play_again() -> bool:
    
    while True:
        c = input("Would you like to play again? (Y or N)").lower()
        if c in ('y', 'n'):
            return c == 'y'
        else:
            print("enter valid input!")
        


def first_player_select():
    
    while True:
        user_input = input("Who would like to go first? x or o? :  ").lower()
        
        if user_input == "x":
            print("X goes first!")
            return True
        
        elif user_input == "o":
            print ("O goes first!")
            return False
        
        else:
            print("Please enter a valid player (x or o).")


def parse_position(board):
    
    while True:
        try:
            move = int(input("Enter your move: "))
            board.make_move(move - 1)
            break
        except (errors.IllegalMove, ValueError):
            print("bad move, try again")
