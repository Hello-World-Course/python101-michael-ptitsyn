from project.board.board_functions import create_empty_board

# will print [[None, None, None], [None, None, None], [None, None, None]]
print(create_empty_board(3, None))

# will print [[None]]
print(create_empty_board(1, None))

# will print [["test", "test"], ["test", "test"]]
print(create_empty_board(2, "test"))
