import PySimpleGUI as sg
import random
import sys

# Reference light bulb .png file: https://iconarchive.com/search?q=lightbulb

# Light Up Game GUI

font = 'Arial 16 bold'
# width and height of board, 7x7 grid
width = 7
height = 7
blankBlackBox = []
numberedBlackBox = []
restart = True
size = (30, 30)
# PNG images graphic's Base64 byte string
lightBulbIcon = b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAidJREFUeNp0U89rE0EU/ja7kZRWQwOS2sRgEayiRFGp9JBL/oN4EbyJtSG3eFFEpEUvHiMUpPXoteCPP8CbF1FQY6vWom2zCdt00yZx0242u7O+nbVl3awP3sybN9/73puZN4Jt2/DLm9lwjqZp0om/rnekC9nZ3gs/VvASUGCCpvupKzcK8XQOA9Ek9+utKpTyK8jvn88zs/uIiKr7MZKXLSRFHpzNPcnHTpyHbW7D7v3i/sjQAMYyUxgey+SXX94WyXXrIMaT/fqx9NX8cGIUbPcTbKMCmCpXx3Z80XgMI+nclIPtIyApjJyZgLX7GaynBqqzFz91kWODCC6IwjcquwFx6DJsq032lquWBnHwErdFfOXYIALL6qzA2vuJnroI6XCG7kGj4A4RTnKfpVdgapzACrrED53tZvbIUZOYmmDKM0SOz1CKCPS1u7DZb9AAraHtP2tfBU/lpXUwy6KsJpjRoHPX+ZFYb8f10V51eYNj+wjobRc1tTEnl9d4JledHrEP1vKXdWiqOudtKMnXWHeU1aoYkoTC6OmkG+yMFKys1KD8kJ3M9/7pHe+CmPdoeri5uulmhVsBM03UvtccyGPCaN4YfwV4O/5RidVfw6iP4+RgEnV1C+Wla6jokyx87uZG1ocPIUBCUhSxaII+ShhhegXTOIR2hwVjg5yGYaDVanN7p9lEt6vjfyIEfWdHisXivKIo0w5ZKpVaKJVK+SDcHwEGAD5qJSG2+HXsAAAAAElFTkSuQmCC'
blkBlank = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAA0SURBVFhH7c6xDQAgDANBh/13TijYIQX3kuX2KknfrXXerwUAAAAAAAAAAAAAAAAA8DsgGSESAT8rDAeCAAAAAElFTkSuQmCC'
blkZero = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAF2SURBVFhH7VdBbsQgDHT7liSHKC/gQbyHc1/RE/1BXxD1EOcv1M7ShoAJbFSJrrQjjdZrWWTweAn7AgCO2Ayv/rMZHlGAAqUNWERwzgXk7whoDWjlSyvBM1Cm0hst0uMqgEbJ66QUkxHpwbQo8x6wiJKQ5jPAEJWF1NLW0Tjy2teorSatu/VNR+tFFJM7lXGp7dKiNCPeqhhWx7U7/78Fyghjb3m3cr1o10l9sQPT0Plox7rMPkrx9v7howD9SKeHjIIABWPvwwD49emjSnQDTD6MURAwgdCAc8wLrD6swYUhXOHEgQx6GDMeNP8VPAVcENDBkBvpLBByP5yCgBmWe0b6Ai5Z0OdGmjEN1KMI60JbyUM8In/4F0dx4U4gJnfKh3vl25DFozO/r22RYjKgclITDvcBuqpxTVJHNUwyLFrzQDF5pNiFEm47L+z+Qa5kTGXsRsmNFEXfQ4rJPNlvuptjpAQpwbRGlzw/sLkFzz+njQUAfAO0ngHpWmnk2wAAAABJRU5ErkJggg=='
blkOne = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAADESURBVFhH7ZdBDoIwEEU/nkU2HqGeAA8C15ElHqScgBu4K3epfyZsSCpqUi0m85KXJk1gPpSSaQUg0mIclrEY/xPAtR4hRjU+0bdQP2E7gGvhA29Mp6HBkVNiTna6BHzdYpgGNHxk8VskA7hTra7rzhi7Tu3nZSoDL5aARXsWpeeqxuV2V3NS/BsQ5E/4pk69ci+m4BZU09em3eku+CEWwAJYAAtgAYoHSJ8LpCMikX1gDsZOyoC9hA4rbAnsaGYBCgcAHtHEctzwtkS+AAAAAElFTkSuQmCC'
blkTwo = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAFuSURBVFhH1ZbNbcMwDIWZzpJcMgI3aAdRjl1F13YQZYJmgiCHsruoFK0U/nmW7TiNnQd8oEFYokzSkjZEFJXF9JLtsJjJ+WCIRIqxiUjyB/KOifOQMRq/gH9UKkEPHF0QY5IkRE2EgedtgJzOmBq3IfGGlqM1dwfgZG/U40vwra/S7HjNjlJScLV5AWvtgVwCzUFwbOD3KlzIn4sU0lx4XAY6J8GlMgws4C4lOF0kP03X4j1wlwXwfpefuvr5PuenfsHajCM1J0fcAskp0Q9sRvMOIxfMxI9Xsw0dD2Y2b59m+7T2s6BE2if0L7N0t1Wlfij9GegcpLT5iC9vXHWeswRzdj4AdEJS4N7g44/fNtDZpVx0C3xD8GfoAXA5+dPtaa8DnRU5MK663vv0nQQcOx7kvF5I+lQFx2OnsXgPwMNIfzWzX+9bs3N1PKQwROhcekgGdns2kOAC0hVrzjWrLbmcDKR19sAjtXAGiH4B+bdvSXOmRtQAAAAASUVORK5CYII='
blkThree = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAGRSURBVFhH7Ze7ccMwDIaRzCK5yGUCjJA0qTICU2aJdGlYewT3lieIRkgRaBcaACWfbIGibMcnx5f/7jv6YFF8ASB0BwCBmU33bTubpk0AneIrUogChDCESP4jqBwCSrfYOys5AgNUeEB+9wmiSvEIij2GYhld4O7K2SKv8G4Y4yiGEX2Qde/W3q7GISr7z/Jk+cHcRlWu16fH7E4oMmYmR0ARd7BiC96xwa4diHzyPabxSJwy5jepCfyRPHBhmVtzDOhJsRU9YyQXmMY8Eo4Slpn4k7MfcUDBNO5wJ2WjGD1TIugiPtBsCH64FXK6fidMO9dEdWnceHeLaZyAnC8GdH7SXdBdSIeX0i9VRPHm9/Sl7XuhzUCbNxkO4GmpjepWMmGtrNaNklL5gEpft7IDUY+LQkmJvmulr+vMAxr7XPoKlXd2KdbBJZkUrtniNRGGzMBwYv5PSSZ25G14dvYTtRkwV5anE5F8jLD86wssnkv9XRbRwQZu1sTQa2it7efHCpb1vrOlNLsT/n+czjwBgC3+Qv2qvb+n/QAAAABJRU5ErkJggg=='
blkFour = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAFBSURBVFhH7Zc7coMwEIZ/5yxJ4yPoBslBlNJp3FG6S6OUzkHECZIjuAjcRdld8ZAJ2GAUgx/fzDeMGthd/QNiAcCRk/FQXCfjQgvQRsycg+swM0rsA2dggMoZejJ7EKvF9nvUDp+ATrB6hBiDAQVo0W6f/VLIkabeU7mcECqzFsP+kb5j8wPxVHoWoJHQprMeHnmOj82nX46gVwFl51X31Dn79l2sR3CkAB+8unPGdx6je2beIdR2KzaDx6OPMX6muwBlsKYns554wQvpLEAnK/DOV7sfMXghfwugzsvua+IGL2R+IeTRl+OviBy8kP0CzhS8JvX3WdviYx4bvq919FrbOwuwZ8rAk7hsOSDNL4T/QybuWkI8+r9AGb458NU8o6Wvclm8HA7wrWxBN1dQwI4ywDbI6ZzIHuP+czpxAcAvccQX5Z33KBAAAAAASUVORK5CYII='
whiteIcon = \
    b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAySURBVFhH7c6xAQAgCMTAx/13Bgt3oPDSpL3qWxY772sBAAAAAAAAAAAAAAAAAPwOSAZNiAQ82P7MAwAAAABJRU5ErkJggg=='
yellowIcon = \
    b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAA0SURBVFhH7c4xAQAgDMTAL/7V1kBZ8NCBy5L1ajqTxc77WgAAAAAAAAAAAAAAAAAAvwOSC24gAzAPqVgaAAAAAElFTkSuQmCC'

# 0: white space, 1: light bulb image, 2: black box, 3: lit up (yellow space)

image = [whiteIcon, lightBulbIcon, yellowIcon, blkBlank, blkZero, blkOne, blkTwo,
         blkThree,
         blkFour]
color = [('black', 'white'), ('black', 'white'), ('black', 'yellow'), ('black',
                                                                    'black'), ('black', 'black'), ('black','black'), ('black','black'), ('black','black') , ('black','black') ]



# Setting for menu buttons
def menu_buttons(text, key=None, disabled=False, button_color=('grey',
                                                               'blue')):
    return sg.Button(text, pad=(10, 10), font=font, focus=False,
                     key=key, disabled=disabled, button_color=button_color)

# Create button for each grid in board game
def grid_button(x, y):
    board[x][y] = button(x, y)
    return board[x][y].button

def load_black_boxes():
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




# Class for game board's button objects
class button():

    def __init__(self, x, y):
        self.x          = x
        self.y          = y
        self.state      = 0
        self.color      = color[self.state]
        self.disabled   = False
        self.key        = (x, y)             # keys can be ANYTHING,
        # not just strings
        self.num        = 0
        self.button     = sg.Button('',
            auto_size_button=False,
            border_width=2,
            button_color=self.color,
            disabled=self.disabled,
            focus=False,
            font=font,
            image_size=size,
            image_data=image[self.state],
            key=self.key,
            pad=(1,1))

    def assign_cell(self, state):
        self.state = state
        # Update cell to white cell, light bulb cell or 'beam' cell
        if state in [0, 1, 2]:
            text = ' '
        # Update cell to black background with inside cell text ('' or number)
        elif state > 2:
            self.disabled = True
            text = ' '
        # # Update cell to 'beam' color
        # elif state == 3:
        #     text = ' '
        # Update
        self.color = color[self.state]
        window[self.key].Widget['disabledforeground'] = 'black'

        self.button.Update(text=text, disabled=self.disabled,
                           image_data=image[self.state], image_size=(29, 29),
                           button_color=self.color)


# Initialize board theme and grid size
sg.change_look_and_feel('DarkBlue')
board = [[0 for j in range(height)] for i in range(width)]


# Create layout of window
layout = [[menu_buttons('Reset Board', key='-New Game-'), menu_buttons(
    'Solve', key='-Solve Game-'), menu_buttons(
    'Check: Did I win?', key='-Solve Game-'),]]+[[grid_button(x, y) for x in range(
    width)] for y in range(height)]

# Create window to display game board
window = sg.Window('Light Up', layout=layout, finalize=True)

# Read input game board file for game board's black boxes and respective
# positions in board
load_black_boxes()


# Main code to run the game
while True:
    event, values = window.read()

    # Close game if window closed
    if event == None:
        break
    x, y = event

    # Add light bulb if cell is white or yellow
    if board[x][y].state == 0 or board[x][y].state == 2:
        board[x][y].assign_cell(1)
    # Update cell from light bulb to white
    elif board[x][y].state == 1:
        # Check adjacent cells to see if row/ column is also in a 'beam'
        inBeam = False
        range = [0, 1, 2, 3, 4, 5, 6]
        if (x-1) in range and y in range:
            if board[x-1][y].state == 2:
                inBeam = True
        if (x+1) in range and y in range:
            if board[x+1][y].state == 2:
                inBeam = True
        if x in range and (y-1) in range:
            if board[x][y-1].state == 2:
                inBeam = True
        if x in range and (y+1) in range:
            if board[x][y+1].state == 2:
                inBeam = True
        if inBeam:
            board[x][y].assign_cell(2)

        # If not row/ column not in 'beam', update to white cell
        else:
            board[x][y].assign_cell(0)
