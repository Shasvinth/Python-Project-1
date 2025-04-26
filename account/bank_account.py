from account.transaction import Transaction
from account.user import User
import time

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        if not isinstance(initial_balance, (int, float)):
            print("Invalid initial balance type! Must be a number.")
            time.sleep(2)
            raise ValueError("Invalid initial balance type!")
        if initial_balance < 0:
            print("Initial balance cannot be negative!")
            time.sleep(2)
            raise ValueError("Initial balance cannot be negative!")
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"
        self.user = User(name, email)

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Deposit amount must be a positive number!")
            time.sleep(2)
            raise ValueError("Deposit amount must be a positive number!")
        self.balance += amount
        self.transactions_history.append(Transaction(amount, "deposit"))
        print(f"Deposit successful! New balance: Rs. {self.balance}")
        time.sleep(2)
        return self.balance

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount must be a positive number!")
            time.sleep(2)
            raise ValueError("Withdrawal amount must be a positive number!")
        if self.balance < amount:
            print("Insufficient Balance!")
            time.sleep(2)
            raise ValueError("Insufficient Balance!")
        self.balance -= amount
        self.transactions_history.append(Transaction(amount, "withdraw"))
        print(f"Withdrawal successful! New balance: Rs. {self.balance}")
        time.sleep(2)
        return self.balance

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type

    def get_user(self):
        return self.user


class SavingsAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount must be a positive number!")
            time.sleep(2)
            raise ValueError("Withdrawal amount must be a positive number!")
        if self.balance - amount < self.MIN_BALANCE:
            error_msg = f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Savings account!"
            print(error_msg)
            time.sleep(2)
            raise ValueError(error_msg)
        return super().withdraw(amount)

    def get_account_type(self):
        return "Savings account"


class CurrentAccount(BankAccount):
    MIN_BALANCE = 1000  # Adding minimum balance requirement

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount must be a positive number!")
            time.sleep(2)
            raise ValueError("Withdrawal amount must be a positive number!")
        if self.balance - amount < self.MIN_BALANCE:
            error_msg = f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Current account!"
            print(error_msg)
            time.sleep(2)
            raise ValueError(error_msg)
        return super().withdraw(amount)

    def get_account_type(self):
        return "Current account"


class StudentAccount(BankAccount):
    MIN_BALANCE = 100

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Withdrawal amount must be a positive number!")
            time.sleep(2)
            raise ValueError("Withdrawal amount must be a positive number!")
        if self.balance - amount < self.MIN_BALANCE:
            error_msg = f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Students account!"
            print(error_msg)
            time.sleep(2)
            raise ValueError(error_msg)
        return super().withdraw(amount)

    def get_account_type(self):
        return "Students account"

