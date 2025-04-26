import time
import re

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account added successfully for user {self.name}")
        time.sleep(2)

    def get_total_balance(self): 
        return sum(account.get_balance() for account in self.accounts)

    def get_account_count(self):
        return len(self.accounts)

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            print("Account removed successfully.")
            time.sleep(2)
            return True
        print("Account not found.")
        time.sleep(2)
        return False

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            print("Invalid email format!")
            time.sleep(2)
            return False
        return True

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Number of accounts: {len(self.accounts)}"
