# MineSweeper !

![image](https://github.com/user-attachments/assets/28300b09-9fc9-4cfd-8a41-2bc68db6de54)

MineSweeper orginally created in 1990 by microsoft as a single player computer game. This game follows the same style of rules and outcome. The Main goal of the game is to correctly figure out where the bombs are located on the board without hitting there locations. This is mainly done logic and at time partly guessing (depending how good you are). The game supplies the player with a numer which referes to the numer of near by bombs. From thi information the player can work out which locations are safe and which have a hidden bomb. If the board is completed the player get a nice WELL DONE! message.

Deployed version of Heroku can be found [here](https://minesweeper-python-56b9c81700d5.herokuapp.com/)


## User Experience (UX)

### Site Purpose
The purpose of this game was to be a fun logical puzzle game. Where a player can test there ability to figure out how to complete the gameboard without hitting a bomb.

### Audience
This game was created for minesweeper fans, also in general this a fun game to play/

### Communication
Game proives clear intructions and also input location. Additionally, it has ASCII art which displays a colourful phrases on the games progression, example GAMEOVER or WELL DONE!!

### User Goals
The goal is to clear the hidden game board by tpying in specific locations to the input section. However, the board has hidden bombs. The game provides hints in the form of numbers of how many bombs there are in a 3x3 area. For example if the number is 0 there are no bombs with a 3x3 area of that 0.

### Future Goals
Difficulty levels. This can be done by adding three game modes which have more or less number of bombs.


### Flowchart
![image](https://github.com/user-attachments/assets/376a09af-c368-44bf-8f3a-81bcadd92daa)



## Features
- At the start game overview and intructions are displayed
  
  ![image](https://github.com/user-attachments/assets/7a9e4dd1-207d-4d48-a878-65da3705a3e7)

- Player can then scroll down and the Game board with all the hidden locations is revealed
  
  ![image](https://github.com/user-attachments/assets/1fac627d-7399-45e0-8d92-c2dd2f7c77f0)

- The player is promted by the input intrcutions to choose a starting row and collumn. To start this is completely random and the player has no prior knowleadge of where the bombs may be.
  
  ![image](https://github.com/user-attachments/assets/2f4da074-fe21-4c07-b40f-100e69175642)

- Based on the chosen location the player the sees various numbers, representing the number of surrounding bombs. These locations are randomised each new game.
  
  ![image](https://github.com/user-attachments/assets/1e6478dd-b12d-4b8e-811b-5e73324ba89e)

- Altneratively, the player hit a bomb or they continued and eventually hit a bomb. GAMEOVER! displayed.
  
  ![image](https://github.com/user-attachments/assets/c42f6919-b1b7-42bd-80b3-1b8ceadecf90)

- If the player outsmarts the game they can workout the bomb locations. The use of flags (blue 'f') can provide a helpful reminder of where not to dig. 

![image](https://github.com/user-attachments/assets/eaf5fb3a-e373-42ea-844c-9d5d7664aae0)

- A WELL DONE!! ASCII message is displayed. A sense of satisfaction and complistion.

  ![image](https://github.com/user-attachments/assets/62d368e0-c5bc-44e5-82b4-af6947766955)




### Error Handling



### Future Features
- Add different levels
- A highscore option, based on how fast you finish the board




## Testing
- Tested on GIThub and Horoku.
- Tested by mentor Spencor.
- Tested by my dad (big minesweeper fan)
- Ran Code through  CI Python Linter




### Feature testing
-   tested that all functions running the game was working as it should by checking:
  ![image](https://github.com/user-attachments/assets/35a87820-0553-4391-abad-bfc8a11cbd29)





### Validator Testing

- Used https://pep8ci.herokuapp.com/ and put run.py file through it.
- Errors due to white space in ASCII art or due to the spacing left on the comments.

![image](https://github.com/user-attachments/assets/ea34f1d4-3885-4c2c-a5fc-c54942a5ae56)



## Bugs

- Main bug was due to the adding of colorama to the game board. This caused a spacing issue on the board due to the colour codes not being taken into account when calculating the column widths. The issue was in the def __str__(self). The solution ended up using strip_color to remove color codes and calculate the maximum width for each column based on the actual content.

   0  1  2  3  4  5  6  7  8  9
-------------------------------------------
 0|   |   |   |   |   |   |   |   |   |   |
 1|   |   |   |   |   |   |   |   |   |   |
 2|   |   |   |   |   |   |   |   |   |   |
 3|   |   |   |   |   |   |1|   |   |   |
 4|   |   |   |   |   |   |   |   |   |   |
 5|   |   |   |   |   |   |   |   |   |   |
 6|   |   |   |   |   |   |   |   |   |   |
 7|   |   |   |   |   |   |   |   |   |   |
 8|   |   |   |   |   |   |   |   |   |   |
 9|   |   |   |   |   |   |   |   |   |   |
-------------------------------------------

   0  1  2  3  4  5           6  7  8  9
-------------------------------------------
 0|  |  |  |  |  |           |  |  |  |  |
 1|  |  |  |  |  |           |  |  |  |  |
 2|  |  |  |  |  |           |  |  |  |  |
 3|  |  |  |  |  |F |  |  |  |  |
 4|  |  |  |  |  |           |  |  |  |  |
 5|  |  |  |  |  |           |  |  |  |  |
 6|  |  |  |  |  |           |  |  |  |  |
 7|  |  |  |  |  |           |  |  |  |  |
 8|  |  |  |  |  |           |  |  |  |  |
 9|  |  |  |  |  |           |  |  |  |  |
-------------------------------------------


### Unfixed bugs



## Deployment

### Version Control
 

### Page Deployment


### Cloning of the Repository Code locally



## Content

### Technologies Used

-   Programming language was Python.

-   I used the following Libraries:

-   Github was used to store the repository for submission.

-   Heroku was used to deploy the the live version of the terminal.

 

## Credits

