"""
Simplified Banking Application
Demonstrates: class, objects, __init__, instance methods,
class variables, class methods, and input validation.
"""


class BankAccount:
    # Class variables: shared by every BankAccount object
    bank_name = "Python National Bank"
    total_accounts = 0

    def __init__(self, holder_name, account_number, balance=0.0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        # Instance variables: unique to each account
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

        # Bonus: track total accounts created
        BankAccount.total_accounts += 1

    # ---------- Instance methods ----------
    def deposit(self, amount):
        """Add money to the account. Amount must be positive."""
        if amount <= 0:
            print(f"Deposit failed: amount must be greater than 0 (got {amount}).")
            return False
        self.balance += amount
        print(f"Deposited ${amount:,.2f} into {self.account_number}. "
              f"New balance: ${self.balance:,.2f}")
        return True

    def withdraw(self, amount):
        """Withdraw money. Blocks invalid amounts and overdrafts."""
        if amount <= 0:
            print(f"Withdrawal failed: amount must be greater than 0 (got {amount}).")
            return False
        if amount > self.balance:
            print(f"Withdrawal failed: insufficient funds. "
                  f"Requested ${amount:,.2f}, available ${self.balance:,.2f}.")
            return False
        self.balance -= amount
        print(f"Withdrew ${amount:,.2f} from {self.account_number}. "
              f"New balance: ${self.balance:,.2f}")
        return True

    def check_balance(self):
        """Return the current balance."""
        return self.balance

    def display_account_details(self):
        """Print all account details."""
        print("-" * 42)
        print(f"Bank           : {BankAccount.bank_name}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ${self.balance:,.2f}")
        print("-" * 42)

    # ---------- Class methods ----------
    @classmethod
    def change_bank_name(cls, new_name):
        """Change the bank name for every account."""
        old_name = cls.bank_name
        cls.bank_name = new_name
        print(f"Bank name changed: '{old_name}' -> '{new_name}'")

    @classmethod
    def get_total_accounts(cls):
        """Return the total number of accounts created."""
        return cls.total_accounts

    def __str__(self):
        return f"{self.account_number} | {self.holder_name} | ${self.balance:,.2f}"


# ---------------- Demo ----------------
if __name__ == "__main__":
    # Create multiple accounts
    acc1 = BankAccount("Aarav Sharma", "ACC1001", 5000)
    acc2 = BankAccount("Priya Verma", "ACC1002", 1200)
    acc3 = BankAccount("Rohan Mehta", "ACC1003")  # starts at $0

    print("\n=== Account Details ===")
    for acc in (acc1, acc2, acc3):
        acc.display_account_details()

    print("\n=== Transactions ===")
    acc1.deposit(1500)
    acc1.withdraw(2000)
    acc2.withdraw(5000)     # more than available -> blocked
    acc3.deposit(-100)      # invalid amount -> blocked
    acc3.deposit(750)
    acc3.withdraw(0)        # invalid amount -> blocked

    print("\n=== Check Balances ===")
    for acc in (acc1, acc2, acc3):
        print(f"{acc.holder_name:<14}: ${acc.check_balance():,.2f}")

    print("\n=== Change Bank Name (class method) ===")
    BankAccount.change_bank_name("Global Trust Bank")
    acc1.display_account_details()
    acc2.display_account_details()   # same new name for every account

    print("\n=== Bonus: Total Accounts ===")
    print(f"Total accounts created: {BankAccount.get_total_accounts()}")