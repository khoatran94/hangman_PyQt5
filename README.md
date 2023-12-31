# A normal Hangman game with GUI based on PyQt5
<p align="center">
  <img src="https://github.com/khoatran94/hangman_PyQt5/assets/39628780/54b5edb1-1a6c-4a48-a483-c5bdc17ef4e4" width="400">
</p>

<br/>
<br/>
<br/>

## Description
Hangman is a simple word puzzle game where you guess letters one at a time to find the target word.\
You have a maximum of 6 incorrect guesses (correct guess does not count towards "lives").

## Gameplay
A virtual keyboard is presented for you. Pressed letters will be automatically disabled, so you don't have to mind them for the rest of the game.\
Two additional buttons ***New game*** and ***Show Result*** are also available to start a new game or to show the target word, respectively.

## Files
* hangman_controller.py: the game is run within this file.
* hangman_gui.py: GUI of the game including the virtual keyboard.\
  This py file is generated by Qt Designer from the **hangman.ui** file. Feel free to generate a new one, but keep in mind once you do, any manually coded content will be erased.
* hangman_logic.py: word processing logic of the game.
  
## References:
 * The hangman pictures are taken from [en3rypt/HANGMAN-GAME](https://github.com/en3rypt/HANGMAN-GAME).
 * The English words are randomly generated from [dwyl/english-words](https://github.com/dwyl/english-words).





