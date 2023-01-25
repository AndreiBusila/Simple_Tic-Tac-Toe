board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


def verify_win(sign):
    return (board[0][0] is sign and board[0][1] is sign and board[0][2] is sign) \
        or (board[1][0] is sign and board[1][1] is sign and board[1][2] is sign) \
        or (board[2][0] is sign and board[2][1] is sign and board[2][2] is sign) \
        or (board[0][0] is sign and board[1][0] is sign and board[2][0] is sign) \
        or (board[0][1] is sign and board[1][1] is sign and board[2][1] is sign) \
        or (board[0][2] is sign and board[1][2] is sign and board[2][2] is sign) \
        or (board[0][0] is sign and board[1][1] is sign and board[2][2] is sign) \
        or (board[2][0] is sign and board[1][1] is sign and board[0][2] is sign)


def verify_draw():
    number_space = 0
    for i in board:
        for j in i:
            if j == " ":
                number_space += 1
    return number_space == 0


def print_board():
    print("---------")
    for i in board:
        print("|", end=" ")
        for j in i:
            print(j, end=" ")
        print("|")
    print("---------")


def main():
    print_board()
    player_turn = "X"
    while True:
        try:
            coord = [int(x) - 1 for x in input().split(" ")]
            if 0 <= coord[0] <= 2 and 0 <= coord[1] <= 2:
                if board[coord[0]][coord[1]] == " ":
                    board[coord[0]][coord[1]] = player_turn
                    print_board()
                    if verify_win(player_turn):
                        print("{0} wins".format(player_turn))
                        break
                    elif verify_draw():
                        print("Draw")
                        break
                    else:
                        if player_turn == "X":
                            player_turn = "O"
                        else:
                            player_turn = "X"
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")


main()
