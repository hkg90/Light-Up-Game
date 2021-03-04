import PySimpleGUI as sg
import board_functions as func
import verifier as algo
import solver as auto


# Reference light bulb .png file: https://iconarchive.com/search?q=lightbulb

# Global constants for setting up game board:
font = 'Arial 16 bold'
width = 7 # width and height of board, 7x7 grid
height = 7
blankBlackBox = []
numberedBlackBox = []
lightBulbCells = []
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
whiteIcon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAySURBVFhH7c6xAQAgCMTAx/13Bgt3oPDSpL3qWxY772sBAAAAAAAAAAAAAAAAAPwOSAZNiAQ82P7MAwAAAABJRU5ErkJggg=='
yellowIcon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAA0SURBVFhH7c4xAQAgDMTAL/7V1kBZ8NCBy5L1ajqTxc77WgAAAAAAAAAAAAAAAAAAvwOSC24gAzAPqVgaAAAAAElFTkSuQmCC'

# 0: white space, 1: light bulb image, 2: black box, 3: lit up (yellow space)

image = [whiteIcon, lightBulbIcon, yellowIcon, blkBlank, blkZero, blkOne, blkTwo,
         blkThree, blkFour, yellowIcon]
color = [('black', 'white'), ('black', 'yellow'), ('black', 'yellow'),
         ('black', 'black'), ('black', 'pink'), ('black', 'pink'), ('black', 'pink'), ('black', 'pink'), ('black', 'black'), ('black', 'yellow')]

# Setting for menu buttons
def menu_buttons(text, key=None, disabled=False, button_color=('grey',
                                                               'blue')):
    return sg.Button(text, pad=(10, 10), font=font, focus=False,
                     key=key, disabled=disabled, button_color=button_color)


# Function creates buttons for each cell in board game
def grid_button(x, y):
    board[x][y] = button(x, y)
    return board[x][y].button





# Class for game board's button objects
class button():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 0
        self.color = color[self.state]
        self.disabled = False
        self.key = (x, y)
        self.num = 0
        self.button = sg.Button(' ',
            auto_size_button=False,
            border_width=2,
            button_color=self.color,
            disabled=self.disabled,
            focus=False,
            font=font,
            image_size=size,
            image_data=image[self.state],
            key=self.key,
            pad=(1, 1))

    # Function assigns new state to selected cell in board
    def assign_cell(self, state):
        self.state = state
        # Update cell to white cell, light bulb cell or 'beam' cell
        if state in [0, 1, 2, 9]:
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
                           image_data=image[self.state], image_size=(size),
                           button_color=self.color)


#~~~ Initialize board theme and grid size ~~~#

#Set theme of GUI
sg.change_look_and_feel('DarkBlue')

# Initialize board grid
board = [[0 for j in range(height)] for i in range(width)]

# Create layout of GUI window
layout = [[menu_buttons('Reset Board', key='-Reset Game-'), menu_buttons(
    'Auto-Solve', key='-Solve Game-'), menu_buttons(
    'Submit', key='-Check Game-'),]]+[[grid_button(x, y) for x in range(
    width)] for y in range(height)]

# Create window to display game board
window = sg.Window('Light Up', layout=layout, finalize=True)

# Read input game board file for game board's black boxes and respective
# positions in board
func.load_black_boxes(board, blankBlackBox, numberedBlackBox)

# Main code to run the game/ runs game logic
while True:
    event, values = window.read()

    # Exit game if window closed
    if event == None:
        break

    # Clear board if user hits "Reset" button
    elif event == '-Reset Game-':
        func.reset(board, lightBulbCells)
        func.update_beams(board)

    # Initiate 'Solver'
    elif event == '-Solve Game-':
        cells_to_try = auto.setup_solver(board, numberedBlackBox)
        auto.solver(board, cells_to_try)

    # Initiate 'Verifier'
    elif event == '-Check Game-':
        game_result = algo.verifier(board, lightBulbCells, numberedBlackBox)
        if game_result:
            sg.popup('You win!', title='Note:')
        else:
            sg.popup('You lost... Try again!', title='Note:')

    else:
        x, y = event

        if board[x][y].state == 1:
            board[x][y].assign_cell(0)
            lightBulbCells.remove([x, y])
        elif board[x][y].state in [0, 2]:
            board[x][y].assign_cell(1)
            lightBulbCells.append([x, y])
        func.update_beams(board)



