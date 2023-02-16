# Import custom module/package(s)
from Package import game

# Import external module/package(s)
import mysql.connector
import webbrowser
from datetime import date, datetime
import os


def save_html():
    """Save game results as html to show in web page"""
    stat = ''

    # Open database connection using a dictionary
    conDict = {
        'host': 'localhost',
        'database': 'DOC334_CW',
        'user': 'root',
        'password': ''
    }

    db = mysql.connector.connect(**conDict)

    # Create cursor object
    cursor = db.cursor()

    # execute the sql query
    cursor.execute(
        f"SELECT COUNT(CASE WHEN gameName = '{game.p1} vs {game.p2}' THEN 1 END)FROM scoreBoard WHERE ("
        f"PlayerOne = 'Won') and RoundNo = '{game.RoundNo}'")

    # fetch all of the results using fetchall()
    result1 = cursor.fetchall()
    print()
    for item in result1:
        for num in item:
            if num == 1:
                stat = 'Player one won!'

    # execute the sql query
    cursor.execute(
        f"SELECT COUNT(CASE WHEN gameName = '{game.p1} vs {game.p2}' THEN 1 END)FROM scoreBoard WHERE ("
        f"PlayerTwo = 'Won') and RoundNo = '{game.RoundNo}'")

    # fetch all of the results using fetchall()
    result2 = cursor.fetchall()

    for item in result2:
        for num in item:
            if num == 1:
                stat = 'Player two won!'

    cursor.execute(
        f"SELECT COUNT(CASE WHEN gameName = '{game.p1} vs {game.p2}' THEN 1 END)FROM scoreBoard WHERE ("
        f"PlayerOne = 'Draw') and RoundNo = '{game.RoundNo}'")
    # fetch all of the results using fetchall()
    result3 = cursor.fetchall()
    for item in result3:
        for num in item:
            if num == 1:
                stat = 'Game was a draw'

    fo = open(f"{os.getcwd()}/Package/game_play.html", 'a')

    # To print data
    day = date.today()
    d2 = day.strftime("%B %d, %Y")

    # To print time
    time = datetime.now()
    current_time = time.strftime("%H:%M:%S")

    if game.RoundNo == 1:
        heading = f'''

         <html>
                <h3
                style="font-family:courier;">This is the session of {game.p1} vs {game.p2}
                (Started on {d2} at {current_time})
                </h3>
                <br>
        </html>

        '''

        fo.write(heading)
        fo.seek(0)
    body = f'''<html>
    <body>

    <pre> ___________________________</pre>
    <pre>| RoundNo |   Game status   |</pre>
    <pre>|---------------------------|</pre>
    <pre>| {game.RoundNo}       | {stat} |</pre>
    <pre>|___________________________|</pre><br>

    </body>
    </html>
    '''

    fo.write(body)
    fo.close()


def show_web():
    """Open the htl file to show the webpage with game play history"""
    file = 'file:///' + os.getcwd() + '/' + 'Package/game_play.html'
    webbrowser.open_new_tab(file)


def clear_html():
    """Clear all the html data"""
    fo = open("Package/game_play.html", 'w')

    data = ''''''
    fo.write(data)
    fo.close()
