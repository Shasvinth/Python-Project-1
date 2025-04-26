from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import uuid

class Transaction:
    VALID_TYPES = {"deposit", "withdraw"}
    
    def __init__(self, amount, transaction_type):
        # Convert and validate amount with proper rounding
        try:
            if isinstance(amount, str):
                amount = amount.strip()
            self.amount = Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            if self.amount <= 0:
                raise ValueError("Amount must be positive")
        except (InvalidOperation, TypeError):
            raise ValueError("Amount must be a valid number")
            
        transaction_type = transaction_type.lower().strip()
        if transaction_type not in self.VALID_TYPES:
            raise ValueError(f"Transaction type must be one of: {', '.join(self.VALID_TYPES)}")
            
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
        self.transaction_id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} [{self.transaction_id[:8]}] - {self.transaction_type.upper()}: Rs. {self.amount:.2f}"
