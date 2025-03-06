import ship

def print_win_message():
    print(f"Congrats, you won!")

def print_lose_message():
    print(f"Sorry you lost.")
    

def create_board(height, width):
    #Creates board filled with "E" with any height and width
    return [["E" for i in range(width)] for i in range(height)]

'''board = create_board(4,4)
ships_grid = create_board(4,4)
ships_grid = ships.place_ships(ships_grid)'''

'''def read_guess(board_copy):
    #Dont need to set the height and width equal to anything since it already has a value
    #height = 4
    #width = 4
    #Changed the name of the variables to work with the rest of the code
    while True:
        col = int(input("enter a column location (enter an appropaite index) \n"))
    #Column index
        if 0 < col < len(width):
        #column_index = int(input("enter a column location (enter an appropaite index) \n"))
            row = int(input("enter a row location (enter an appropaite index)\n"))
            #Row index
            if 0 < row < len(height):
                return (row, col)
            else:
                print("Invalid Input")
                continue
        else:
            print("Invalid Input")
            continue'''
   

def update_guess(guess, board, ships_grid):
    #If the board doesn't t

    if ships_grid[guess[0]][guess[1]] == "E":
        board[guess[0]][guess[1]] = "M"
    elif ships_grid[guess[0]][guess[1]] == "B":
        board[guess[0]][guess[1]] = "H"
    else:
        print("You cant bomb this area again!")

    return board

def read_guess(board):
    col = int(input("enter a column location (enter an appropaite index(1->4)\n:"))
    row = int(input("enter a row location (enter an appropaite index(1->4)\n:"))
    user_guess = []
    while int(col) > len(board[0]) or int(row) > len(board[1]) or (row,col) in user_guess:
        print("row and col not found: Try again ")
        col = int(input("enter a column location (enter an appropaite index(1->4)\n:"))
        row = int(input("enter a row location (enter an appropaite index(1->4)\n:"))
    row -= 1
    col -= 1
    user_guess.append(row)
    user_guess.append(col)
    return (user_guess)

def play_game(num_guesses):
    print('--<|--\n---|--\n-[_|_]-')
    print('Welcome to BattleShip')
    #print('How big would you like your board to be (ex: 3 x 3 or 5 x 5)')
    #width = input(': ')
    #height = input(': ')

    board = create_board(4, 4)
    ships_grid = create_board(4,4)
    ships_grid = ship.place_ships(ships_grid)
    guess_list = []
    
    while True:
        print(ships_grid)
        print(f'Number of Guesses left: {num_guesses}')
        print('__|._1_|._2_.|._3_.|._4_.|<COL')
        print('1_|' + str(board[0]))
        print('2_|' + str(board[1]))
        print('3_|' + str(board[2]))
        print('4_|' + str(board[3]))
        print('^ROW')
        guess = read_guess(board)
        num_guesses -= 1
        if guess not in guess_list:
            update_guess(guess, board, ships_grid)
            guess_list.append((guess))
        else: 
            print('You cannot guess this location again')
            num_guesses += 1

        num_B = 0
        num_H = 0
        for i in range(len(ships_grid)):
            for j in range(len(ships_grid[i])):
                if ships_grid[i][j] == 'B':
                    num_B += 1
        for a in range(len(board)):
            for b in range(len(board[a])):
                if board[a][b] == 'H':
                    num_H += 1
        if num_B == num_H:
            print_win_message()
            print('__|._1_|._2_.|._3_.|._4_.|<COL')
            print('1_|' + str(board[0]))
            print('2_|' + str(board[1]))
            print('3_|' + str(board[2]))
            print('4_|' + str(board[3]))
            print('^ROW')
            break

        elif num_guesses == 0:
            print_lose_message()
            print('Wrong Board:\n__|._1_|._2_.|._3_.|._4_.|')
            print('1_|' + str(board[0]))
            print('2_|' + str(board[1]))
            print('3_|' + str(board[2]))
            print('4_|' + str(board[3]))
            
            print('Correct Board:\n__|._1_|._2_.|._3_.|._4_.|')
            print('1_|' + str(ships_grid[0]))
            print('2_|' + str(ships_grid[1]))
            print('3_|' + str(ships_grid[2]))
            print('4_|' + str(ships_grid[3]))
            
            break
            