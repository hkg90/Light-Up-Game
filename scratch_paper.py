#
    # # Determine if row have another light bulb in it
    # col_bulb, row_bulb = False, False
    # while True:
    #     y_index += 1
    #     if y_index not in board_range or board[x][y_index].state in \
    #             range(3, 9):
    #         break
    #     # Another bulb exists in row
    #     if board[x][y_index].state in [1]:
    #         row_bulb = True
    # y_index = y
    # while True:
    #     y_index -= 1
    #     if y_index not in board_range or board[x][y_index].state in \
    #             range(3, 9):
    #         break
    #     # Another bulb exists in row
    #     if board[x][y_index].state in [1]:
    #         row_bulb = True
    # y_index = y
    #
    # # Determine if column has another light bulb in it
    # while True:
    #     x_index -= 1
    #     if x_index not in board_range or board[x_index][y].state in \
    #             range(3, 9):
    #         break
    #     # Another bulb exists in column
    #     if board[x_index][y].state in [1]:
    #         col_bulb = True
    # x_index = x
    # # Add 'beam' below light bulb
    # while True:
    #     x_index += 1
    #     if x_index not in board_range or board[x_index][y].state in \
    #             range(3, 9):
    #         break
    #     # Another bulb exists in column
    #     if board[x_index][y].state in [1]:
    #         col_bulb = True
    # x_index = x

# # Update row coloring if bulb does not already exist within row
    # if not row_bulb and new_state == 2: