board_init = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
board_play_init = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal win
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical win
        (0, 4, 8), (2, 4, 6)              # Diagonal win
       ]


# Construct board game
def print_board(b):
    board = (f"{b[0]} | {b[1]} | {b[2]}\n"
             f"---------\n"
             f"{b[3]} | {b[4]} | {b[5]}\n"
             f"---------\n"
             f"{b[6]} | {b[7]} | {b[8]}")
    return board


# Check for winner
def check_winner(b):
    for win in win_conditions:
        if (b[win[0]] == b[win[1]] == b[win[2]]) and b[win[0]] != " ":
            print(f"Player '{b[win[0]]}' Wins!")
            return True


# No more moves and no winner
def check_tie(b):
    if " " not in b:
        print("It's a Tie.")
        return True


# Main function
def game():
    # Init
    print("Welcome to the TicTacToe.\n")
    print("This is layout of the board.")
    print("Use numbers 1-9 to select field.")
    print("Player 'X' is first and Player 'O' is second.\n")
    print(print_board(board_init) + "\n")

    # Start
    # Init variables
    board_play = board_play_init
    player_symbol = "X"
    game_over = False

    while not game_over:
        # Input a move 1-9
        move = input(f"Player {player_symbol} choose: ")
        # Validate input
        if move not in board_init:
            print("Invalid move. Only numbers 1-9 are allowed.")
        elif board_play[int(move) - 1] != " ":
            print("Field already occupied.")
        # Input is validated
        else:
            board_play[int(move) - 1] = player_symbol
            if player_symbol == "X":
                player_symbol = "O"
            else:
                player_symbol = "X"
            print("\n" + print_board(board_play) + "\n")
            # Check if game is won or no more moves available
            if check_winner(board_play):
                game_over = True
            elif check_tie(board_play):
                game_over = True

    again = input("Play again? (y/no = any other key): ")
    if again.upper() == "Y":
        game()


game()


