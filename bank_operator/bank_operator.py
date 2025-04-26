from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount
import time
from decimal import Decimal, InvalidOperation

users = []  # Global list to store users

def create_user():
    try:
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        
        # Create user object which will validate inputs
        user = User(name, email)
        users.append(user)
        print(f"User {name} created successfully.\n")
        time.sleep(1)
        return user
    except ValueError as e:
        print(f"Error creating user: {str(e)}")
        time.sleep(1)
        return None

def list_users():
    if not users:
        print("No users found! Please create a user first.\n")
        time.sleep(1)
        return False
    print("\nList of Users:")
    print("-" * 70)  # Increased width for better formatting
    for i, user in enumerate(users, 1):
        print(f"{i}. {user}")
    print("-" * 70 + "\n")
    time.sleep(1)
    return True

def create_account():
    if not list_users():
        return

    try:
        # User selection
        user_input = input("Select user number (or 'q' to quit): ").strip().lower()
        if user_input == 'q':
            print("Account creation cancelled.")
            time.sleep(1)
            return
            
        idx = int(user_input) - 1
        if idx < 0 or idx >= len(users):
            raise ValueError("Invalid user selection")
        
        selected_user = users[idx]

        # Account type selection
        print("\nAccount Type:")
        print("1. Savings Account (Min. Balance: Rs. 100)")
        print("2. Student Account (Min. Balance: Rs. 100)")
        print("3. Current Account (Min. Balance: Rs. 1000)")
        
        account_choice = int(input("\nEnter your choice (1-3): "))
        if account_choice not in [1, 2, 3]:
            raise ValueError("Invalid account type")

        # Initial deposit
        amount = Decimal(input("Enter initial deposit amount: Rs. ").strip())
        if amount < 0:
            raise ValueError("Initial deposit cannot be negative")

        # Create appropriate account type
        if account_choice == 1:
            if amount < SavingsAccount.MIN_BALANCE:
                raise ValueError(f"Initial deposit must be at least Rs. {SavingsAccount.MIN_BALANCE} for Savings Account")
            account = SavingsAccount(selected_user.name, selected_user.email, float(amount))
        elif account_choice == 2:
            if amount < StudentAccount.MIN_BALANCE:
                raise ValueError(f"Initial deposit must be at least Rs. {StudentAccount.MIN_BALANCE} for Student Account")
            account = StudentAccount(selected_user.name, selected_user.email, float(amount))
        else:
            if amount < CurrentAccount.MIN_BALANCE:
                raise ValueError(f"Initial deposit must be at least Rs. {CurrentAccount.MIN_BALANCE} for Current Account")
            account = CurrentAccount(selected_user.name, selected_user.email, float(amount))

        selected_user.add_account(account)
        print(f"\n✓ {account.get_account_type()} created successfully!")
        print(f"Initial balance: Rs. {account.get_balance():.2f}\n")
        time.sleep(1)

    except (ValueError, InvalidOperation) as e:
        print(f"\nError creating account: {str(e)}")
        time.sleep(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        time.sleep(1)

def deposit_money():
    if not users:
        print("No users available. Please create a user first.\n")
        time.sleep(1)
        return

    try:
        list_users()
        user_input = input("Select user number (or 'q' to quit): ").strip().lower()
        if user_input == 'q':
            print("Transaction cancelled.")
            time.sleep(1)
            return
            
        idx = int(user_input) - 1
        if idx < 0 or idx >= len(users):
            raise ValueError("Invalid user selection")

        user = users[idx]
        if not user.accounts:
            raise ValueError("No accounts found for this user")

        print("\nAvailable accounts:")
        for i, acc in enumerate(user.accounts, 1):
            print(f"{i}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance():.2f}")
        
        acc_idx = int(input("\nSelect account number: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            raise ValueError("Invalid account selection")

        amount = Decimal(input("Enter amount to deposit: Rs. ").strip())
        if amount <= 0:
            raise ValueError("Amount must be positive")

        user.accounts[acc_idx].deposit(float(amount))

    except (ValueError, InvalidOperation) as e:
        print(f"\nError during deposit: {str(e)}")
        time.sleep(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        time.sleep(1)

def withdraw_money():
    if not users:
        print("No users available. Please create a user first.\n")
        time.sleep(1)
        return

    try:
        list_users()
        user_input = input("Select user number (or 'q' to quit): ").strip().lower()
        if user_input == 'q':
            print("Transaction cancelled.")
            time.sleep(1)
            return
            
        idx = int(user_input) - 1
        if idx < 0 or idx >= len(users):
            raise ValueError("Invalid user selection")

        user = users[idx]
        if not user.accounts:
            raise ValueError("No accounts found for this user")

        print("\nAvailable accounts:")
        for i, acc in enumerate(user.accounts, 1):
            print(f"{i}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance():.2f}")
        
        acc_idx = int(input("\nSelect account number: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            raise ValueError("Invalid account selection")

        amount = Decimal(input("Enter amount to withdraw: Rs. ").strip())
        if amount <= 0:
            raise ValueError("Amount must be positive")

        user.accounts[acc_idx].withdraw(float(amount))

    except (ValueError, InvalidOperation) as e:
        print(f"\nError during withdrawal: {str(e)}")
        time.sleep(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        time.sleep(1)

def view_transactions():
    if not list_users():
        return

    try:
        user_input = input("Select user number (or 'q' to quit): ").strip().lower()
        if user_input == 'q':
            print("Operation cancelled.")
            time.sleep(1)
            return
            
        idx = int(user_input) - 1
        if idx < 0 or idx >= len(users):
            raise ValueError("Invalid user selection")

        user = users[idx]
        if not user.accounts:
            raise ValueError("No accounts found for this user")

        print(f"\nAccounts and Transactions for {user.name}:")
        print("=" * 70)
        
        for i, acc in enumerate(user.accounts, 1):
            print(f"\n{acc.get_account_type()} (Account #{i})")
            print(f"Current Balance: Rs. {acc.get_balance():.2f}")
            print("-" * 60)
            
            transactions = acc.get_transaction_history()
            if not transactions:
                print("No transactions found.")
            else:
                print("Transaction History:")
                for tx in transactions:
                    print(f"  {tx}")
            print("-" * 60)
        print("\n")
        time.sleep(1)

    except ValueError as e:
        print(f"\nError: {str(e)}")
        time.sleep(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        time.sleep(1)

