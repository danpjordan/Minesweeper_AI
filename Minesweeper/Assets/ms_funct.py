# Minesweeper functions
# Inspired from Microsoft Minesweeper
# Can be run in terminal

import random


def print_board(board, width, height):
    """Prints the board to the console"""

    print("\n   ", end="")
    for i in range(width):
        if i < width - 1:
            print("{} ".format(i % 10), end="")
        else:
            print("{}".format(i % 10), end="")
    print("\n")
    for i in range(height):
        print("{}  ".format(i % 10), end="")
        for j in range(width):
            if j < width - 1:
                print("{} ".format(board[i][j]), end="")
            else:
                print("{}".format(board[i][j]), end="")
        print()
    print()


def fill_game_board(g_board, width, height, mines):
    """Places the mines and numbers on the game board"""

    # Places the mines the game_board and records where each mine is located
    mine_postition = []
    for i in range(mines):
        row = random.randrange(0, height)
        col = random.randrange(0, width)
        while (g_board[row][col] != "*"):
            row = random.randrange(0, height)
            col = random.randrange(0, width)
        g_board[row][col] = "X"
        mine_postition.append([row, col])

    # Iterates through the mines and adds 1 to each surrounding tiles that is not a mine
    for mine in mine_postition:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    row = mine[0] - 1 + i
                    col = mine[1] - 1 + j
                    if row >= 0 and col >= 0 and row < height and col < width:
                        if g_board[row][col] == "*":
                            g_board[row][col] = 0
                        if g_board[row][col] != "X":
                            g_board[row][col] += 1


def expose_digits(g_board, u_board, width, height):
    """Exposes the digits that surround a blank tile"""

    for i in range(height):
        for j in range(width):
            if u_board[i][j] == "-":
                for k in range(3):
                    row = i - 1
                    col = j - 1 + k
                    if row >= 0 and col >= 0 and row < height and col < width:
                        if u_board[row][col] == "*":
                            u_board[row][col] = g_board[row][col]
                for k in range(0, 3, 2):
                    row = i
                    col = j - 1 + k
                    if row >= 0 and col >= 0 and row < height and col < width:
                        if u_board[row][col] == "*":
                            u_board[row][col] = g_board[row][col]
                for k in range(3):
                    row = i + 1
                    col = j - 1 + k
                    if row >= 0 and col >= 0 and row < height and col < width:
                        if u_board[row][col] == "*":
                            u_board[row][col] = g_board[row][col]


def discover_blanks(g_board, u_board, x, y, width, height):
    """Discovers the blank tiles that surround other blank tiles"""

    for k in range(3):
        for l in range(3):
            if k == 1 or l == 1:
                row = x - 1 + k
                col = y - 1 + l
                if row >= 0 and col >= 0 and row < height and col < width:
                    if g_board[row][col] == "*" and u_board[row][col] == "*":
                        u_board[row][col] = "-"
                        discover_blanks(g_board, u_board, row,
                                        col, width, height)


def check_win(u_board, width, height, mines):
    """Checks if the user has revealed all non-mine tiles and placed a flag over all mine tiles"""

    solved_count = 0
    flag_count = 0
    for i in range(height):
        for j in range(width):
            if u_board[i][j] != "*":
                solved_count += 1
    for i in range(height):
        for j in range(width):
            if u_board[i][j] == "F":
                flag_count += 1
    if solved_count == height * width and flag_count == mines:
        return True
    else:
        return False


def make_move(g_board, u_board, x, y, width, height):
    """Attempts to reveals the tile at position x, y. Returns true if a mine is revealed"""

    if x >= 0 and y >= 0 and x < height and y < width:
        if u_board[x][y] == "F":
            return False
        elif u_board[x][y] == "*":
            if g_board[x][y] == "X":
                u_board[x][y] = "X"
                return True
            else:
                if g_board[x][y] != "*":
                    u_board[x][y] = g_board[x][y]
                    return False
                else:
                    discover_blanks(g_board, u_board, x, y, width, height)
                    expose_digits(g_board, u_board, width, height)
                    return False
        else:
            return False
    else:
        print("Invalid move")
        return False


def flag(u_board, x, y, width, height):
    """Attempts to place a flag at position x, y."""

    if x >= 0 and y >= 0 and x < height and y < width:
        if u_board[x][y] == "F":
            u_board[x][y] = "*"
            return True
        elif u_board[x][y] == "*":
            u_board[x][y] = "F"
            return False
        return False
    else:
        print("Invlaid Move")
        return False


def get_mines_left(u_board, mines):
    """Returns the number of total mines minus the number of flags the user has placed"""

    flags = 0
    for row in u_board:
        for col in row:
            if col == "F":
                flags += 1
    return mines - flags


def reveal_mines(g_board, u_board, width, height):
    """Reveals all mines"""

    for i in range(height):
        for j in range(width):
            if g_board[i][j] == "X":
                u_board[i][j] = "X"


def hint(g_board, u_board, width, height, mines):
    """Reveals a random tile that is not a mine or removes a misplaced flag"""

    remaining_spaces = 0
    for i in range(height):
        for j in range(width):
            if u_board[i][j] == "*" or (u_board[i][j] == "F" and g_board[i][j]):
                remaining_spaces += 1
    if remaining_spaces > mines:
        x = random.randrange(0, height)
        y = random.randrange(0, width)
        update = False
        while g_board[x][y] == "X" or u_board[x][y] != "*":
            x = random.randrange(0, height)
            y = random.randrange(0, width)
            if u_board[x][y] == "F" and g_board[x][y] != "X":
                u_board[x][y] = "*"
                update = True
        if not update:
            make_move(g_board, u_board, x, y, width, height)
        return update
    return False


def main():
    """Runs minesweeper"""

    # Initializes some variables
    WIDTH = 10
    HEIGHT = 10
    DIFFCULTY = 1
    MINES = int(WIDTH * HEIGHT * (0.05 + 0.05 * DIFFCULTY))

    # Initializes the game board and display board
    game_board = [["*" for i in range(WIDTH)] for j in range(HEIGHT)]
    user_board = [["*" for i in range(WIDTH)] for j in range(HEIGHT)]

    # Places the mines and numbers on the game board
    fill_game_board(game_board, WIDTH, HEIGHT, MINES)

    # print_board(game_board, WIDTH, HEIGHT) # Used to display where mines are for testing

    # Prints display
    print("You are playing with {} mines".format(MINES), end="")
    print()
    print_board(user_board, WIDTH, HEIGHT)

    y = ""
    x = ""
    run = True

    # Uses input validation to determine if the user wants to quit
    print("Enter your first move (q to quit) (f to flag) (h for hint)")
    y = input("Down: ")
    if y != "q" and y != "f" and y != "h":
        x = input("Right: ")

    # Runs until the user wants to quit or they have lost/won the game
    while y != "q" and x != "q" and run:
        if y == "f" or x == "f":
            print("\nEnter a flag")
            y = input("Down: ")
            x = input("Right: ")
            try:
                # If valid tile, a flag is placed
                flag(user_board, int(y), int(x), WIDTH, HEIGHT)
            except ValueError:
                print("Invlaid Input")
        #  The game reveals a random tile that is not a mine or removes a misplaced flag
        elif y == "h" or x == "h":
            hint(game_board, user_board, WIDTH, HEIGHT, MINES)
        else:
            # If valid tile, the move is attempted and if the user revealed a mine the loop stops
            try:
                run = not make_move(game_board, user_board,
                                    int(y), int(x), WIDTH, HEIGHT)
            except ValueError:
                print("Invlaid Input")

        # Displays if the user won or lost the game if the game has ended
        if check_win(user_board, WIDTH, HEIGHT, MINES):
            print_board(game_board, WIDTH, HEIGHT)
            print("You won!")
            run = False
        elif not run:
            reveal_mines(game_board, user_board, WIDTH, HEIGHT)
            print_board(user_board, WIDTH, HEIGHT)
            print("Game Over!")

        # Asks the user for their next input if the game has not ended
        if run:
            print_board(user_board, WIDTH, HEIGHT)
            print("Enter your next move (q to quit) (f to flag) (h for hint)")
            y = input("Down: ")
            if y != "q" and y != "f" and y != "h":
                x = input("Right: ")


if __name__ == '__main__':
    main()
