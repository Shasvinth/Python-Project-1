from datetime import datetime

class Transaction:
    VALID_TYPES = {"deposit", "withdraw"}  # Define valid transaction types
    
    def __init__(self, amount, transaction_type):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if transaction_type.lower() not in self.VALID_TYPES:
            raise ValueError(f"Transaction type must be one of: {', '.join(self.VALID_TYPES)}")
            
        self.amount = float(amount)  # Convert to float for consistency
        self.transaction_type = transaction_type.lower()  # Normalize to lowercase
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.transaction_type.upper()}: Rs. {self.amount:.2f}"  # Format amount to 2 decimal places
