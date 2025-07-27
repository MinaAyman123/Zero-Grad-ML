# 🏧 ATM Simulator (Python CLI)

A simple command-line ATM simulation program written in Python. This application supports user authentication via PIN and allows basic banking operations like checking balance, depositing, withdrawing, and viewing a mini statement.

---

## 💡 Features

* 🔒 **PIN authentication** (3 attempts max)
* 💰 **Balance Inquiry**
* ➕ **Deposit Money**
* ➖ **Withdraw Money**
* 🧾 **Mini Statement** (shows last 5 transactions)
* 🚪 **Exit**

---

## 🧪 How to Run

### 1. Clone or download the script

```bash
git clone https://github.com/your-username/atm-simulator.git
cd atm-simulator
```

### 2. Run the script

```bash
python atm.py
```

---

## 🔐 Default Settings

* **PIN**: `1234`
* **Initial Balance**: `$1000.00`

---

## 🖥️ Example Run

```
PIN : 1234

Available Transactions :
 - Balance inquiry
 - Deposit
 - Withdraw
 - Mini statement
 - Exit

Enter transectoin : deposit
Number of Deposit : 500
Vallied Transection
--------------------------------------------------

Enter transectoin : balance inquiry
Current Account Balance : 1500.0
--------------------------------------------------
```

---

## 🧠 Code Overview

* `authenticate()` → Verifies the PIN (up to 3 tries)
* `show_menu()` → Displays transaction options
* `balance_inquiry()` → Shows current balance
* `deposit()` → Adds money to the account
* `withdraw()` → Deducts money if sufficient balance
* `mini_statement()` → Shows last 5 transactions
* `main()` → Main loop of the program

---

## 📦 Requirements

* Python 3.x
  (No third-party packages needed)

