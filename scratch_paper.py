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







# Updates board with white or yellow ('beam') cells
# def update_cell(x, y):
#     board_range = [0, 1, 2, 3, 4, 5, 6]
#     inBeam = False
#
#     # Update cell from light bulb to white
#     elif board[x][y].state == 1:
#         # Check adjacent cells to see if row/ column is also in a 'beam'
#         if (x - 1) in board_range and y in board_range:
#             if board[x - 1][y].state == 2:
#                 inBeam = True
#         if (x + 1) in board_range and y in board_range:
#             if board[x + 1][y].state == 2:
#                 inBeam = True
#         if x in board_range and (y - 1) in board_range:
#             if board[x][y - 1].state == 2:
#                 inBeam = True
#         if x in board_range and (y + 1) in board_range:
#             if board[x][y + 1].state == 2:
#                 inBeam = True
#         if inBeam:
#             board[x][y].assign_cell(2)
#
#         # If not row/ column not in 'beam', update to white cell
#         else:
#             update_beam(x, y, 0)
#             board[x][y].assign_cell(0)