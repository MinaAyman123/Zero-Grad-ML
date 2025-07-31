# Hangman Word Guessing Game 🎮

This is a simple command-line Hangman-style game built in Python. The player must guess a hidden word by entering one letter at a time. The game ends if the player successfully guesses the entire word or exceeds the allowed number of incorrect guesses.

## 🔧 Features

* Randomly selects a word from a predefined list.
* Allows the player to guess one letter at a time.
* Tracks correct and incorrect guesses.
* Ends the game after 10 incorrect attempts.
* Displays partially guessed word after each round.

## 📜 How It Works

* A word is randomly chosen from a list (`['Mina', 'Bab', 'Gdo']`).
* The user is prompted to guess one letter at a time.
* If the guessed letter is in the word and hasn't been guessed before, it's revealed in its correct position(s).
* If the guessed letter is incorrect or repeated, it counts as a failed trial.
* The player has a maximum of 10 incorrect guesses.
* The game ends in either a **win** (if all letters are guessed) or a **loss** (if 10 incorrect trials are reached).

## ▶️ How to Play

1. Run the script:

   ```bash
   python your_script_name.py
   ```
2. Input single letters when prompted.
3. Try to guess all the letters in the word before reaching 10 wrong attempts.

## 📝 Code Structure

* `Choice_Word()`: Chooses a random word.
* `display_Word(word, letter_list)`: Displays the word with guessed letters revealed.
* `guess_validation(letter_list, trial, word)`: Validates player input and counts wrong attempts.
* `play()`: Main game loop.

## ✅ Example

```
Please enter Single Letter : a
-a-
Please enter Single Letter : b
Please enter one letter
Please enter Single Letter : b
-ab
...
Lost the Game the Word was: Mina
```

## 📌 Requirements

* Python 3.x
* No external libraries needed
