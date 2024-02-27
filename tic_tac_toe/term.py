import errors

def help():
    print("If you don't know how to play the game, google it!")
    print("""there is a 3x3 grid where you face your opponent
          and try and get 3 x or o on the same row, column or diagonal
          you take turns with the other player trying to outwit each other
          .If the board is full without a winner, consider it a draw""")
    

def banner():
    print("Welcome to Tic Tac Toe.")
    print("[x][o][x]")
    print("[o][x][x]")
    print("[o][o][o]")
    print("Developed by Marudhu2004 and Siddharth Tantri")


def print_board(x):

    row_1 = x[0:3]
    row_2 = x[3:6]
    row_3 = x[6:9]
    print()
    print(f"[ {row_1[0]} ][ {row_1 [1]} ][ {row_1 [2]} ]")
    print(f"[ {row_2[0]} ][ {row_2 [1]} ][ {row_2 [2]} ]")
    print(f"[ {row_3[0]} ][ {row_3 [1]} ][ {row_3 [2]} ]")
    print()


print_board([1,2,3,4,5,6,7,8,9])


def print_over():
    print("The board is full, the game is a draw. Play Again if you want to. ")
    


def print_winner(x):
    print(f"Congrats! {x} is the winner. ")

    again = input("Do you want to play again?")

def game_mode_select():
    
    difficulty = input("What difficulty would you like to play on? Beginner or Advanced Mode? : ")
    if difficulty == "Beginner":
        print("Welcome to Beginner Mode")
    elif difficulty == "Advanced":
        print("So you would like a challenge hmmm....????? Alright, suit yourself. WELCOME TO ADVANCED MODE.")
    else:
        print("Please enter a valid difficulty, not random information. ")

    
def play_again():
      again = input("Would you like to play again?")

def first_player_select():
    user_input = input("Who would like to go first? x or y? :  ")
    if user_input == "x":
        print("X goes first! make the first move!: ")
    elif user_input ==  "y":
        print ("Y goes first! make the first move!: ")
    else:
        print("Please enter a valid player name. ")


def parse_position(board):
    
    while True:
        try:
            move = int(input("Enter your move: "))
            board.make_move(move)
            break
        except (errors.IllegalMove, ValueError):
            print("bad move, try again")
