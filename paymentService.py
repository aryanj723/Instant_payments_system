class PaymentService:
    def process_transaction(self, transaction):
        # Perform necessary validation and processing of the transaction
        # Update account balances and transaction status
        sender_account = transaction.sender.bank_accounts[0]
        receiver_account = transaction.receiver.bank_accounts[0]
        
        if sender_account.balance >= transaction.amount:
            sender_account.balance -= transaction.amount
            receiver_account.balance += transaction.amount
            transaction.status = "Completed"
        else:
            transaction.status = "Failed"
