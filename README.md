# tic-tac-toe
python(3.x version) program which will allow the user to play a game called “Noughts and Crosses”, also known as “tic-tac-toe”.

This is a simple board game played by 2 human players. Two players are supposed to draw noughts and crosses taking turns on a board. Player 1 may draw noughts while player 2 may draw crosses. The player who can place their symbol diagonally, horizontally, or vertically in a row is the winner of the game.
1. If both players failed to draw 3 of his/her symbols in a row (diagonally, horizontally, or vertically) the game is a draw.
2. A player who can place 3 of his/her symbols diagonally, horizontally, or vertically in a row; before the other player is the winner of the game.

The player is able to do below tasks.
(01) View the past game play history - This is stored by using database
(02) Two players must be able to play this game as many times they like. (Players must also can exit the game as they desire at any time)
(03) The program keeps track of wins, losses and draws of each player. 
(04) The program is able to display stats like below. 
  i) Total game plays
  ii) Total wins by player 1
  iii) Total wins by player 2
  iv) Total draws
  
When the program is run, a menu will be shown with 6 options as shown as bellow.
  
![image](https://user-images.githubusercontent.com/100549603/219430963-bd99b2f0-60e3-4fd2-a0fa-7b4d982372f6.png)

When the user inputs a valid option, it will direct the user to the relevant option. Below are the outputs of the relevant user inputs.

![image](https://user-images.githubusercontent.com/100549603/219431024-da253120-d050-434e-b812-12d57b218d09.png)

As it clearly states, option 1 will commence the game. If this is the round one of a session between two players, it will ask for the names of player 1 and player 2. After the users have entered a name with 1-5 characters, the game will start. As shown in the screen shot, the user will have the option to quit(q) the game or view the instructions(i) at any time of playing game.

When a user wins, the program will display a message saying who won, if it’s a draw it will display ‘Game was a draw’. If the user wishes to, he/she can replay the game by typing ‘y’, if they wish to go back to the main menu, they can type any other key.

![image](https://user-images.githubusercontent.com/100549603/219431195-136fd93a-8997-4ca6-9462-4bc0fde370ff.png)

There are two types of possible invalid inputs for this program when playing the game. First invalidation is when a user enters a number/character which is not in the range of 1-9, since the game board has only 9 slots. In such a case, the program will display an error message as shown in this screen shot.

![image](https://user-images.githubusercontent.com/100549603/219431272-cf4abfd6-47a0-473a-90a9-4f333c1d93e1.png)

If the user selects option 2 from the menu it will display the game instructions as shown below. The game instructions can be accessed while playing the game as well by typing "i".

![image](https://user-images.githubusercontent.com/100549603/219431579-c96160b3-19d5-4fcf-9ea0-c38ab676ef1f.png)

Through the option 3 the user will be given access to view the game play history. When the user selects option 3, the program will show a sub menu with three options as show bellow.

![image](https://user-images.githubusercontent.com/100549603/219431699-f8426e62-03f2-45be-9e19-ddf951408ebb.png)

When the option 4 is chosen, it will display a sub menu with two options, in case the user came into the option 4 through the main menu by accident, then he/she can go back through the second option to the main menu.

![image](https://user-images.githubusercontent.com/100549603/219431797-13203f68-607b-4339-a2ff-e1bccea5247f.png)

Option one in the sub-menu will redirect the user to a webpage, a sample of a few game plays is given below. The web page includes the names of the two players, including the time and date they started.

![image](https://user-images.githubusercontent.com/100549603/219431835-f0d6749d-ee9f-46ea-b90d-3d747d648d03.png)
