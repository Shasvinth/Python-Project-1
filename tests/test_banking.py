import pytest
from decimal import Decimal
from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount
from account.transaction import Transaction

def test_user_creation():
    # Test valid user creation
    user = User("John Doe", "john@example.com")
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    
    # Test invalid email
    with pytest.raises(ValueError):
        User("John Doe", "invalid-email")
        
    # Test invalid name (empty)
    with pytest.raises(ValueError):
        User("", "john@example.com")
        
    # Test invalid name (numbers)
    with pytest.raises(ValueError):
        User("John123", "john@example.com")

def test_account_creation():
    user = User("John Doe", "john@example.com")
    
    # Test savings account with valid initial balance
    savings = SavingsAccount(user.name, user.email, 200)
    assert savings.get_balance() == 200.0
    assert savings.get_account_type() == "Savings Account"
    
    # Test savings account with insufficient initial balance
    with pytest.raises(ValueError):
        SavingsAccount(user.name, user.email, 50)  # Below minimum 100
        
    # Test current account
    current = CurrentAccount(user.name, user.email, 2000)
    assert current.get_balance() == 2000.0
    assert current.get_account_type() == "Current Account"
    
    with pytest.raises(ValueError):
        CurrentAccount(user.name, user.email, 500)  # Below minimum 1000

def test_transaction_creation():
    # Test valid transaction
    tx = Transaction("100.50", "deposit")
    assert tx.amount == Decimal("100.50")
    assert tx.transaction_type == "deposit"
    assert tx.transaction_id is not None
    
    # Test invalid amount
    with pytest.raises(ValueError):
        Transaction("-50", "deposit")
        
    # Test invalid type
    with pytest.raises(ValueError):
        Transaction("100", "invalid_type")

def test_deposit_withdraw():
    account = SavingsAccount("John Doe", "john@example.com", 500)
    
    # Test deposit
    initial = account.get_balance()
    account.deposit(200)
    assert account.get_balance() == initial + 200
    
    # Test withdraw
    account.withdraw(100)
    assert account.get_balance() == initial + 100
    
    # Test withdraw below minimum balance
    with pytest.raises(ValueError, match="maintain minimum balance"):
        account.withdraw(500)  # Would go below minimum 100
        
    # Test transaction history
    history = account.get_transaction_history()
    assert len(history) == 2  # One deposit, one withdrawal
    assert history[0].transaction_type == "deposit"
    assert history[1].transaction_type == "withdraw"

def test_decimal_precision():
    account = SavingsAccount("John Doe", "john@example.com", 500)
    
    # Test that decimal places are handled correctly with rounding
    account.deposit("100.125")  # Should round to 100.13
    assert account.get_balance() == 600.13
    
    account.withdraw("50.125")  # Should round to 50.13
    assert account.get_balance() == 550.00

def test_student_account():
    # Test student account specific features
    account = StudentAccount("Student Name", "student@example.com", 200)
    assert account.get_account_type() == "Student Account"
    
    # Verify minimum balance requirement
    with pytest.raises(ValueError):
        account.withdraw(150)  # Would go below minimum 100