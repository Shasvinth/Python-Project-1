from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount
import time  # Add time module import

users = []  # Global list to store users

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Invalid email format! Please enter a valid email address.")
        return None
    users.append(user)
    print(f"User {name} created successfully.\n")
    time.sleep(2)  # Add 2 second delay
    return user

def list_users():
    if not users:
        print("No users found! Please create a user first.\n")
        time.sleep(2)  # Add delay for empty users message
        return False
    print("\nList of Users:")
    print("-" * 50)
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")
    print("-" * 50 + "\n")
    time.sleep(2)  # Add delay after showing user list
    return True

def create_account():
    if not list_users():  # This will show users if they exist
        return

    while True:
        try:
            user_input = input("Select user number: ").strip()
            if not user_input:
                print("Please enter a number.")
                time.sleep(2)  # Add delay for error message
                continue

            idx = int(user_input) - 1
            if idx < 0 or idx >= len(users):
                print("Invalid user selection.\n")
                time.sleep(2)  # Add delay for error message
                continue
            
            selected_user = users[idx]
            break
        except ValueError:
            print("Invalid user selection.\n")
            time.sleep(2)  # Add delay for error message
            continue

    print("Account Type:")
    print("1. Savings Account")
    print("2. Students Account")
    print("3. Current Account")
    
    while True:
        try:
            account_choice = int(input("Enter your choice (1, 2, 3): "))
            if account_choice not in [1, 2, 3]:
                print("Invalid account type!")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Invalid account type!")
            time.sleep(2)  # Add delay for error message
            continue

    while True:
        try:
            amount = float(input("Enter initial deposit: "))
            if amount < 0:
                print("Amount cannot be negative.")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
            time.sleep(2)  # Add delay for error message
            continue

    if account_choice == 1:
        account = SavingsAccount(selected_user.name, selected_user.email, amount)
    elif account_choice == 2:
        account = StudentAccount(selected_user.name, selected_user.email, amount)
    else:
        account = CurrentAccount(selected_user.name, selected_user.email, amount)

    selected_user.add_account(account)
    print(f"{account.get_account_type()} added successfully!\n")
    time.sleep(2)  # Add 2 second delay

def deposit_money():
    if not users:
        print("No users available. Please create a user first.\n")
        time.sleep(2)  # Add delay for error message
        return

    list_users()
    while True:
        try:
            idx = int(input("Select user: ")) - 1
            if idx < 0 or idx >= len(users):
                print("Invalid user selection.\n")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Invalid user selection.\n")
            time.sleep(2)  # Add delay for error message
            continue

    user = users[idx]
    if not user.accounts:
        print("No accounts found for this user.\n")
        time.sleep(2)  # Add delay for error message
        return

    print("\nAvailable accounts:")
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    
    while True:
        try:
            acc_input = input("Select account (or 'q' to quit): ").strip().lower()
            if acc_input == 'q':
                print("Transaction cancelled.\n")
                time.sleep(2)  # Add 2 second delay
                return
                
            acc_idx = int(acc_input) - 1
            if acc_idx < 0 or acc_idx >= len(user.accounts):
                print(f"Please enter a number between 1 and {len(user.accounts)}.\n")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Please enter a valid account number.\n")
            time.sleep(2)  # Add delay for error message
            continue

    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be positive.")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
            time.sleep(2)  # Add delay for error message
            continue

    user.accounts[acc_idx].deposit(amount)
    print(f"Successfully deposited Rs. {amount}. New balance: Rs. {user.accounts[acc_idx].get_balance()}\n")
    time.sleep(2)  # Add 2 second delay

def withdraw_money():
    if not users:
        print("No users available. Please create a user first.\n")
        time.sleep(2)  # Add delay for error message
        return

    list_users()
    while True:
        try:
            idx = int(input("Select user: ")) - 1
            if idx < 0 or idx >= len(users):
                print("Invalid user selection.\n")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Invalid user selection.\n")
            time.sleep(2)  # Add delay for error message
            continue

    user = users[idx]
    if not user.accounts:
        print("No accounts found for this user.\n")
        time.sleep(2)  # Add delay for error message
        return

    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. {acc.get_account_type()} - Balance: Rs. {acc.get_balance()}")
    
    while True:
        try:
            acc_idx = int(input("Select account: ")) - 1
            if acc_idx < 0 or acc_idx >= len(user.accounts):
                print("Invalid account selection.\n")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Invalid account selection.\n")
            time.sleep(2)  # Add delay for error message
            continue

    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be positive.")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")
            time.sleep(2)  # Add delay for error message
            continue

    try:
        user.accounts[acc_idx].withdraw(amount)
        print(f"Successfully withdrawn Rs. {amount}. New balance: Rs. {user.accounts[acc_idx].get_balance()}\n")
        time.sleep(2)  # Add 2 second delay
    except ValueError as e:
        print(f"Error: {e}\n")
        time.sleep(2)  # Add 2 second delay

def view_transactions():
    if not list_users():  # This will show users if they exist
        return

    while True:
        try:
            idx = int(input("Select user: ")) - 1
            if idx < 0 or idx >= len(users):
                print("Invalid user selection.\n")
                time.sleep(2)  # Add delay for error message
                continue
            break
        except ValueError:
            print("Invalid user selection.\n")
            time.sleep(2)  # Add delay for error message
            continue

    user = users[idx]
    if not user.accounts:
        print("No accounts found for this user.\n")
        time.sleep(2)  # Add delay for error message
        return

    print("\nAccounts and Transactions:")
    print("=" * 60)
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} (Account #{i+1})")
        print(f"Current Balance: Rs. {acc.get_balance()}")
        print("-" * 40)
        transactions = acc.get_transaction_history()
        if not transactions:
            print("No transactions found.")
        else:
            print("Transaction History:")
            for tx in transactions:
                print(f"  {tx}")
        print("-" * 40)
    print("\n")
    time.sleep(2)  # Add delay after showing transactions

