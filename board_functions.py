# File contains functions that perform cell value and game board updates in response
# to user's choices, verifier.py or solver.py's needs.


# Function loads game board black box setup from .txt file and
# initializes blank and numbered black boxes into board
def load_black_boxes(board, blankBlackBox, numberedBlackBox):
    # Open file
    new_file = open('gameboards/board1.txt', 'r')
    num_blank = int(new_file.readline())
    for i in range(num_blank):
        blank = new_file.readline()
        if '\n' in blank:
            blank = blank.strip()
        divided = list(map(int, blank.split(',')))
        blankBlackBox.append(divided)

    num_numbered = int(new_file.readline())
    for i in range(num_numbered):
        num_box = new_file.readline()
        if '\n' in num_box:
            num_box = num_box.strip()
        divided = list(map(int, num_box.split(',')))
        numberedBlackBox.append(divided)

    # Assign blank black background cells
    for cell in blankBlackBox:
        col = cell[0] - 1
        row = cell[1] - 1
        new_state = 3
        board[row][col].assign_cell(new_state)

    # Assign numbered black background cells
    for cell in numberedBlackBox:
        col = cell[0] - 1
        row = cell[1] - 1
        new_state = cell[2] + 4
        board[row][col].assign_cell(new_state)


# Function resets the board to initial state (removes all light bulbs and 'beams')
def reset(board):
    for col in board:
        for cell in col:
            if cell.state in [1, 2, 9]:
                cell.assign_cell(0)


# Function updates board with beams of each light bulb present (where applicable)
def update_beams(board):
    board_range = [0, 1, 2, 3, 4, 5, 6]
    light_bulb_cells = []
    # Clear board of old beams and find light bulbs in board
    for col in board:
        for cell in col:
            if cell.state == 1:
                light_bulb_cells.append([cell.x, cell.y])
            elif cell.state == 2:
                cell.assign_cell(0)

    # Add beams for each light bulb in board
    for light_bulb in light_bulb_cells:
        x_index = light_bulb[0]
        y_index = light_bulb[1]

        # Update color below light bulb
        while True:
            y_index += 1
            if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)

        # Update color above light bulb
        y_index = light_bulb[1]
        while True:
            y_index -= 1
            if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)

        # Update color to left of light bulb:
        y_index = light_bulb[1]
        while True:
            x_index -= 1
            if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)

        # Update color right of light bulb
        x_index = light_bulb[0]
        while True:
            x_index += 1
            if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)


