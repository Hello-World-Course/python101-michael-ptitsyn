def is_name_valid(name):
    return len(name) > 2


def is_board_size_valid(b_s):
    return 0 < b_s < 26

def is_number_of_mines_valid(board_size, number_of_mines):
    return number_of_mines and number_of_mines < 0.5 * board_size*board_size


def register_user():
    name = input("Hello, whats your name?")
    if not is_name_valid(name):
        print("Your name is too short")
        return None, None, None
    board_size = int(input(f"{name}, please choose board size:"))
    if not is_board_size_valid(board_size):
        print(f"{name}, you have entered illegal board size")
        return None, None, None
    number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate:"))

    if not is_number_of_mines_valid(board_size, number_of_mines):
        print(f"{name}, you have entered illegal number of mines")
        return None, None, None
    return name, board_size, number_of_mines