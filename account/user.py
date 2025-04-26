import time
import re

class User:
    def __init__(self, name, email):
        self.validate_name(name)
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        self.name = name.strip()
        self.email = email.lower().strip()
        self.accounts = []

    @staticmethod
    def validate_name(name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not re.match(r'^[A-Za-z\s]{2,50}$', name.strip()):
            raise ValueError("Name must be 2-50 characters long and contain only letters and spaces")
        return True

    def add_account(self, account):
        # Validate account type
        if not hasattr(account, 'get_account_type'):
            raise ValueError("Invalid account object")
        self.accounts.append(account)
        print(f"Account added successfully for user {self.name}")
        time.sleep(2)

    def get_total_balance(self): 
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if not hasattr(account, 'get_account_type'):
            raise ValueError("Invalid account object")
        if account in self.accounts:
            self.accounts.remove(account)
            print("Account removed successfully.")
            time.sleep(2)
            return True
        print("Account not found.")
        time.sleep(2)
        return False

    def is_valid_email(self, email):
        if not email or not isinstance(email, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email.strip()))

    def __str__(self):
        total_balance = self.get_total_balance()
        return f"Name: {self.name}, Email: {self.email}, Number of accounts: {len(self.accounts)}, Total Balance: Rs. {total_balance:.2f}"
