from account.transaction import Transaction
from account.user import User
import time
from decimal import Decimal, ROUND_HALF_EVEN, InvalidOperation, ROUND_HALF_UP

class BankAccount:
    def __init__(self, name="John", email="john@gmail.com", initial_balance=0):
        self.user = User(name, email)
        
        try:
            self.balance = Decimal(str(initial_balance)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            if self.balance < 0:
                raise ValueError("Initial balance cannot be negative!")
        except (InvalidOperation, TypeError):
            raise ValueError("Invalid initial balance! Must be a valid number.")
            
        self.transactions_history = []
        self._account_type = "Generic Account"

    def deposit(self, amount):
        try:
            if isinstance(amount, str):
                amount = amount.strip()
            # Round up for deposits (0.125 becomes 0.13)
            amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            if amount <= 0:
                raise ValueError("Deposit amount must be positive!")
                
            transaction = Transaction(str(amount), "deposit")  # Pass as string to ensure consistent rounding
            self.balance = (self.balance + transaction.amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            self.transactions_history.append(transaction)
            print(f"Deposit successful! New balance: Rs. {self.balance:.2f}")
            time.sleep(1)
            return float(self.balance)
        except (ValueError, InvalidOperation) as e:
            print(f"Error during deposit: {str(e)}")
            time.sleep(1)
            raise

    def withdraw(self, amount):
        try:
            if isinstance(amount, str):
                amount = amount.strip()
            # Round up for withdrawals (0.125 becomes 0.13)
            amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive!")
            if self.balance < amount:
                raise ValueError(f"Insufficient Balance! Current balance: Rs. {self.balance:.2f}")
            
            # Calculate new balance
            new_balance = (self.balance - amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            
            # Check minimum balance before proceeding with transaction
            self._check_minimum_balance(new_balance)
            
            # Only create transaction and update balance if minimum balance check passes
            transaction = Transaction(str(amount), "withdraw")
            self.balance = new_balance
            self.transactions_history.append(transaction)
            
            print(f"Withdrawal successful! New balance: Rs. {self.balance:.2f}")
            time.sleep(1)
            return float(self.balance)
        except (ValueError, InvalidOperation) as e:
            print(f"Error during withdrawal: {str(e)}")
            time.sleep(1)
            raise

    def _check_minimum_balance(self, new_balance):
        """Check if new balance would be valid. Override in derived classes."""
        pass

    def get_balance(self):
        return float(self.balance)

    def get_transaction_history(self):
        return self.transactions_history

    def get_account_type(self):
        return self._account_type

    def get_user(self):
        return self.user


class SavingsAccount(BankAccount):
    MIN_BALANCE = Decimal('100.00')

    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self._account_type = "Savings Account"
        if self.balance < self.MIN_BALANCE:
            raise ValueError(f"Initial balance must be at least Rs. {self.MIN_BALANCE} for Savings Account")

    def _check_minimum_balance(self, new_balance):
        if new_balance <= self.MIN_BALANCE:
            raise ValueError(f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Savings account!")


class CurrentAccount(BankAccount):
    MIN_BALANCE = Decimal('1000.00')

    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self._account_type = "Current Account"
        if self.balance < self.MIN_BALANCE:
            raise ValueError(f"Initial balance must be at least Rs. {self.MIN_BALANCE} for Current Account")

    def _check_minimum_balance(self, new_balance):
        if new_balance <= self.MIN_BALANCE:
            raise ValueError(f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Current account!")


class StudentAccount(BankAccount):
    MIN_BALANCE = Decimal('100.00')

    def __init__(self, name, email, initial_balance=0):
        super().__init__(name, email, initial_balance)
        self._account_type = "Student Account"
        if self.balance < self.MIN_BALANCE:
            raise ValueError(f"Initial balance must be at least Rs. {self.MIN_BALANCE} for Student Account")

    def _check_minimum_balance(self, new_balance):
        if new_balance <= self.MIN_BALANCE:
            raise ValueError(f"Must maintain minimum balance of Rs. {self.MIN_BALANCE} in Student account!")

