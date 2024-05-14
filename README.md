[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/i3cjXgnP)
# othello-python
Starter Code for Othello AI Agent Programming Assignment

Originally created by Erich Kramer at OSU for Professor Rebecca Hutchinson.
Cleaned up by Rob Churchill.

How to play a game:

1. Run `python3 game_driver.py [player_type] [player_type]`.
2. Choose `human`, or `minimax` as the player types.
3. Follow the prompts to choose where to place stones.

Analysis
1.
    a. 1st and 2nd game, ai won, 3rd and 4th game, I won
    b. yes
    c. miliseconds: 3.1, 1.3, 0.33, 0.60
       Overall trend is that the shallower the depth, the less time it takes which makes sense because a shallower depth means much less lines of code to run
2.
    a. 1st game, tie game, 2md game, I won
    b. yes
    c. seconds: 2.18, 0.0054
       once again, a shallower depth means less lines of code to run but as this is a bigger board and there are usually more legal plays available per turn, a depth of 5 compared to a depth of 2 is a much bigger difference that the same on a 4x4 board.