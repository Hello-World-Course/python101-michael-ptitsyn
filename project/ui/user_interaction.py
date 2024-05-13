def is_name_valid(name):
    return len(name) > 2


def is_board_size_valid(b_s):
    return 0 < b_s < 26

def is_number_of_mines_valid(board_size, number_of_mines):
    return number_of_mines and number_of_mines < 0.5 * board_size*board_size
