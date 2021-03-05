# This python file contains the solver algorithm that will determine a valid solution to the set
# game board.


import board_functions as func
import verifier as algo


# Function assigns light bulbs to pre-determined board cells (ex: A numbered 4 box requires 4 light bulbs to be placed
# directly adjacent to it) and determines remaining to-be-assigned white cells in game board
def setup_solver(board, numbered_black_boxes):
    board_range = [0, 1, 2, 3, 4, 5, 6]

    # Determine if it's possible to pre-set bulbs for numbered boxes or pre-set squares to yellow
    # as its not possible to place a light bulb there (ex: a 0 box cannot have any bulbs near it)
    for box in numbered_black_boxes:
        x_index = box[1] - 1
        y_index = box[0] - 1
        adjacent_cells = [[x_index, y_index + 1], [x_index, y_index - 1], [x_index + 1, y_index], [x_index - 1, y_index]]
        bulb_tally = 0

        # Determine if adjacent cells (where applicable) can have a bulb placed there
        for cell in adjacent_cells:
            x = cell[0]
            y = cell[1]
            # Check if cell below numbered box is a potential space for a bulb
            # y_index += 1
            if (x in board_range and y in board_range) and board[x][y].state == 0:
                bulb_tally += 1
                # If 0 box, set adjacent square to yellow - cannot assign bulb next to it
                if box[2] == 0:
                    board[x][y].assign_cell(9)

        # If white squares directly adjacent to number of black box is equal to number of box,
        # assign light bulb icons to those locations
        if bulb_tally == box[2]:
            for cell in adjacent_cells:
                x = cell[0]
                y = cell[1]
                if (x in board_range and y in board_range) and board[x][y].state == 0:
                    board[x][y].assign_cell(1)
                    # x = board[x_index][y_index].x
                    # y = board[x_index][y_index].y
                    #pre_set_bulbs.append([x, y])

    # Add beams to board
    func.update_beams(board)

    # Determine whit cells in board
    return get_white_cells(board)


def get_white_cells(board):
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
    cell_state = board[numbered_box[0]][numbered_box[1]].state - 4
    list_of_bulbs = find_adjacent(board, numbered_box, cell_state)
    if list_of_bulbs:
        return len(list_of_bulbs)
    else:
        return 0

# Function determines cells adjacent to desired cell
def find_adjacent(board, cell, cell_type):
    board_range = [0, 1, 2, 3, 4, 5, 6]
    list_of_adj = []
    x_index = cell[0]
    y_index = cell[1]
    adjacent_cells = [[x_index, y_index + 1], [x_index, y_index - 1], [x_index + 1, y_index], [x_index - 1, y_index]]

    # If cell type is white cell, determine if cells directly adjacent are numbered boxes
    # If yes, add to list
    if cell_type == 0:
        for cell in adjacent_cells:
            # If cell below cell in question is a numbered box,
            # add to list_of_adj
            # y_index += 1
            x = cell[0]
            y = cell[1]
            if (x in board_range and y in board_range) and board[x][y].state > 3:
                list_of_adj.append([x, y])
        return list_of_adj

    # If cell type is numbered box cell, determine if cells directly adjacent are light bulbs
    # If yes, add to list
    if cell_type > 3:
        for cell in adjacent_cells:
            x = cell[0]
            y = cell[1]
            if (x in board_range and y in board_range) and board[x][y].state == 1:
                list_of_adj.append([x, y])
        return list_of_adj


# Function determines if the potential location to place the bulb in is valid
def valid_placement(board, cell, cell_type):
    # If potential cell type is a white cell, continue - no verification needed
    if cell_type == 0:
        return True
    # If potential cell type changing from white cell to light bulb, determine if
    # its placement will interfere with beams and numbered boxes (where applicable)
    # on board
    else:
        # Verify bulb placement does not conflict with other beams
        if not algo.check_beams(board, cell):
            return False
        # Determine if cell has numbered black box(es) around it
        adjacent_to_cell = find_adjacent(board, cell, 0)

        # If bulb placement is directly adjacent to numbered box, ensure its placement is valid
        for num_box in adjacent_to_cell:
            max_bulbs = board[num_box[0]][num_box[1]].state - 4
            adj_bulbs = num_box_tally(board, num_box)
            # If numbered box already has maximum assigned bulbs directly adjacent to it, return
            # False. Placement is invalid
            if adj_bulbs + 1 > max_bulbs:
                return False
        # If placement is valid, return True
        return True


# Function recursively determines possible light bulb placements to generate wining certificate solution
def solver(board, cells_to_try, tried_cells):
    for white_cell in cells_to_try:
        if white_cell not in tried_cells:
            # Set up x and y board coordinate values
            x = white_cell[0]
            y = white_cell[1]
            assignment = 1

            # Check bulb placement
            if valid_placement(board, white_cell, assignment):
                # Assign cell new state
                board[x][y].assign_cell(assignment)
                # Update board with beams of all light bulbs now present in board
                func.update_beams(board)
                # Update list of white cells now present in board
                cells_to_try = get_white_cells(board)
                # Recursively call solver() function until all placements are deemed valid
                # or final solution is found to be valid and function needs to backtrack bulb placement
                result = solver(board, cells_to_try, tried_cells)

                # If assignment fails, change backtrack solution and bulb placement
                if not result:
                    # Un-assign bulb - change back to white cell
                    board[x][y].assign_cell(0)
                    # Update board with beams of all light bulbs now present in board
                    func.update_beams(board)
                    # Update list of white cells now present in board
                    cells_to_try = get_white_cells(board)
                    # Removed unsuccessfully attempted cell from list
                    #cells_to_try.remove([x, y])

            # If placement was invalid, remove cell from list of potential values to try
            #cells_to_try.remove([x, y])
            print('placement invalid, try next cell')


    # If all cells assinged a value, determine if certificate solution is valid.
    # If puzzle solved, send completion message. Else return False to backtrack solution.
    print('tried all cells currently in cells_to_try: CHECKING SOLUTION')
    if algo.verifier(board):
        return True
    # if algo.verifier(board, light_bulb_cells, numbered_black_boxes):
    # sg.popup('Puzzle solved!', title='Note:')
    else:
        # If placement results in invalid solution, backtrack to find next possible
        # valid step to solve puzzle
        print('Solution not found: BACKTRACKING')
        return False
