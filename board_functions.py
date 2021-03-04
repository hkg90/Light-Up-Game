# File contains function that performs cell value updates to the game board


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
def reset(board, lightBulbCells):
    # Reset status of light bulb cells to white
    for light_bulb in lightBulbCells:
        x = light_bulb[0]
        y = light_bulb[1]
        board[x][y].assign_cell(0)

    # Clear list
    lightBulbCells.clear()

    # Reset yellow 'beam' cells to white
    for col in board:
        for cell in col:
            if cell.state == 2:
                cell.assign_cell(0)



# Function updates board with beams of each light bulb present (if applicable)
def update_beams(board):
    board_range = [0, 1, 2, 3, 4, 5, 6]
    lightBulbCells = []
    # Clear board of old beams
    for col in board:
        for cell in col:
            if cell.state == 1:
                lightBulbCells.append([cell.x, cell.y])
            elif cell.state == 2:
                cell.assign_cell(0)

    # Update color along right side of light bulb
    # Add beam for each light bulb in board
    for light_bulb in lightBulbCells:
        x_index = light_bulb[0]
        y_index = light_bulb[1]
        # Update color below light bulb
        while True:
            y_index += 1
            if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)

        y_index = light_bulb[1]
        # Update color above light bulb
        while True:
            y_index -= 1
            if y_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)

        y_index = light_bulb[1]
        # Update color to left of light bulb:
        while True:
            x_index -= 1
            if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)

        x_index = light_bulb[0]
        # Update color right of light bulb
        while True:
            x_index += 1
            if x_index not in board_range or board[x_index][y_index].state in range(3, 9):
                break
            elif board[x_index][y_index].state == 0:
                board[x_index][y_index].assign_cell(2)


