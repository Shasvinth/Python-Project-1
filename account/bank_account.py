from account.transaction import Transaction
from account.user import User
import time
from decimal import Decimal, ROUND_DOWN

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        # Validate initial balance
        if not isinstance(initial_balance, (int, float, Decimal)):
            raise ValueError("Invalid initial balance type! Must be a number.")
        initial_balance = Decimal(str(initial_balance)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative!")
            
        # Create user first to validate name and email
        self.user = User(name, email)
        self.balance = initial_balance
        self.transactions_history = []
        self.account_type = "Generic"

    def deposit(self, amount):
        try:
            amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive!")
                
            self.balance += amount
            self.transactions_history.append(Transaction(float(amount), "deposit"))
            print(f"Deposit successful! New balance: Rs. {self.balance:.2f}")
            time.sleep(1)  # Reduced delay for better UX
            return float(self.balance)
        except (ValueError, TypeError) as e:
            print(f"Error during deposit: {str(e)}")
            time.sleep(1)
            raise

    def withdraw(self, amount):
        try:
            amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive!")
            if self.balance < amount:
                raise ValueError(f"Insufficient Balance! Current balance: Rs. {self.balance:.2f}")
                
            self.balance -= amount
            self.transactions_history.append(Transaction(float(amount), "withdraw"))
            print(f"Withdrawal successful! New balance: Rs. {self.balance:.2f}")
            time.sleep(1)
            return float(self.balance)
        except (ValueError, TypeError) as e:
            print(f"Error during withdrawal: {str(e)}")
            time.sleep(1)
            raise

    def get_balance(self):
        return float(self.balance)

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self.account_type

    def get_user(self):
        return self.user


class SavingsAccount(BankAccount):
    MIN_BALANCE = Decimal('100.00')

    def withdraw(self, amount):
        try:
            amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
            if self.balance - amount < self.MIN_BALANCE:
                raise ValueError(f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Savings account!")
            return super().withdraw(float(amount))
        except (ValueError, TypeError) as e:
            print(f"Error during withdrawal: {str(e)}")
            time.sleep(1)
            raise

    def get_account_type(self):
        return "Savings account"


class CurrentAccount(BankAccount):
    MIN_BALANCE = Decimal('1000.00')

    def withdraw(self, amount):
        try:
            amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
            if self.balance - amount < self.MIN_BALANCE:
                raise ValueError(f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Current account!")
            return super().withdraw(float(amount))
        except (ValueError, TypeError) as e:
            print(f"Error during withdrawal: {str(e)}")
            time.sleep(1)
            raise

    def get_account_type(self):
        return "Current account"


class StudentAccount(BankAccount):
    MIN_BALANCE = Decimal('100.00')

    def withdraw(self, amount):
        try:
            amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
            if self.balance - amount < self.MIN_BALANCE:
                raise ValueError(f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Student account!")
            return super().withdraw(float(amount))
        except (ValueError, TypeError) as e:
            print(f"Error during withdrawal: {str(e)}")
            time.sleep(1)
            raise

    def get_account_type(self):
        return "Student account"

