# Initialize variables

data = ''  # To store data to be sent to the database
total_moves = 0  # To store total moves
RoundNo = 1  # To store total rounds

# Create empty strings as p1 and p2 for player 1 and player 2
p1 = ''
p2 = ''


def Dict(dictionary):
    """Print the dictionary with valid user input values"""
    print(
        f" {dictionary['1']} | {dictionary['2']} | {dictionary['3']} \n"
        f" _________\n"
        f" {dictionary['4']} | {dictionary['5']} | {dictionary['6']} \n"
        f" _________\n"
        f" {dictionary['7']} | {dictionary['8']} | {dictionary['9']} \n")


def check(dictionary):
    """Check if there is a possibility that is satisfied to win"""

    # Define global variables
    global p1, p2, data, RoundNo

    # Return 1 if a condition is satisfied

    # Check Player two's move for win

    # In the horizontal axis
    if dictionary['1'] == 'X' and dictionary['2'] == 'X' and dictionary['3'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True
    if dictionary['4'] == 'X' and dictionary['5'] == 'X' and dictionary['6'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True

    if dictionary['7'] == 'X' and dictionary['8'] == 'X' and dictionary['9'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True

    # The diagonal
    if dictionary['1'] == 'X' and dictionary['5'] == 'X' and dictionary['9'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True

    if dictionary['3'] == 'X' and dictionary['5'] == 'X' and dictionary['7'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True

    # In the vertical axis
    if dictionary['1'] == 'X' and dictionary['4'] == 'X' and dictionary['7'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True
    if dictionary['2'] == 'X' and dictionary['5'] == 'X' and dictionary['8'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True
    if dictionary['3'] == 'X' and dictionary['6'] == 'X' and dictionary['9'] == 'X':
        print(f'{p1} won!')
        data = str(RoundNo), 'Won', 'Lost', f'{p1} vs {p2}'
        return True

    # Check Player two's move for win

    # In the horizontal axis
    if dictionary['1'] == 'O' and dictionary['2'] == 'O' and dictionary['3'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True
    if dictionary['4'] == 'O' and dictionary['5'] == 'O' and dictionary['6'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True
    if dictionary['7'] == 'O' and dictionary['8'] == 'O' and dictionary['9'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True

    # In the diagonals
    if dictionary['1'] == 'O' and dictionary['5'] == 'O' and dictionary['9'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True
    if dictionary['3'] == 'O' and dictionary['5'] == 'O' and dictionary['7'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True

    # In the vertical axis
    if dictionary['1'] == 'O' and dictionary['4'] == 'O' and dictionary['7'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True
    if dictionary['2'] == 'O' and dictionary['5'] == 'O' and dictionary['8'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True
    if dictionary['3'] == 'O' and dictionary['6'] == 'O' and dictionary['9'] == 'O':
        print(f'{p2} won!')
        data = str(RoundNo), 'Lost', 'Won', f'{p1} vs {p2}'
        return True

    # Check if the game is draw
    elif total_moves == 9:
        print("Game is a draw!")
        data = str(RoundNo), 'Draw', 'Draw', f'{p1} vs {p2}'
        return True

    # Return False if the game wasn't a draw or won by any player
    return False


def instructions():
    """Show gameplay instructions"""
    print(f'\n--INSTRUCTIONS--\n\n'
          # Print the game board numbering system and other instructions
          f'01. Given below is the interface\n'
          '\n-ROWS AND COLUMNS-\n\n'
          'R |       1 | 2 | 3\n'
          'O |  |    _________\n'
          'W |  v    4 | 5 | 6\n'
          'S |       _________\n'
          '          7 | 8 | 9\n\n'
          '             -->           \n'
          '         _____________ \n'
          '         C O L U M N S\n\n\n'
          f'02. To beat the other player get three of your characters (X or O) in a row, column or diagonal!\n'
          f'\n03. To quit during the game enter Q.\n\n'
          '--------------------------------------\n')
