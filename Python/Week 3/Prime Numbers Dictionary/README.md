# 🔢 Prime Numbers Dictionary

This is a **Prime Numbers Dictionary** program built in Python.  
It generates a dictionary of prime numbers up to a user-specified limit,  
displays all primes, and allows the user to retrieve a prime number by its position.

---

## 📋 Features

- 📈 **Generate Prime Numbers** up to a limit chosen by the user.
- 📂 Store primes in a dictionary with their position as the key.
- 🔍 **View Options**:
  - View all generated prime numbers.
  - Get a prime number by its position.
- ✅ Input validation for menu choices and positions.

---

## 🚀 How to Use

1. Run the script:
   ```bash
   python your_script_name.py
````

2. Follow the prompts:

   * Enter a number to set the range for generating primes.
   * Choose from the menu:

     * **1** → View all primes.
     * **2** → Get a prime by its position.
     * **3** → Exit the program.

---

## 📌 Example Usage

```text
Welcomme in Prime Numbers Dictionary
Number : 20
Menu:
Enter 1 to View all primes
enter 2 to  Get prime by position
enter 3 to Exit

Choose: 1
1 -> 2
2 -> 3
3 -> 5
4 -> 7
5 -> 11
6 -> 13
7 -> 17
8 -> 19
----------------------------------------------------------------------------------------------------
Menu:
Enter 1 to View all primes
enter 2 to  Get prime by position
enter 3 to Exit

Choose: 2
Postion : 5
11
----------------------------------------------------------------------------------------------------
```

---

## 🧠 Code Structure

| Function               | Description                                   |
| ---------------------- | --------------------------------------------- |
| `Welcomme_Message()`   | Prints a welcome message at program start.    |
| `isPrime(num)`         | Checks if a number is prime.                  |
| `Generate_dictonary()` | Generates the prime number dictionary.        |
| `display_prime()`      | Displays all primes with their positions.     |
| `display_number()`     | Displays a prime at a given position.         |
| `display_Menu()`       | Shows menu options to the user.               |
| `take_input()`         | Validates and returns the user's menu choice. |
| `play()`               | Main function that runs the program loop.     |

---

## ✅ Requirements

* Python 3.x
* No external libraries required

---

## ✨ Future Enhancements (Optional Ideas)

* Add the ability to save the primes to a `.txt` or `.csv` file.
* Allow generating primes within a specific range instead of from 1 to N.
* Add error handling for non-integer inputs.
* Create a GUI version for better interactivity.

---

Enjoy exploring prime numbers! 🔢

