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





