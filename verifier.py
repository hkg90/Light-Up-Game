# Function that verifies if user's input solution is valid.
def verifier(board, lightBulbCells, numberedBlackBox):
    # Ensure no white spaces remain on board, if yes then return False
    for row in board:
        for cell in row:
            if cell.state == 0:
                return False
    # Check board for beams that may have more than 1 light bulb in it. If overlapping,
    # return False
    for light_bulb in lightBulbCells:
        board_range = [0, 1, 2, 3, 4, 5, 6]
        x_index = light_bulb[0]
        y_index = light_bulb[1]

        while True:
            y_index += 1
            if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 1:
                return False
        y_index = light_bulb[1]
        # Update color above light bulb
        while True:
            y_index -= 1
            if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 1:
                return False
        y_index = light_bulb[1]
        # Update color to left of light bulb:
        while True:
            x_index -= 1
            if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 1:
                return False
        x_index = light_bulb[0]
        # Update coloring right of light bulb
        while True:
            x_index += 1
            if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 1:
                return False

    # Ensure that each numbered black box has appropriate number of directly
    # adjacent light bulbs
    for box in numberedBlackBox:
        y_index = box[0] - 1
        x_index = box[1] - 1
        bulb_tally = 0
        # Check cell below numbered box (if applicable)
        y_index += 1
        if y_index in board_range and board[x_index][y_index].state == 1:
            bulb_tally += 1

        # Check cell above numbered box (if applicable)
        y_index = box[0] - 1
        y_index -= 1
        if y_index in board_range and board[x_index][y_index].state == 1:
            bulb_tally += 1

        # Check cell left of numbered box (if applicable)
        y_index = box[0] - 1
        x_index -= 1
        if x_index in board_range and board[x_index][y_index].state == 1:
            bulb_tally += 1

        # Check cell right of numbered box (if applicable)
        x_index = box[1] - 1
        x_index += 1
        if x_index in board_range and board[x_index][y_index].state == 1:
            bulb_tally += 1

        # Determine if tally is valid
        if bulb_tally != box[2]:
            return False
    return True