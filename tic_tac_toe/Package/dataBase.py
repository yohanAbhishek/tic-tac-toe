# Import custom module/package(s)
from Package import game

# Import external module/package(s)
import mysql.connector

# Create variables
total_p1 = 0
total_p2 = 0
total_draw = 0
games = 0

# Open database connection using a dictionary
conDict = {
    'host': 'localhost',
    'database': 'DOC334_CW',
    'user': 'root',
    'password': ''
}

db = mysql.connector.connect(**conDict)


def save():
    """Save game data to the database"""

    # Define global variables
    global db

    # Prepare the cursor object
    cursor = db.cursor()

    # Create sql command to execute
    insertVal = 'INSERT INTO scoreBoard(RoundNo,PlayerOne, PlayerTwo, GameName) VALUES (%s,%s,%s,%s)'

    # Execute command
    cursor.execute(insertVal, game.data)

    # Commit the changes
    db.commit()

    print('>>Your game score has been recorded\n')


def clearDb():
    """Clear database"""

    # Define global variables
    global db

    # Create a cursor object
    cursor = db.cursor()

    # Execute sql query using cursor.execute()
    cursor.execute('DELETE FROM scoreBoard')

    # Commit changes to the database
    db.commit()


def game_play():
    """Print table with saved data from the database"""

    # Define global variables
    global db

    # Create cursor object
    cursor = db.cursor()

    # execute the sql query
    cursor.execute("SELECT * FROM scoreBoard")

    # fetch all of the results using fetchall()
    result = cursor.fetchall()

    # Print headers of the table
    print('--------------------------------------------------------------------')
    print(f'gameName        | RoundNo        | Player1        | Player2        |')
    print('--------------------------------------------------------------------')

    # Loop through the result to extract the data
    for row in result:
        for item in row:
            print(str(item).center(16), end='|')
        print("\n")
    print('--------------------------------------------------------------------')


def player1():
    """Display total winnings of player 1"""

    # Define global variables
    global db, total_p1

    # Create cursor object
    cursor = db.cursor()

    # execute sql query with execute() command
    cursor.execute(
        f"SELECT COUNT(CASE WHEN gameName = '{game.p1} vs {game.p2}' THEN 1 END)FROM scoreBoard WHERE (PlayerOne = 'Won')")

    # fetch all of the results
    result = cursor.fetchall()

    # set counter(total_p1) to 0
    total_p1 = 0

    # Loop through result o count total wins of player 1
    for item in result:
        for num in item:
            total_p1 += int(num)

    # Display total wins of player 1
    return total_p1


def player2():
    """Display total winnings of player 2"""

    # Define global variables
    global db, total_p2

    # Create cursor object
    cursor = db.cursor()

    # execute sql query with execute() command
    cursor.execute(
        f"SELECT COUNT(CASE WHEN gameName = '{game.p1} vs {game.p2}' THEN 1 END) FROM scoreBoard WHERE (PlayerTwo = 'Won')")

    # fetch all the matching rows
    result = cursor.fetchall()

    # set counter(total_p1) to 0

    # fetch all of the results
    for item in result:
        for total_p2 in item:
            return total_p2


def draw():
    """Display total draw matches"""

    # Define global variables
    global db, total_draw

    # Create cursor object
    cursor = db.cursor()

    # execute sql query with execute() command
    cursor.execute(
        f"SELECT COUNT(CASE WHEN gameName = '{game.p1} vs {game.p2}' THEN 1 END)FROM scoreBoard WHERE (PlayerOne = 'Draw') AND (PlayerTwo = 'Draw')")

    # fetch all of the results
    result = cursor.fetchall()
    for item in result:
        for total_draw in item:
            # Display total draws
            return total_draw


def total_games():
    """Display total games played in a session"""

    # Define global variables
    global db, games

    # Create cursor object
    cursor = db.cursor()

    # execute sql query with execute() command
    cursor.execute(f"SELECT COUNT(CASE WHEN gameName = '{game.p1} vs {game.p2}' THEN 1 END)FROM scoreBoard")

    # fetch all of the results
    result = cursor.fetchall()

    for item in result:
        for games in item:
            # Display total games played
            return games


def current_game():
    """Print table with saved data from the database"""

    # Define global variables
    global db

    # Create cursor object
    cursor = db.cursor()

    # execute the sql query
    cursor.execute(f"SELECT * FROM scoreBoard WHERE gameName = '{game.p1} vs {game.p2}'")

    # fetch all of the results using fetchall()
    result = cursor.fetchall()

    # Print headers of the table
    print('--------------------------------------------------------------------')
    print(f"   gameName     |    RoundNo     |{game.p1.center(16)}|{game.p2.center(16)}| ")
    print('--------------------------------------------------------------------')

    # Loop through the result to extract the data
    for row in result:
        for item in row:
            print(str(item).center(16), end='|')
        print("\n")
    print('--------------------------------------------------------------------')

