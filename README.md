# **Snake Game**
This program displays the game Snake exactly as it was in cube form on the beautiful old Nokia 
and not as smoothly as in the new versions, but with a bit more color.

 __How to play the game__: 

Start the game by pressing one of the four arrow keys. Your task in the game is to guide the snake and feed it with the red food block. 
If the snake eats the food, it grows by one block unit and a new food must be eaten. In the end, you should beat the high score.

But be careful! You are not allowed to run out of the playing field or steer into your snake (if the snake is too long or 
directly makes a 180-degree turn, of course twice 90 degrees, 
is allowed as long as the snake has run at least one length unit further). Then the game is over.
When the game is over, you can see your score and the high score you should have cracked. You will also be prompted to press the space bar to restart the game
or press x or esc to end the game.

Pressing the space bar will take you back to the home screen. Pressing any arrow key will restart the game. If you press the space bar during the game 
, you can interrupt the game. You will then be prompted to press the space bar again to continue the game or press x or esc to end the game.


# Feedback
This looks already quite nice. After installing the missing requirements it was really fun!

Here are some remarks, next to the comments I gave in code:
- README.md is already informative, but please also add an installation and execution guide (check our repositories for this) 
- the package folder "Snake_game" (which contains the modules) should follow the naming convention for variables -> "snake_game"
- please have a look at our suggested project structure, tests should be seperated from you "runnable" code
- You are missing a `requirements.txt`, as it is I wouldn't be able to run it as `pygame` is missing
- You have proper commit messages, but didn't use feature branches, please use some, as you implement my remarks
- Docstrings are pretty nice
- You have no typing yet, mypy might rage
- please run ruff and mypy on your code

 