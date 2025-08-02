# 🎮 Word Guessing Game (Hangman Style)

This is a **Hangman-style word guessing game** built in Python. Players must guess a hidden word from a chosen category by entering one letter at a time. The game includes difficulty levels and multiple categories for increased fun and challenge.

---

## 📋 Features

- 🧠 **Three Difficulty Levels**:
  - **Easy**: 15 attempts
  - **Medium**: 10 attempts
  - **Hard**: 6 attempts
- 🗂️ **Five Categories**:
  - Animal
  - City
  - Food
  - Job
  - Nation
- ✅ Input validation and prevents repeated guesses.
- 📢 Real-time feedback after each guess.
- 🎯 Victory when the word is fully guessed.
- ❌ Game over after running out of attempts.

---

## 🚀 How to Play

1. Run the script:
   python your_script_name.py

2. Follow the prompts:

   * Choose a **difficulty level**.
   * Choose a **category**.
   * Start guessing one letter at a time.

3. You win if you guess all letters before running out of attempts.

---

## 📌 Example Gameplay

```text
Welcome in Guess Word  
PLease enter Level  
 - Easy  
 - Meduim  
 - Hard  
Level : medium  
Choose a category:  
 - Animal  
 - City  
 - Food  
 - Job  
 - Nation  
Your Choice : city  
Word Selected  
Word: -----  
Attempts left: 10  
Letter : o  
Correct guess  
Attempts left: 10  
...  
You won! The word was: Tokyo
---
```
## 🧠 Code Structure

| Function         | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `Message()`      | Prints welcome message.                                       |
| `Choice_Level()` | Lets user select a difficulty level.                          |
| `Choice_word()`  | Lets user select a word category and randomly selects a word. |
| `Show_Word()`    | Displays guessed letters and hidden letters as dashes.        |
| `take_input()`   | Handles user letter input and checks validity.                |
| `play()`         | Main function that runs the game logic.                       |

---

## 📂 Word Categories

### 🐾 Animal

Cat, Dog, Lion, Elephant, Zebra, Monkey, Dolphin, Tiger, Giraffe, Bear, Kangaroo, Crocodile, Horse, Panda, Wolf, Fox, Deer, Rabbit, Owl, Camel, Shark, Penguin

### 🌆 City

Cairo, Paris, Tokyo, New York, Sydney, London, Dubai, Rome, Berlin, Toronto, Istanbul, Beijing, Madrid, Buenos Aires, Moscow, Athens, Los Angeles, Chicago, Seoul, Bangkok

### 🍔 Food

Pizza, Rice, Chicken, Burger, Pasta, Sushi, Salad, Sandwich, Steak, Ice cream, Tacos, Fruits, Soup, Noodles, Cake, Curry, Bread, Chocolate, Fries, Dumplings

### 👷 Job

Engineer, Doctor, Teacher, Chef, Pilot, Artist, Accountant, Lawyer, Nurse, Mechanic, Scientist, Dentist, Firefighter, Pharmacist, Driver, Plumber, Electrician, Photographer, Architect

### 🌍 Nation

Egypt, France, Japan, Brazil, Canada, India, China, Germany, Mexico, South Africa, Russia, Spain, Italy, Argentina, Nigeria, Thailand, Turkey, Sweden, Norway, Pakistan

---

## ✅ Requirements

* Python 3.x
* No external libraries required

---

## ✨ Future Enhancements (Optional Ideas)

* Add option to guess the full word.
* Track score over multiple rounds.
* Add ASCII art or animations.
* Add sound (for GUI versions).
* Use a GUI library like Tkinter or PyGame.

---

Enjoy the game and have fun guessing! 🧩
