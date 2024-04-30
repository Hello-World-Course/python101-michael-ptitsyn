name = input("Hello, whats your name?")
if len(name)>=2:
    board_size = int(input(f"{name}, please choose board size:"))
    number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate:"))
    if number_of_mines>0 and number_of_mines<=0.5*board_size*board_size:
        print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")
    else:
        print(f"{name}, you have entered illegal number of mines")
else:
    name=None
    print("Your name is too short")