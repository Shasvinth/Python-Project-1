import time
import re

class User:
    def __init__(self, name, email):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        if not email or not isinstance(email, str):
            raise ValueError("Email must be a non-empty string")
            
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
        name = name.strip()
        if len(name) < 2 or len(name) > 50:
            raise ValueError("Name must be between 2 and 50 characters")
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValueError("Name must contain only letters and spaces")
        return True

    def add_account(self, account):
        if account is None:
            raise ValueError("Account cannot be None")
        if not hasattr(account, 'get_account_type'):
            raise ValueError("Invalid account object")
        if not hasattr(account, 'get_user') or account.get_user() != self:
            raise ValueError("Account must belong to this user")
            
        self.accounts.append(account)
        print(f"Account added successfully for user {self.name}")
        time.sleep(1)

    def get_total_balance(self): 
        if not self.accounts:
            return 0.0
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if account is None:
            raise ValueError("Account cannot be None")
        if not hasattr(account, 'get_account_type'):
            raise ValueError("Invalid account object")
            
        if account in self.accounts:
            self.accounts.remove(account)
            print("Account removed successfully.")
            time.sleep(1)
            return True
            
        print("Account not found.")
        time.sleep(1)
        return False

    @staticmethod
    def is_valid_email(email):
        if not email or not isinstance(email, str):
            return False
        email = email.strip()
        if len(email) > 254:  # RFC 5321
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def __str__(self):
        total_balance = self.get_total_balance()
        return f"Name: {self.name}, Email: {self.email}, Number of accounts: {len(self.accounts)}, Total Balance: Rs. {total_balance:.2f}"
