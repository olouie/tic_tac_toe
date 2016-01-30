def show_board(grid): # displays board
    print ' '
    for line in grid:
        print line
    
print 'Welcome to Tic Tac Toe.\nPlease enter player names.'
player1 = raw_input('Player x: ')
player2 = raw_input('Player o: ')

# Assigns the symbols x/o to players
symbol = {player1:'x',player2:'o'}

# The keyboard letters that correspond to the board spaces
list_space = [['q','w','e'],['a','s','d'],['z','x','c']]
list_one = ['q','w','e','a','s','d','z','x','c']
x_coordinate = {}
y_coordinate = {}

# This for loop will attach separate x and y coordiante value to every keyboard letter space
for row in list_space:
    for element in row:
        x_coordinate[element] = list_space.index(row)
        y_coordinate[element] = 4*(row.index(element))+1

play_again = 'yes'

while play_again == 'yes':

    # Defines values for new game
    board = ["___|___|___","___|___|___","   |   |   "]

    # Has meaningless intergers to place hold but will be replaced by symbols for win checks
    board_row = [[1,2,3],[4,5,6],[7,8,9]]
    board_column = [[1,2,3],[4,5,6],[7,8,9]]
    board_diagonal = [[1,2,3],[4,5,6]]
    
    # Indicate whose turn it is
    player_turn = player1

    # set to 'q' to just define user_input for the space and empty while loop check
    user_input = 'q'

    # Turn counter that will be used to limit number of turns to 9 per game
    num_turn = 0

    game_won = False

    while game_won == False:

        # if statement that will switch turns between the two players
        if num_turn % 2 == 0:
            player_turn = player1
        else:
            player_turn = player2

        show_board(board)

        print "Player ",symbol[player_turn],'turn:',player_turn

        valid = False

        # This while loop will only allow corresponding keyboard spaces that are empty
        while valid == False:

            user_input = raw_input('Pick space: ') 
            
            # This if statement will check if user_input is a corresponding keyboard letter
            if user_input in list_one:
                # collapse breaks up a row on the board into separate list elements so it can be iterated over with player symbols
                collapse = list(board[x_coordinate[user_input]])

                # This if statment will check if the selected space is empty
                if collapse[y_coordinate[user_input]] != 'x' and collapse[y_coordinate[user_input]] != 'o':
                    valid = True
                    # This replaces the empty spot on the board with the user's symbol using the y-coordinate
                    collapse[y_coordinate[user_input]] = symbol[player_turn]

                    # This big mess will replace the intergers in board_row with the player symbols for the win checks    
                    board_row[x_coordinate[user_input]][(y_coordinate[user_input]-1)/4] = symbol[player_turn]

                    # After iterating over the collapsed row, this reassembles and replaces the previous row
                    board[x_coordinate[user_input]] = ''.join(collapse)

        # This for loop will create matrixes from board_row that will check for wins
        for i in xrange(0,3):
            for row in board_row:
                board_column[i][int(board_row.index(row))] = row[i]
            board_diagonal[0][i] = board_row[i][i]
            board_diagonal[1][i] = board_row[i][2-i]


        # The next 3 for loop check for wins after each turn
        # Was not sure how to write a method that check for wins and break all the nested loops
        for row in board_row:
            if row[0] == row[1] == row[2]:
                show_board(board)
                print player_turn,"wins!"
                game_won = True
                break

        for row in board_column:
            if row[0] == row[1] == row[2]:
                show_board(board)
                print player_turn,"wins!"
                game_won = True
                break

        for row in board_diagonal:
            if row[0] == row[1] == row[2]:
                show_board(board)
                print player_turn,"wins!"
                game_won = True
                break

        # Adds to the turn counter
        num_turn += 1

        # This if statement limits the game to 9 turns, usually means tie
        if num_turn == 9:
            print 'Tie!\nGame over!'
            break

    play_again = raw_input('Play again? ').lower()