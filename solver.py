# File contains algorithm that solves the board for the user
white_cells = []

# Function assigns light bulbs to pre-determined board cells (ex: A numbered 4 box requires 4 light bulbs to be placed
# directly adjacent to it) and determines remaining to-be-assigned white cells in game board
def setup_solver(board, numberedBlackBox):
    board_range = [0, 1, 2, 3, 4, 5, 6]

    for box in numberedBlackBox:
        y_index = box[0] - 1
        x_index = box[1] - 1
        bulb_tally = 0
        # Check if cell below numbered box is white
        y_index += 1
        if y_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1

        # Check if cell above numbered box is white
        y_index = box[0] - 1
        y_index -= 1
        if y_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1

        # Check if cell left of numbered box is white
        y_index = box[0] - 1
        x_index -= 1
        if x_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1

        # Check if cell right of numbered box is white
        x_index = box[1] - 1
        x_index += 1
        if x_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1

        # If available white squares directly adjacent to number of black box is equal to number of box,
        # assign light bulb icons to those locations
        if bulb_tally == box[2]:
            for i in bulb_tally:
                y_index = box[0] - 1
                x_index = box[1] - 1
                bulb_tally = 0
                # If cell below numbered box is white, assign light bulb icon
                y_index += 1
                if y_index in board_range and board[x_index][y_index].state == 0:
                    board[x_index][y_index].assign_cell(1)

                # If cell above numbered box is white, assign light bulb icon
                y_index = box[0] - 1
                y_index -= 1
                if y_index in board_range and board[x_index][y_index].state == 0:
                    board[x_index][y_index].assign_cell(1)

                # If cell left of numbered box is white, assign light bulb icon
                y_index = box[0] - 1
                x_index -= 1
                if x_index in board_range and board[x_index][y_index].state == 0:
                    board[x_index][y_index].assign_cell(1)

                # If cell right of numbered box is white, assign light bulb icon
                x_index = box[1] - 1
                x_index += 1
                if x_index in board_range and board[x_index][y_index].state == 0:
                    board[x_index][y_index].assign_cell(1)

    # Determine remaining white cells in game board
    for col in board:
        for cell in col:
            if cell.state == 0:
                white_cells.append([cell.x, cell.y])

def updater(l):
    l[0] = 1
    l[1] = 2
    return False


# Function recursively determines possible light bulb placements to generate wining certificate solution
def solver(board, numberedBlackBox):
    l = [0, 0]

    if (not updater(l)):
        return True
    print(str(l[0]) + ' ' + str(l[1]))
    print('done')

solver([], [])