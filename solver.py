# File contains algorithm that solves the board for the user
import PySimpleGUI as sg
import board_functions as func
import verifier as algo

# Function assigns light bulbs to pre-determined board cells (ex: A numbered 4 box requires 4 light bulbs to be placed
# directly adjacent to it) and determines remaining to-be-assigned white cells in game board
def setup_solver(board, numbered_black_boxes):
    board_range = [0, 1, 2, 3, 4, 5, 6]
    pre_set_bulbs = []

    # Determine if possible to pre-set bulbs for numbered boxes or pre-set squares to yellow
    # as its not possible to place a light bulb there (ex: 0 box cannot have any bulbs near it)
    for box in numbered_black_boxes:
        y_index = box[0] - 1
        x_index = box[1] - 1
        bulb_tally = 0
        # Check if cell below numbered box is white
        y_index += 1
        if y_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1
            # If 0 box, set adjacent square to yellow - cannot assign bulb next to it
            if box[2] == 0:
                board[x_index][y_index].assign_cell(9)

        # Check if cell above numbered box is white
        y_index = box[0] - 1
        y_index -= 1
        if y_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1
            # If 0 box, set adjacent square to yellow - cannot assign bulb next to it
            if box[2] == 0:
                board[x_index][y_index].assign_cell(9)

        # Check if cell left of numbered box is white
        y_index = box[0] - 1
        x_index -= 1
        if x_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1
            # If 0 box, set adjacent square to yellow - cannot assign bulb next to it
            if box[2] == 0:
                board[x_index][y_index].assign_cell(9)

        # Check if cell right of numbered box is white
        x_index = box[1] - 1
        x_index += 1
        if x_index in board_range and board[x_index][y_index].state == 0:
            bulb_tally += 1
            # If 0 box, set adjacent square to yellow - cannot assign bulb next to it
            if box[2] == 0:
                board[x_index][y_index].assign_cell(9)

        # If available white squares directly adjacent to number of black box is equal to number of box,
        # assign light bulb icons to those locations
        if bulb_tally == box[2]:

            y_index = box[0] - 1
            x_index = box[1] - 1
            bulb_tally = 0
            # If cell below numbered box is white, assign light bulb icon
            y_index += 1
            if y_index in board_range and board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(1)
                x = board[x_index][y_index].x
                y = board[x_index][y_index].y
                pre_set_bulbs.append([x, y])

            # If cell above numbered box is white, assign light bulb icon
            y_index = box[0] - 1
            y_index -= 1
            if y_index in board_range and board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(1)
                x = board[x_index][y_index].x
                y = board[x_index][y_index].y
                pre_set_bulbs.append([x, y])

            # If cell left of numbered box is white, assign light bulb icon
            y_index = box[0] - 1
            x_index -= 1
            if x_index in board_range and board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(1)
                x = board[x_index][y_index].x
                y = board[x_index][y_index].y
                pre_set_bulbs.append([x, y])

            # If cell right of numbered box is white, assign light bulb icon
            x_index = box[1] - 1
            x_index += 1
            if x_index in board_range and board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(1)
                x = board[x_index][y_index].x
                y = board[x_index][y_index].y
                pre_set_bulbs.append([x, y])

    # Add beams to board
    func.update_beams(board)

    white_cells = []
    # Determine whit cells in board
    for col in board:
        for cell in col:
            if cell.state == 0:
                white_cells.append([cell.x, cell.y])
    return white_cells



# Function finds a white cell in game board for solver algorithm to place
# a bulb in. If no remaining white cells exist in the board, return False
def find_white_cell(board, white_cell):
    for col in board:
        for cell in col:
            if cell.state == 0:
                white_cell[0] = cell.x
                white_cell[1] = cell.y
                return False
    return True

# Function tallies number of light bulbs around numbered box cell
def num_box_tally(board, numbered_box):
    cell_state = board[numbered_box[0]][numbered_box[1]].state - 3
    list_of_bulbs = find_adjacent(board, numbered_box, cell_state)
    return len(list_of_bulbs)

# Function determines cells adjacent to desired cell
def find_adjacent(board, cell, cell_type):
    board_range = [0, 1, 2, 3, 4, 5, 6]
    list_of_adj = []
    y_index = cell[0] - 1
    x_index = cell[1] - 1

    # If cell type is white cell, continue query to determine if cells adjacent are
    # or are not numbered boxes
    if cell_type == 0:
        # If cell below cell in question is a numbered box,
        # add to list_of_adj
        y_index += 1
        if y_index in board_range and board[x_index][y_index].state > 2:
            list_of_adj.append([x_index, y_index])

        # If cell above cell in question in question is a numbered box,
        # add to list_of_adj
        y_index = cell[0] - 1
        y_index -= 1
        if y_index in board_range and board[x_index][y_index].state > 2:
            list_of_adj.append([x_index, y_index])

        # If cell left of cell in question is a numbered box,
        # add to list_of_adj
        y_index = cell[0] - 1
        x_index -= 1
        if x_index in board_range and board[x_index][y_index].state > 2:
            list_of_adj.append([x_index, y_index])

        # If cell right of cell in question is a numbered box,
        # add to list_of_adj
        x_index = cell[1] - 1
        x_index += 1
        if x_index in board_range and board[x_index][y_index].state > 2:
            list_of_adj.append([x_index, y_index])
        return list_of_adj

    # If cell type is numbered box cell, continue query to determine if cells adjacent are
    # occupied by light bulbs
    if cell_type > 2:
        # If cell below box in question is a bulb,
        # add to list_of_adj
        y_index += 1
        if y_index in board_range and board[x_index][y_index].state == 1:
            list_of_adj.append([x_index, y_index])

        # If cell above box in question in question is a bulb,
        # add to list_of_adj
        y_index = cell[0] - 1
        y_index -= 1
        if y_index in board_range and board[x_index][y_index].state == 1:
            list_of_adj.append([x_index, y_index])

        # If cell left of box in question is a bulb,
        # add to list_of_adj
        y_index = cell[0] - 1
        x_index -= 1
        if x_index in board_range and board[x_index][y_index].state == 0:
            list_of_adj.append([x_index, y_index])

        # If cell right of box in question is a bulb,
        # add to list_of_adj
        x_index = cell[1] - 1
        x_index += 1
        if x_index in board_range and board[x_index][y_index].state == 0:
            list_of_adj.append([x_index, y_index])
        return list_of_adj

# Function determines if the potential location to place the bulb in is valid
def valid_placement(board, cell, cell_type):
    # If potential cell type is a white cell, continue - no verification needed
    if cell_type == 0:
        return True
    # If potential cell type is a light bulb, continue - no verification needed
    else:
        # Verify bulb placement does not conflict with other beams
        if not algo.check_beams(board, cell):
            return False
        # Determine if cell has numbered black box(es) around it
        adjacent_to_cell = find_adjacent(board, cell)

        # Verify bulb placement does not conflict with directly adjacent numbered box cells
        for num_box in adjacent_to_cell:
            max_bulbs = board[num_box[0]][board[1]] - 3
            adj_bulbs = num_box_tally(board, num_box)
            # If numbered box already has maximum assigned bulbs directly adjacent to it, return
            # False as placement of another bulb adjacent to the box is not valid
            if adj_bulbs + 1 > max_bulbs:
                return False
        # If placement is valid, return True
        return True


# Function recursively determines possible light bulb placements to generate wining certificate solution
def solver(board, cells_to_try):
    #white_cell = [0, 0]

    for white_cell in cells_to_try:
        # Determines cell to try placing bulb in. If puzzle solved, send completion message
        if not cells_to_try:

            sg.popup('Puzzle solved!', title='Note:')
            return True
            # if algo.verifier(board, light_bulb_cells, numbered_black_boxes):
                # sg.popup('Puzzle solved!', title='Note:')

        # Set up x and y board coordinate values
        x = white_cell[0]
        y = white_cell[1]

        for assignment in [1, 0]:
            # Check bulb placement
            if valid_placement(board, white_cell, assignment):

                # Assign bulb
                board[x][y].assign_cell(assignment)
                func.update_beams(board)
                cells_to_try.remove([x, y])

                # Recursively call solver() function until all placements are deemed valid
                # of need to backtrack placement
                if solver(board, cells_to_try):
                    return True

                # If placement fails, change back to white cell
                else:
                    board[x][y].assign_cell(0)

            # If placement results in invalid solution, backtrack to find next possible
            # valid step to solve puzzle
        return False
