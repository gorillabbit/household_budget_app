class Transaction:
    def __init__(self, transaction_id, user_id, type, amount, category_id, date, description):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.type = type
        self.amount = amount
        self.category_id = category_id
        self.date = date
        self.description = description