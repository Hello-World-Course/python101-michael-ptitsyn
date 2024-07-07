from project.ui.board_ui import convert_coords

user_input = "4G"
row_number, col_number = convert_coords(user_input)
# will print 3
print(row_number)
# will print 6
print(col_number)

user_input = "23A"
row_number, col_number = convert_coords(user_input)
# will print 22
print(row_number)
# will print 0
print(col_number)
