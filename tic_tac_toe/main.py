import traceback  # For error handling
import logging

try:
    # Import custom modules
    from Package import game, dataBase, my_html

    # Import external modules/packages
    import sys

    # Create dictionary to store values for the game
    dictionary = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }

    # Initialize option as empty string for the menu input
    option = ''

    # Create variable to count rounds in a session
    counter = 0

    # Continue While user doesn't enter 6 as the option from the menu which will end the program
    while option != '6':

        # Show menu and get user input for required action
        option = input('\n--MAIN MENU-- \n\n'
                       '1. Play game \n'
                       '2. Instructions \n'
                       '3. Game play history\n'
                       '4. View past game plays in a web browser\n'
                       '5. Reset\n'
                       '6. Exit game\n\n'
                       'Enter a number from the menu --> ')

        # if user inserts an invalid value
        if option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6':
            print('\n>>> Please enter a valid option!')
        print()

        # Make replay option default to yes
        replay = 'y'

        # If the user inputs 1 as his action from the menu
        if option == '1':

            # If it's the first round, get player names
            if game.RoundNo == 1:

                # Get names for player 1 and player 2
                print('>> Please enter a name with 1-5 characters\n')

                while len(game.p1) == 0 or len(game.p1) > 5:
                    game.p1 = input("Enter player 1 name --> ")

                while len(game.p2) == 0 or len(game.p2) > 5:
                    game.p2 = input("Enter player 2 name --> ")

            # While user inputs 1 from the menu and decides to replay, run the game
            while replay == 'y' or replay.upper() == 'Y' and option == 1:
                game.total_moves = 0

                # player 1 plays first
                player = 1

                # Reset the game board(dictionary) for the new round
                dictionary = {
                    '1': ' ', '2': ' ', '3': ' ',
                    '4': ' ', '5': ' ', '6': ' ',
                    '7': ' ', '8': ' ', '9': ' '
                }
                print('\n------Game started------\n'
                      '\nType (i) to view instructions'
                      '\nType (q) to quit game')
                print(f'\nRound number {game.RoundNo}\n')

                while True:
                    game.Dict(dictionary)
                    # assign the move check(module1.check) to a variable
                    stop = game.check(dictionary)

                    # break from loop if the move check(module1.check) returns True
                    if stop:
                        break

                    while True:
                        if player == 1:

                            # Get player one input and assign it to p1_input
                            p1_input = input(f"{game.p1}'s turn -> ")

                            # If user input is a valid number and is not a taken position, then save it in the dictionary
                            if p1_input.upper() in dictionary and dictionary[p1_input.upper()] == ' ':
                                dictionary[p1_input.upper()] = 'X'
                                player = 2
                                break

                            # If the input of the user is already taken in the dictionary, show an error message
                            elif p1_input.upper() in dictionary and dictionary[p1_input.upper()] != ' ':
                                print('>>> Position already taken')

                            # If user entered the quit command(Q) quit the game.
                            elif p1_input.upper() == 'Q':
                                sys.exit('>> You exited the game')

                            # If the user inputs i, show the instructions
                            elif p1_input.upper() == 'I':
                                game.instructions()

                            # If the input is not from 1-9 display error
                            else:
                                print('>>> Input not in range, please try again')

                        else:
                            # Get player two input and assign it to p2_input
                            p2_input = input(f"{game.p2}'s turn -> ")

                            # If user input is a valid number and is not a taken position, then save it in the dictionary
                            if p2_input.upper() in dictionary and dictionary[p2_input.upper()] == ' ':
                                dictionary[p2_input.upper()] = 'O'
                                player = 1
                                break

                            # If the user input holds a place in the dictionary then display error message
                            elif p2_input.upper() in dictionary and dictionary[p2_input.upper()] != ' ':
                                print('>>> Position already taken')

                            # If user entered the quit command(Q) quit the game.
                            elif p2_input.upper() == 'Q':
                                sys.exit('>> You exited the game')

                            # If the user inputs i, show the instructions
                            elif p2_input.upper() == 'I':
                                game.instructions()

                            # If the input is not from 1-9 display error
                            else:
                                print('>>> Input not in range, please try again')
                                continue

                    # On exiting the True condition Increase the number of moves by one
                    game.total_moves += 1
                    print('-------------')
                    print()

                # Save the game data onto the database
                dataBase.save()

                # Save the game data to html file
                my_html.save_html()

                # After completing a game increase the round by one
                game.RoundNo += 1
                counter += 1

                # Get user input to play a new game
                replay = input("Enter 'y' to play again, else press any key to end session --> ")

            print('\nROUND ENDED!')

        # If the user inputs 2 as his action from the menu, show game instructions
        if option == '2':
            game.instructions()

        # If the user inputs 3 as his action from the menu, show game play history
        if option == '3':

            # Initialize the new option as new_opt
            new_opt = ''
            print("-------------------------------------------")

            # While new option isn't a valid option get user input until its valid
            while new_opt != '1' and new_opt != '2' and new_opt != '3':

                # Get user input for new option
                new_opt = input('1. View game play history of the session\n'
                                '2. View entire game history\n'
                                '3. Go back\n\n'
                                'Type a valid option from the menu above --> ')

                # On wrong input show error message
                if new_opt != '1' and new_opt != '2' and new_opt != '3':
                    print("Please enter a valid option!\n")

            # If user selects 1 as the option, show the game play history of the session started
            if new_opt == '1':
                if counter != 0:
                    # This is a function to print table of game session history in a table
                    dataBase.current_game()

                    # This is a function to display total games played
                    print('\nTotal games played --> ', dataBase.total_games())

                    # This is a function to display total wins of player 1
                    print(f'\nTotal wins by {game.p1} --> ', dataBase.player1())

                    # This is a function to display total wins of player 2
                    print(f'\nTotal wins by {game.p2} --> ', dataBase.player2())

                    # This is a function to display the number of draw matches
                    print("\nTotal draw games --> ", dataBase.draw())
                else:
                    print('\nNo records to show, play a game to see your records here!')

            # If the user selects 2 as the option show the entire database
            elif new_opt == '2':

                # This is a function to print table of game session history in a table
                dataBase.game_play()

            # If the user selects 2 as the option the break out of the loop
            elif new_opt == '3':
                continue

        # If the user inputs 4 as his action from the menu, show web page
        if option == '4':

            # Initialize new option as new_opt
            new_opt = ''

            # While new option isn't a valid option get user input until its valid
            print("-------------------------------------------")
            while new_opt != '1' and new_opt != '2':
                # Get user input for new option
                new_opt = input('1. View webpage\n'
                                '2. Go back\n\n'
                                'Type a valid option from the menu above --> ')

                # If user input is invalid show error message
                if new_opt != '1' and new_opt != '2':
                    print("Please enter a valid option!\n")

            # If user selects 1 as the option, show the entire game play history in a web page
            if new_opt == '1':
                my_html.show_web()

            # If user selects option 3 then break from the loop
            elif new_opt == '2':
                continue

        # If the user inputs 5 as his action from the menu, give options to clear data
        if option == '5':

            # Initialize new option as new_opt
            new_opt = ''

            # While new option isn't a valid option get user input until its valid
            while new_opt != '1' and new_opt != '2' and new_opt != '3' and new_opt != '4':
                new_opt = input('1. Reset game\n'
                                '2. Clear web page data\n'
                                '3. Clear all\n'
                                '4. Go back\n'
                                '\nType a valid option from the menu above -->')

            # If user selects 1 as the option, clear the database that has the session data along with the current game
            if new_opt == '1':
                answer = input('\nYour session and game data will be lost, if you wish to continue type (y) --> ')
                if answer.upper() == 'Y':
                    # Reset game wins
                    dataBase.total_p1 = 0
                    dataBase.total_p2 = 0
                    dataBase.total_draw = 0

                    # Reset total games played
                    dataBase.games = 0

                    # Reset the round
                    game.RoundNo = 1

                    # Reset the player 1 and player 2 names
                    game.p1 = ''
                    game.p2 = ''

                    print('\n>> Your database and game data has been cleared successfully! ')

            # If user selects 2 as the option, clear all the html data
            if new_opt == '2':
                answer = input('\nAll your records will be deleted, if you still wish to continue type(y) --> ')
                if answer.upper() == 'Y':
                    my_html.clear_html()
                    print('\n>> Your html data has been cleared successfully! ')

            # If user selects 3 as the option, clear all the data
            if new_opt == '3':
                answer = input('\nEverything will be cleared, if you still wish to continue type(y) --> ')
                if answer.upper() == 'Y':
                    # Clear the database
                    dataBase.clearDb()

                    # Reset game wins
                    dataBase.total_p1 = 0
                    dataBase.total_p2 = 0
                    dataBase.total_draw = 0

                    # Reset the number of games played
                    dataBase.games = 0

                    # Reset the game round number
                    game.RoundNo = 1

                    # Reset player 1 and player 2 names
                    game.p1 = ''
                    game.p2 = ''

                    # Clear the web page(html) content
                    my_html.clear_html()
                    print('\n>> All the data has been cleared successfully!')

            # If user inputs 4 as the menu for the new_option, break out of the loop
            if new_opt == '4':
                continue

    # Close the db
    dataBase.db.close()

    # Display end message when the game is exited.
    print('\n--END OF PROGRAM--')

# If any errors occur use this exception

except Exception as e:  # specific exceptions has not been given so that the program can detect all errors
    logging.error(traceback.format_exc())
    print("\n>> In the report there is a section named as 'Important', if you do get any errors in the program "
          "please go through that. Possible errors include Can't connect to MySQL server, directory not found. Thank "
          "you!\n")
