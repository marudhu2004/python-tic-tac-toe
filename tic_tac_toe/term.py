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