import random
from pytimedinput import timedInput
from grid import GRID
import os


def check_for_change_input(u_input):
    return u_input


def check_for_collision(row, col):
    return GRID[row][col] == "X"


def grow(last_input):
    last_snake_el = snake_positions[-1]
    last_snake_row = last_snake_el[0]
    last_snake_col = last_snake_el[1]

    row_to_grow = last_snake_row + add_to_snake[last_input][0]
    col_to_grow = last_snake_col + add_to_snake[last_input][1]

    if not is_not_valid(row_to_grow, col_to_grow):
        snake_positions.append([row_to_grow, col_to_grow])
        GRID[row_to_grow][col_to_grow] = "X"

    else:
        if last_input == "w" or last_input == "s":
            row_to_grow = last_snake_row + add_to_snake["d"][0]
            col_to_grow = last_snake_row + add_to_snake["d"][1]

            if not is_not_valid(row_to_grow, col_to_grow):
                snake_positions.append([row_to_grow, col_to_grow])
                GRID[row_to_grow][col_to_grow] = "X"
                return

            row_to_grow = last_snake_row + add_to_snake["a"][0]
            col_to_grow = last_snake_row + add_to_snake["a"][1]

            if not is_not_valid(row_to_grow, col_to_grow):
                snake_positions.append([row_to_grow, col_to_grow])
                GRID[row_to_grow][col_to_grow] = "X"

        else:
            row_to_grow = last_snake_row + add_to_snake["w"][0]
            col_to_grow = last_snake_row + add_to_snake["w"][1]

            if not is_not_valid(row_to_grow, col_to_grow):
                snake_positions.append([row_to_grow, col_to_grow])
                GRID[row_to_grow][col_to_grow] = "X"
                return

            row_to_grow = last_snake_row + add_to_snake["s"][0]
            col_to_grow = last_snake_row + add_to_snake["s"][1]

            if not is_not_valid(row_to_grow, col_to_grow):
                snake_positions.append([row_to_grow, col_to_grow])
                GRID[row_to_grow][col_to_grow] = "X"


def is_not_valid(row, col):
    return (1 > row or 1 > col) or (row > 15 or col > 15)


def check_for_fruit(row, col):
    if GRID[row][col] == "O":
        return True

    return False


def make_a_move(u_input):
    global is_lost
    curr_snake_row = snake_positions[0][0]
    curr_snake_col = snake_positions[0][1]

    row_to_move = curr_snake_row + directions[u_input][0]
    col_to_move = curr_snake_col + directions[u_input][1]

    if is_not_valid(row_to_move, col_to_move):
        is_lost = True
        return

    if check_for_collision(row_to_move, col_to_move):
        is_lost = True
        return

    ck = check_for_fruit(row_to_move, col_to_move)

    GRID[row_to_move][col_to_move] = "X"
    GRID[curr_snake_row][curr_snake_col] = " "

    row_to_turn = curr_snake_row
    col_to_turn = curr_snake_col

    if len(snake_positions) > 1:
        for i in range(1, len(snake_positions)):
            try:
                curr_row = snake_positions[i][0]
                curr_col = snake_positions[i][1]

                GRID[row_to_turn][col_to_turn] = "X"
                GRID[curr_row][curr_col] = " "

                snake_positions[i][0] = row_to_turn
                snake_positions[i][1] = col_to_turn

                row_to_turn = curr_row
                col_to_turn = curr_col

            except IndexError:
                break

    snake_positions[0][0] = row_to_move
    snake_positions[0][1] = col_to_move

    return ck


initial_row = 8
initial_col = 2

snake_positions = [[initial_row, initial_col]]

snake_symbol = "X"
GRID[initial_row][initial_col] = snake_symbol

directions = {
    "w": (-1, 0),
    "s": (1, 0),
    "a": (0, -1),
    "d": (0, 1)
}

add_to_snake = {
    "w": (1, 0),
    "s": (-1, 0),
    "a": (0, 1),
    "d": (0, -1)
}

initial_fruit_row = 8
initial_fruit_col = 8

GRID[initial_fruit_row][initial_fruit_col] = "O"

is_taken = False
is_lost = False

last_user_input = ""
user_input = "d"

while True:
    os.system("cls")

    while True:
        fruit_row = random.randint(1, 15)
        fruit_col = random.randint(1, 15)

        if not GRID[fruit_row][fruit_col] == "X":
            break

    if is_taken:
        GRID[fruit_row][fruit_col] = "O"
        is_taken = False

    for el in GRID:
        print(''.join(el))

    txt,_ = timedInput("get_input:", timeout=0.4)

    if txt == "w" and not last_user_input == "s":
        user_input = "w"
    elif txt == "s" and not last_user_input == "w":
        user_input = "s"
    elif txt == "d" and not last_user_input == "a":
        user_input = "d"
    elif txt == "a" and not last_user_input == "d":
        user_input = "a"
    elif txt == "q":
        break

    last_user_input = user_input

    mm = make_a_move(user_input)

    if is_lost:
        print("You Lost!")
        break

    if mm:
        is_taken = True
        grow(last_user_input)

