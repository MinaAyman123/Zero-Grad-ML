# 🎯 Guess the Number Game (Python CLI)

A simple Python command-line game where the player guesses a randomly generated number within a certain range and limited number of attempts based on the selected difficulty level.

## 🕹️ How to Play

1. Choose a difficulty level:

   * **Easy**: Range 1–10, 3 attempts
   * **Medium**: Range 1–100, 7 attempts
   * **Hard**: Range 1–1000, 15 attempts

2. Try to guess the secret number within the allowed attempts.

3. After each guess, the game will give you a hint:

   * `Increase` if your guess is too low
   * `Decrease` if your guess is too high

4. Win the game by guessing correctly, or lose if attempts run out.

---

## ▶️ Run the Game

### 1. Clone the repo or download the script

```bash
git clone https://github.com/your-username/guess-the-number.git
cd guess-the-number
```

### 2. Run the script

```bash
python guess_game.py
```

---

## 📄 Code Overview

* `show_levels()`
  Prints level options to the player.

* `game_level_choice()`
  Handles user input and validates the chosen level.

* `set_game_settings(level)`
  Sets number range and attempts according to difficulty.

* `start_play(limits, n_trials)`
  Main game logic — player guesses the number.

* `play()`
  Orchestrates the full game flow.

---

## 💡 Example

```bash
Plase enter level( Easy , Meduim , hard )
Level : easy
Welcomme Guess game please enter number between 1 and 10
NUmber : 5
Increase
NUmber : 7
Decrease
NUmber : 6
Congratulations
```

---

## 🛠 Requirements

* Python 3.x
  (No external libraries required — built entirely with standard Python)

