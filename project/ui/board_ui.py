def parse_cmd(command: str):
    cmd, *args = command.split(" ")
    return cmd, args


def draw_board(board):
    a_ord = ord("A")
    board_str = " "*3 + " ".join(chr(a_ord + i) for i in range(len(board))) + " \n"
    for i, row in enumerate(board):
        board_str += f"{i} |"+"|".join(str(i) for i in row) + "|\n"
    return board_str

def convert_coords(location):
    return int(location[:-1])-1, ord(location[-1])-ord('A')