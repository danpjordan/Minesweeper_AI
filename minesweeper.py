# Minesweeper
# Inspired from Microsoft Minesweeper
# Mine sweeper font by Gezoda
# Clock font by Style 7

import pygame
import ms_funct
import os
pygame.font.init()

# Defines the width and height in tiles of the game board
GAME_WIDTH_TILES = 15
GAME_HEIGHT_TILES = 15

# Defines the numbers of mines based on the board size and difficulty
DIFFICULTY = 1
MINES = int(GAME_WIDTH_TILES * GAME_HEIGHT_TILES * (0.05 + 0.05 * DIFFICULTY))

# Defines the width and height in pixels of the display board which appears above the game board
DISPLAY_HEIGHT = 70
DISPLAY_LINE_WIDTH = 15
SIZE_OF_SQUARE = 40
WIDTH_OF_BORDER = 15
MINE_BORDER = 2

# Defines the width and height in pixels of the board which consists of both the game board and display board
BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS = SIZE_OF_SQUARE * GAME_WIDTH_TILES + 2 * \
    WIDTH_OF_BORDER, SIZE_OF_SQUARE * GAME_HEIGHT_TILES + \
    DISPLAY_HEIGHT + 3 * WIDTH_OF_BORDER

# Defines the pixel, width and height, of where the game board starts
GAME_STARTING_HEIGHT = WIDTH_OF_BORDER + \
    WIDTH_OF_BORDER + DISPLAY_HEIGHT - MINE_BORDER // 2
GAME_STARTING_WIDTH = WIDTH_OF_BORDER - MINE_BORDER // 2

# Defines frams per second
FPS = 60

# Defines colors
LIGHT_GRAY = (200, 200, 200)
GRAY = (192, 192, 192)
DARK_GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (254, 0, 0)
BLUE = (1, 0, 255)
GREEN = (1, 127, 1)
DARK_BLUE = (0, 0, 127)
MAROON = (129, 1, 2)
TEAL = (0, 127, 126)
YELLOW = (255, 255, 0)

#Set random seed
ms_funct.set_random_seed(1)

# Defines fonts
NUMBER_FONT = pygame.font.Font(os.path.join(
    'Assets', 'ms_font.ttf'), 24)
DISPLAY_FONT = pygame.font.Font(os.path.join('Assets', 'clock_font.ttf'), 28)

# Defines events
HIT_MINE = pygame.USEREVENT + 1
FOUND_ALL_MINES = pygame.USEREVENT + 2
RESET = pygame.USEREVENT + 3
HINT = pygame.USEREVENT + 4


# Defines the width and hight in pixels of the window
WIN = pygame.display.set_mode((BOARD_WIDTH_PIXELS, BOARD_HEIGHT_PIXELS))
pygame.display.set_caption("minesweeper")


def draw_smile(smile):
    """Draws the smile in the display board"""

    # Defines the height in pixels of the center of the smile
    RADIUS_HEIGHT = WIDTH_OF_BORDER + WIDTH_OF_BORDER // 2 + \
        (DISPLAY_HEIGHT - WIDTH_OF_BORDER) // 2
    EYE_OFFSET = 7

    # Draws a yellow circle with a black boarder
    pygame.draw.circle(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 + 1,
                       RADIUS_HEIGHT + 1), (DISPLAY_HEIGHT - WIDTH_OF_BORDER) // 2 - 7)
    pygame.draw.circle(WIN, YELLOW, (BOARD_WIDTH_PIXELS // 2 + 1,
                       RADIUS_HEIGHT + 1), (DISPLAY_HEIGHT - WIDTH_OF_BORDER) // 2 - 9)

    # 0 is happy, 1 is sunglasses, 2 is dead
    if smile == 0:
        # Draws eyes
        pygame.draw.circle(WIN, BLACK, (BOARD_WIDTH_PIXELS //
                                        2 + 1 - EYE_OFFSET, RADIUS_HEIGHT - 4), 3)
        pygame.draw.circle(WIN, BLACK, (BOARD_WIDTH_PIXELS //
                                        2 + 1 + EYE_OFFSET, RADIUS_HEIGHT - 4), 3)

        # Draws the smile
        SMILE_RECT = pygame.Rect(BOARD_WIDTH_PIXELS //
                                2 - EYE_OFFSET, RADIUS_HEIGHT + 1, 16, 10)
        pygame.draw.arc(WIN, BLACK, SMILE_RECT, 3.1415, 2 * 3.1415 - 0.2, 1)
    elif smile == 1:
        # Draws the smile
        SMILE_RECT = pygame.Rect(BOARD_WIDTH_PIXELS // 
                                2 - EYE_OFFSET, RADIUS_HEIGHT + 1, 16, 10)
        pygame.draw.arc(WIN, BLACK, SMILE_RECT, 3.1415, 2 * 3.1415 - 0.2, 1)

        # Draws the sunglass lenses
        pygame.draw.circle(WIN, BLACK, (BOARD_WIDTH_PIXELS //
                                        2 + 1 - EYE_OFFSET, RADIUS_HEIGHT - 4), 5)
        pygame.draw.circle(WIN, BLACK, (BOARD_WIDTH_PIXELS //
                                        2 + 1 + EYE_OFFSET, RADIUS_HEIGHT - 4), 5)

        # Draws the sunglass frame
        pygame.draw.line(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 + 1 - EYE_OFFSET, RADIUS_HEIGHT - 9),
                         (BOARD_WIDTH_PIXELS // 2 + 1 + EYE_OFFSET, RADIUS_HEIGHT - 9), 2)
        pygame.draw.line(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 - 2 - EYE_OFFSET, RADIUS_HEIGHT - 9),
                         (BOARD_WIDTH_PIXELS // 2 - RADIUS_HEIGHT // 3 - 1, RADIUS_HEIGHT), 2)
        pygame.draw.line(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 + 3 + EYE_OFFSET, RADIUS_HEIGHT - 9),
                         (BOARD_WIDTH_PIXELS // 2 + RADIUS_HEIGHT // 3 + 1, RADIUS_HEIGHT), 2)
    elif smile == 2:
        # Draws the dead eyes
        LINE_SIZE = 2
        pygame.draw.line(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 + 1 - EYE_OFFSET - LINE_SIZE, RADIUS_HEIGHT - 6 + 1 -
                         LINE_SIZE), (BOARD_WIDTH_PIXELS // 2 + 1 - EYE_OFFSET + LINE_SIZE, RADIUS_HEIGHT - 6 + 1 + LINE_SIZE), 2)
        pygame.draw.line(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 + 1 - EYE_OFFSET + LINE_SIZE, RADIUS_HEIGHT - 6 + 1 -
                         LINE_SIZE), (BOARD_WIDTH_PIXELS // 2 + 1 - EYE_OFFSET - LINE_SIZE, RADIUS_HEIGHT - 6 + 1 + LINE_SIZE), 2)
        pygame.draw.line(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 - 1 + EYE_OFFSET - LINE_SIZE, RADIUS_HEIGHT - 6 + 1 -
                         LINE_SIZE), (BOARD_WIDTH_PIXELS // 2 - 1 + EYE_OFFSET + LINE_SIZE, RADIUS_HEIGHT - 6 + 1 + LINE_SIZE), 2)
        pygame.draw.line(WIN, BLACK, (BOARD_WIDTH_PIXELS // 2 - 1 + EYE_OFFSET + LINE_SIZE, RADIUS_HEIGHT - 6 + 1 -
                         LINE_SIZE), (BOARD_WIDTH_PIXELS // 2 - 1 + EYE_OFFSET - LINE_SIZE, RADIUS_HEIGHT - 6 + 1 + LINE_SIZE), 2)

        # Draws the frown
        FROWN_RECT = pygame.Rect(BOARD_WIDTH_PIXELS //
                                2 - EYE_OFFSET, RADIUS_HEIGHT + 4, 16, 10)
        pygame.draw.arc(WIN, BLACK, FROWN_RECT, 2 * 3.1415 - 0.2, 3.1415, 1)


def draw_display(num_mines_left, time, smile):
    """Draws the display board found above the game board"""

    # Defines the starting height in pixels of the display
    STARTING_HEIGHT_DISPLAY = WIDTH_OF_BORDER + WIDTH_OF_BORDER // 2

    # Defines the starting width in pixels of the mine counter, time counter, and hint display
    TIME_DISPLAY_STARTING_WIDTH = BOARD_WIDTH_PIXELS - 3 * SIZE_OF_SQUARE
    MINE_COUNT_DISPLAY_STARTING_WIDTH = int(1.5 * WIDTH_OF_BORDER)
    HINT_DISPLAY_STARTING_WIDTH = BOARD_WIDTH_PIXELS - int(6.85 * SIZE_OF_SQUARE) + WIDTH_OF_BORDER // 2

    # Defines the width in pixels of the time-mine, and hint display
    TIME_MINE_DISPLAY_WIDTH = 3 * SIZE_OF_SQUARE - int(1.5 * WIDTH_OF_BORDER)
    HINT_DISPLAY_WIDTH = 4 * SIZE_OF_SQUARE - int(2 * WIDTH_OF_BORDER)


    # Defines and draws the rectangles where the time, mine, and hint will be displayed
    DISPLAY_MINES = pygame.Rect(MINE_COUNT_DISPLAY_STARTING_WIDTH, STARTING_HEIGHT_DISPLAY,
                                TIME_MINE_DISPLAY_WIDTH,  DISPLAY_HEIGHT - WIDTH_OF_BORDER)
    DISPLAY_TIME = pygame.Rect(TIME_DISPLAY_STARTING_WIDTH, STARTING_HEIGHT_DISPLAY,
                                TIME_MINE_DISPLAY_WIDTH, DISPLAY_HEIGHT - WIDTH_OF_BORDER)
    DISPLAY_HINT = pygame.Rect(HINT_DISPLAY_STARTING_WIDTH, STARTING_HEIGHT_DISPLAY,
                                HINT_DISPLAY_WIDTH, DISPLAY_HEIGHT - WIDTH_OF_BORDER)
    
    pygame.draw.rect(WIN, BLACK, DISPLAY_MINES)
    pygame.draw.rect(WIN, BLACK, DISPLAY_TIME)
    pygame.draw.rect(WIN, BLACK, DISPLAY_HINT)
    

    # Seperates the time input into a ones, tens, and hundreds value and draws it into the time rectangle
    time_arr = time % 10, time // 10 % 10, time // 100 % 10
    for i in range(3):
        draw_text = DISPLAY_FONT.render(str(time_arr[2 - i]), 1, RED)
        WIN.blit(draw_text, (TIME_DISPLAY_STARTING_WIDTH + 4 + i *
                 (TIME_MINE_DISPLAY_WIDTH // 3), STARTING_HEIGHT_DISPLAY + 7))

    # Displays the word hint
    hint_text = 'HINT'
    for i in range(4):
        draw_text = DISPLAY_FONT.render(str(hint_text[i]), 1, RED)
        WIN.blit(draw_text, (HINT_DISPLAY_STARTING_WIDTH + 4 + i *
                 (TIME_MINE_DISPLAY_WIDTH // 3), STARTING_HEIGHT_DISPLAY + 7))


    # Seperates the number of mines left input into a ones, tens, and hundreds value and draws it into the mines rectangle
    # If the number of mines is less than 0, only the ones and tens places are consider and a negitive sign is placed in the hundreds place
    if (num_mines_left >= 0):
        num_mines_left_arr = num_mines_left % 10, num_mines_left // 10 % 10, num_mines_left // 100 % 10
        for i in range(3):
            draw_text = DISPLAY_FONT.render(
                str(num_mines_left_arr[2 - i]), 1, RED)
            WIN.blit(draw_text, (MINE_COUNT_DISPLAY_STARTING_WIDTH + 4 + i *
                     (TIME_MINE_DISPLAY_WIDTH // 3), STARTING_HEIGHT_DISPLAY + 7))
    else:
        num_mines_left_arr = -1 * num_mines_left % 10, -1 * \
            num_mines_left // 10 % 10, num_mines_left // 100 % 10
        draw_text = DISPLAY_FONT.render("-", 1, RED)
        WIN.blit(draw_text, (MINE_COUNT_DISPLAY_STARTING_WIDTH + 4,
                 STARTING_HEIGHT_DISPLAY + (DISPLAY_HEIGHT - WIDTH_OF_BORDER) // 2 - 2))
        for i in range(1, 3):
            draw_text = DISPLAY_FONT.render(
                str(num_mines_left_arr[2 - i]), 1, RED)
            WIN.blit(draw_text, (MINE_COUNT_DISPLAY_STARTING_WIDTH + 4 + i *
                     (TIME_MINE_DISPLAY_WIDTH // 3), STARTING_HEIGHT_DISPLAY + 7))

    # Defines and draws the rectangle for the smile / reset button
    RESET_BUTTON = pygame.Rect(BOARD_WIDTH_PIXELS // 2 - (DISPLAY_HEIGHT - WIDTH_OF_BORDER) // 2, WIDTH_OF_BORDER +
                               WIDTH_OF_BORDER // 2, DISPLAY_HEIGHT - WIDTH_OF_BORDER, DISPLAY_HEIGHT - WIDTH_OF_BORDER)
    pygame.draw.rect(WIN, LIGHT_GRAY, RESET_BUTTON)
    draw_smile(smile)

    pygame.display.update()


def draw_window():
    """Draws the window"""

    # Clears the window
    WIN.fill(WHITE)

    # Defines and draws the display board
    DISPLAY = pygame.Rect(WIDTH_OF_BORDER, WIDTH_OF_BORDER,
                          BOARD_WIDTH_PIXELS - WIDTH_OF_BORDER * 2, DISPLAY_HEIGHT)
    pygame.draw.rect(WIN, GRAY, DISPLAY)

    # Defines and draws a border around the edges of the window and display
    TOP_BORDER = pygame.Rect(0, 0, BOARD_WIDTH_PIXELS, WIDTH_OF_BORDER)
    LEFT_BORDER = pygame.Rect(0, 0, WIDTH_OF_BORDER, BOARD_HEIGHT_PIXELS)
    BOTTOM_BORDER = pygame.Rect(
        0, BOARD_HEIGHT_PIXELS - WIDTH_OF_BORDER, BOARD_WIDTH_PIXELS, WIDTH_OF_BORDER)
    RIGHT_BORDER = pygame.Rect(
        BOARD_WIDTH_PIXELS - WIDTH_OF_BORDER, 0, WIDTH_OF_BORDER, BOARD_HEIGHT_PIXELS)
    DISPLAY_BORDER = pygame.Rect(
        WIDTH_OF_BORDER, DISPLAY_HEIGHT + WIDTH_OF_BORDER, BOARD_WIDTH_PIXELS, WIDTH_OF_BORDER)
    pygame.draw.rect(WIN, LIGHT_GRAY, TOP_BORDER)
    pygame.draw.rect(WIN, LIGHT_GRAY, LEFT_BORDER)
    pygame.draw.rect(WIN, LIGHT_GRAY, BOTTOM_BORDER)
    pygame.draw.rect(WIN, LIGHT_GRAY, RIGHT_BORDER)
    pygame.draw.rect(WIN, LIGHT_GRAY, DISPLAY_BORDER)

    pygame.display.update()


def draw_boxes(u_board):
    """Draws the game display"""

    for i in range(GAME_HEIGHT_TILES):
        for j in range(GAME_WIDTH_TILES):

            # Defines the starting width and height for the boxes
            box_starting_width = GAME_STARTING_WIDTH + SIZE_OF_SQUARE * j + MINE_BORDER // 2
            box_starting_height = GAME_STARTING_HEIGHT + \
                SIZE_OF_SQUARE * i + MINE_BORDER // 2

            # Draws a number unless otherwise stated
            if u_board[i][j] == "-":
                # Draws a grayed out box
                box = pygame.Rect(
                    box_starting_width, box_starting_height, SIZE_OF_SQUARE, SIZE_OF_SQUARE)
                pygame.draw.rect(WIN, LIGHT_GRAY, box)
            elif u_board[i][j] == 1:
                draw_text = NUMBER_FONT.render("1", 1, BLUE)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == 2:
                draw_text = NUMBER_FONT.render("2", 1, GREEN)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == 3:
                draw_text = NUMBER_FONT.render("3", 1, RED)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == 4:
                draw_text = NUMBER_FONT.render("4", 1, DARK_BLUE)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == 5:
                draw_text = NUMBER_FONT.render("5", 1, MAROON)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == 6:
                draw_text = NUMBER_FONT.render("6", 1, TEAL)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == 7:
                draw_text = NUMBER_FONT.render("7", 1, BLACK)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == 8:
                draw_text = NUMBER_FONT.render("8", 1, DARK_GRAY)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == "X":
                # Draws a mine
                draw_text = NUMBER_FONT.render("*", 1, BLACK)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == "R":
                # Draws the mine which was revealed by user
                draw_text = NUMBER_FONT.render("*", 1, RED)
                WIN.blit(draw_text, (box_starting_width + SIZE_OF_SQUARE / 2 - draw_text.get_width(
                ) / 2, box_starting_height + SIZE_OF_SQUARE / 2 - draw_text.get_height() / 2))
            elif u_board[i][j] == "F":
                # Draws the flag
                pygame.draw.polygon(WIN, RED, ((box_starting_width + 1 + SIZE_OF_SQUARE / 2, box_starting_height + 6), (box_starting_width +
                                    1 + SIZE_OF_SQUARE / 6, box_starting_height + 14), (box_starting_width + 1 + SIZE_OF_SQUARE / 2, box_starting_height + 20)))
                flag_pole = pygame.Rect(
                    box_starting_width + SIZE_OF_SQUARE / 2, box_starting_height + 20, 2, 10)
                flag_base = pygame.Rect(box_starting_width + 1 + SIZE_OF_SQUARE / 6,
                                        box_starting_height + 32, int(SIZE_OF_SQUARE * (2 / 3)), 4)
                flag_base2 = pygame.Rect(
                    box_starting_width + 1 + SIZE_OF_SQUARE / 4, box_starting_height + 30, int(SIZE_OF_SQUARE / 2), 2)
                pygame.draw.rect(WIN, BLACK, flag_pole)
                pygame.draw.rect(WIN, BLACK, flag_base)
                pygame.draw.rect(WIN, BLACK, flag_base2)

    # Draws lines to divide the boxes
    for i in range(0, GAME_HEIGHT_TILES + 1):
        pygame.draw.line(WIN, DARK_GRAY, (GAME_STARTING_WIDTH, GAME_STARTING_HEIGHT + i * SIZE_OF_SQUARE),
                         (BOARD_WIDTH_PIXELS - GAME_STARTING_WIDTH - MINE_BORDER, GAME_STARTING_HEIGHT + i * SIZE_OF_SQUARE), MINE_BORDER)
    for i in range(0, GAME_WIDTH_TILES + 1):
        pygame.draw.line(WIN, DARK_GRAY, (GAME_STARTING_WIDTH + i * SIZE_OF_SQUARE, GAME_STARTING_HEIGHT),
                         (GAME_STARTING_WIDTH + i * SIZE_OF_SQUARE, BOARD_HEIGHT_PIXELS - WIDTH_OF_BORDER), MINE_BORDER)

    pygame.display.update()


def get_grid_cord(x, y):
    """Gets the grid coordinate that coresponds to the x and y pixels"""

    DISPLAY_BUTON_HEIGHT_UPPER_BOUND = (WIDTH_OF_BORDER + WIDTH_OF_BORDER // 2) + (DISPLAY_HEIGHT - WIDTH_OF_BORDER)
    DISPLAY_BUTON_HEIGHT_LOWER_BOUND = WIDTH_OF_BORDER + WIDTH_OF_BORDER // 2
    
    HINT_DISPLAY_STARTING_WIDTH = BOARD_WIDTH_PIXELS - int(6.85 * SIZE_OF_SQUARE) + WIDTH_OF_BORDER // 2
    HINT_DISPLAY_WIDTH = 4 * SIZE_OF_SQUARE - int(2 * WIDTH_OF_BORDER)
    
    # Tests if the user clicked the reset button
    if x > BOARD_WIDTH_PIXELS // 2 - (DISPLAY_HEIGHT - WIDTH_OF_BORDER) // 2 and x < (BOARD_WIDTH_PIXELS // 2 - (DISPLAY_HEIGHT - WIDTH_OF_BORDER) // 2) + (DISPLAY_HEIGHT - WIDTH_OF_BORDER) and y > DISPLAY_BUTON_HEIGHT_LOWER_BOUND and y < DISPLAY_BUTON_HEIGHT_UPPER_BOUND:
        pygame.event.post(pygame.event.Event(RESET))
    
    # Tests if the user clicked the hint button
    if x > HINT_DISPLAY_STARTING_WIDTH and x < HINT_DISPLAY_STARTING_WIDTH + HINT_DISPLAY_WIDTH and y > DISPLAY_BUTON_HEIGHT_LOWER_BOUND // 2 and y < DISPLAY_BUTON_HEIGHT_UPPER_BOUND:
        pygame.event.post(pygame.event.Event(HINT))
        
    # Determines what box, if any, the user clicked
    cords = [-1, -1]
    if x > GAME_STARTING_WIDTH and x < BOARD_WIDTH_PIXELS - WIDTH_OF_BORDER - MINE_BORDER // 2:
        cords[0] = (x - GAME_STARTING_WIDTH) // SIZE_OF_SQUARE
    if y > GAME_STARTING_HEIGHT and y < BOARD_HEIGHT_PIXELS - WIDTH_OF_BORDER - MINE_BORDER // 2:
        cords[1] = (y - GAME_STARTING_HEIGHT) // SIZE_OF_SQUARE
    return cords


def main():
    """Runs minesweeper"""

    # Initializes some variables
    run = True
    pause = False
    clock = pygame.time.Clock()
    time = 0
    loops = 0
    smile = 0

    # Initializes the game board and display board
    game_board = [["*" for i in range(GAME_WIDTH_TILES)]
                    for j in range(GAME_HEIGHT_TILES)]
    user_board = [["*" for i in range(GAME_WIDTH_TILES)]
                    for j in range(GAME_HEIGHT_TILES)]

    # Places the mines and numbers on the game board
    ms_funct.fill_game_board(
        game_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES, MINES)

    # ms_funct.print_board(game_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES) # Used to display where mines are for testing

    draw_window()

    while run:
        # Iterates thorugh the loop at FPS times per second
        clock.tick(FPS)

        # Adds 1 to the time every second
        loops += 1
        if loops % FPS == 0 and not pause:
            time += 1

        # Initializes the array to store the coordinate of the button the user may press
        button_pressed = [-1, -1]

        # Iterates through all events
        for event in pygame.event.get():
          
            # Quits game if user exists out
            if event.type == pygame.QUIT:
                run = False
                return False

            # Runs when the user clicks their mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ms_funct.print_board(user_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES) # Used to display where mines are for testing
              
                # If left click, the coordinates are checked to see what tile the user is attempting to reveal
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    button_pressed = get_grid_cord(
                        pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if (not pause):
                        # If valid tile, the move is attempted and if the user revealed a mine an event is posted to end the game
                        if button_pressed[0] != -1 and button_pressed[1] != -1:
                            if ms_funct.make_move(game_board, user_board, button_pressed[1], button_pressed[0], GAME_WIDTH_TILES, GAME_HEIGHT_TILES):
                                game_board[button_pressed[1]][button_pressed[0]] = 'R'
                                user_board[button_pressed[1]][button_pressed[0]] = 'R'
                                pygame.event.post(pygame.event.Event(HIT_MINE))
                # If right click, the coordinates are checked to see what tile the user is attempting to flag
                elif pygame.mouse.get_pressed() == (0, 0, 1):
                    button_pressed = get_grid_cord(
                        pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    if (not pause):
                        # If valid tile, a flag is placed
                        if button_pressed[0] != -1 and button_pressed[1] != -1:
                            if ms_funct.flag(user_board, button_pressed[1], button_pressed[0], GAME_WIDTH_TILES, GAME_HEIGHT_TILES):
                                draw_window()
                                pass

            # Runs when the user presses a key
            if event.type == pygame.KEYDOWN and not pause:
                # If the key is left control, the game reveals a random tile that is not a mine or removes a misplaced flag
                if event.key == pygame.K_LCTRL:
                    # if(ms_funct.hint(game_board, user_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES, MINES)):
                    ms_funct.hint(game_board, user_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES, MINES)


            # Runs if a mine was hit
            if event.type == HIT_MINE:
                ms_funct.reveal_mines(
                    game_board, user_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES)
                draw_window()
                smile = 2
                pause = True

            # Runs if player won the game
            if event.type == FOUND_ALL_MINES:
                smile = 1
                pause = True

            # Runs if game is reset
            if event.type == RESET:
                run = False
                
            # Runs if game is reset
            if event.type == HINT:
                # uses the ai to generate the postion (x, y) of the next best tile to reveal
                # also indicites if the move should reveal a tile or place a flag
                if (not pause):
                    x, y, placeFlag = ms_funct.ai_move(user_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES)

                    if (placeFlag):
                        ms_funct.flag(user_board, x, y, GAME_WIDTH_TILES, GAME_HEIGHT_TILES)
                    else:
                        # makes a move on that tile
                        if ms_funct.make_move(game_board, user_board, x, y, GAME_WIDTH_TILES, GAME_HEIGHT_TILES):
                            game_board[x][y] = 'R'
                            user_board[x][y] = 'R'
                            pygame.event.post(pygame.event.Event(HIT_MINE))
                    

        if run == True:
            # Checks if the user has won the game and if so an event is posted
            if ms_funct.check_win(user_board, GAME_WIDTH_TILES, GAME_HEIGHT_TILES, MINES):
                pygame.event.post(pygame.event.Event(FOUND_ALL_MINES))

            # Updates the display
            num_mines_left = ms_funct.get_mines_left(user_board, MINES)
            draw_display(num_mines_left, time, smile)
            draw_boxes(user_board)
            

    return True


if __name__ == "__main__":
    continue_game = True
    while continue_game:
        continue_game = main()
    print("Thanks for playing :)")
    pygame.quit()
