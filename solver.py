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
    func.update_beams(board, pre_set_bulbs)


# Function finds a white cell in game board for solver algorithm to place
# a bulb in. If no remaining white cells exist in the board, return False
def find_white_cell(white_cell, board):
    for col in board:
        for cell in col:
            if cell.state == 0:
                white_cell[0] = cell.x
                white_cell[1] = cell.y
                return True
    return False


# Function recursively determines possible light bulb placements to generate wining certificate solution
def solver(board):
    white_cell = [0, 0]
    light_bulb_cells = []
    # setup_solver(board, numbered_black_boxes)
    #print(white_cells)

    # Determines cell to try placing bulb in. If puzzle solved, send completion message
    if not find_white_cell():
        sg.popup('Puzzle solved!', title='Note:')
        # if algo.verifier(board, light_bulb_cells, numbered_black_boxes):
            # sg.popup('Puzzle solved!', title='Note:')

    # Set up x and y board coordinate values
    x = white_cell[0]
    y = white_cell[1]

    # Check bulb placement
    if valid_placement():

        # Assign bulb
        board[x][y].assign_cell(1)

        # Recursively call solver() function until all placements are deemed valid
        # of need to backtrack placement
        if solver(board):
            return True

        # If placement fails, change back to white cell
        else:
            board[x][y].assign_cell(0)

    # If placement results in invalid solution, backtrack to find next possible
    # valid step to solve puzzle
    return False
