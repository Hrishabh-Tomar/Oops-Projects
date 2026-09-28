# Task 2: Simplified Banking Application (Python OOP)

A small command-line banking application. Each account can take deposits and withdrawals, show its balance, and print its details. All accounts share one bank name, and the program counts how many accounts have been opened.

## Features

- Open accounts with a holder name, account number and opening balance
- Deposit money, refusing amounts of zero or less
- Withdraw money, refusing amounts of zero or less and any withdrawal larger than the balance
- Check the balance and display account details
- Change the bank name for every account with one class method call
- **Bonus:** count the total number of accounts created

## OOP Concepts Covered

| Concept | Implementation |
|---|---|
| **Class** | `BankAccount` |
| **Objects** | `acc1`, `acc2`, `acc3` |
| **Constructor (`__init__`)** | Sets `holder_name`, `account_number`, `balance`, refuses a negative opening balance and adds 1 to the account count |
| **Instance methods** | `deposit()`, `withdraw()`, `check_balance()`, `display_account_details()` |
| **Class variables** | `bank_name`, `total_accounts` |
| **Class methods** | `change_bank_name()`, `get_total_accounts()` |

## Project Structure

```
.
├── bank_account.py   # BankAccount class + demo
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

```bash
# Mac / Linux
python3 bank_account.py

# Windows
python bank_account.py
```

## Usage Example

```python
from bank_account import BankAccount

acc = BankAccount("Aarav Sharma", "ACC1001", 5000)
acc.deposit(1500)                      # balance: 6500
acc.withdraw(2000)                     # balance: 4500
acc.withdraw(10000)                    # refused: insufficient funds
print(acc.check_balance())             # 4500

BankAccount.change_bank_name("Global Trust Bank")   # applies to all accounts
print(BankAccount.get_total_accounts())
```

## Sample Output

```
=== Transactions ===
Deposited $1,500.00 into ACC1001. New balance: $6,500.00
Withdrew $2,000.00 from ACC1001. New balance: $4,500.00
Withdrawal failed: insufficient funds. Requested $5,000.00, available $1,200.00.
Deposit failed: amount must be greater than 0 (got -100).

=== Change Bank Name (class method) ===
Bank name changed: 'Python National Bank' -> 'Global Trust Bank'

=== Bonus: Total Accounts ===
Total accounts created: 3
```

## Method Reference

| Method | Type | Description |
|---|---|---|
| `__init__(holder_name, account_number, balance=0.0)` | Constructor | Creates an account and adds 1 to `total_accounts` |
| `deposit(amount)` | Instance | Adds a positive amount to the balance |
| `withdraw(amount)` | Instance | Takes money out only if the amount is positive and no more than the balance |
| `check_balance()` | Instance | Returns the current balance |
| `display_account_details()` | Instance | Prints the bank name, account holder, account number and balance |
| `change_bank_name(new_name)` | Class | Changes the bank name for every account |
| `get_total_accounts()` | Class | Returns the number of accounts created |

## Possible Enhancements

- Keep a transaction history for each account
- Transfer money between accounts
- Add savings accounts that earn interest, as a child class
