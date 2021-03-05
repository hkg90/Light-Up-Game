# File contains the verifier() function that determines is an input certificate solution is valid
# or invalid. Returns True for valid and False for invalid solutions.


# Function determines if any light bulb's placement overlaps with the beam from another light bulb
def check_beams(board, cell):
    board_range = [0, 1, 2, 3, 4, 5, 6]
    x_index = cell[0]
    y_index = cell[1]

    # If cell is a white cell from solver algorithm, return True.
    # No check necessary
    if board[x_index][y_index].state == 0:
        return True

    # Checks if beam below bulb overlaps with another light bulb in column
    while True:
        y_index += 1
        if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
            break
        elif board[x_index][y_index].state == 1:
            return False
    y_index = cell[1]
    # Checks if beam above bulb overlaps with another light bulb in column
    while True:
        y_index -= 1
        if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
            break
        elif board[x_index][y_index].state == 1:
            return False
    y_index = cell[1]
    # Checks if beam left of bulb overlaps with another light bulb in column
    while True:
        x_index -= 1
        if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
            break
        elif board[x_index][y_index].state == 1:
            return False
    x_index = cell[0]
    # Checks if beam right of bulb overlaps with another light bulb in column
    while True:
        x_index += 1
        if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
            break
        elif board[x_index][y_index].state == 1:
            return False
    # If valid, return True
    return True


# Function ensures that each numbered black box has the appropriate number of directly
# adjacent light bulbs.
# Example: A numbered 2 box requires exactly 2 light bulbs to be directly adjacent to it.
def check_num_boxes(board, box):
    board_range = [0, 1, 2, 3, 4, 5, 6]
    x_index = box[0]
    y_index = box[1]
    inner_number = board[x_index][y_index].state - 4
    bulb_tally = 0
    # Check cell below numbered box (if applicable)
    y_index += 1
    if y_index in board_range and board[x_index][y_index].state == 1:
        bulb_tally += 1

    # Check cell above numbered box (if applicable)
    y_index = box[1]
    y_index -= 1
    if y_index in board_range and board[x_index][y_index].state == 1:
        bulb_tally += 1

    # Check cell left of numbered box (if applicable)
    y_index = box[1]
    x_index -= 1
    if x_index in board_range and board[x_index][y_index].state == 1:
        bulb_tally += 1

    # Check cell right of numbered box (if applicable)
    x_index = box[0]
    x_index += 1
    if x_index in board_range and board[x_index][y_index].state == 1:
        bulb_tally += 1

    #x_index = box[0]
    # Determine if tally is valid
    if bulb_tally != inner_number:
        return False

    # If valid, return True
    return True


# Function that verifies if user's input certificate solution is valid or invalid.
def verifier(board):
    for row in board:
        for cell in row:
            # Ensure no white spaces remain on board, if yes then return False
            if cell.state == 0:
                return False
            # Checks if multiple light bulbs exist within the same beam (row and/ or column of beams)
            if cell.state == 1:
                if not check_beams(board, [cell.x, cell.y]):
                    return False
            # Ensures that each numbered black box in board has appropriate number of directly
            # adjacent light bulbs
            if cell.state in [4, 5, 6, 7, 8]:
                if not check_num_boxes(board, [cell.x, cell.y]):
                    return False
    # If solution is valid, return True
    return True
