class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.status = "Pending"

    def authorize_transaction(self):
        # Perform authorization checks and processes
        # Update transaction status accordingly
        self.status = "Authorized"
