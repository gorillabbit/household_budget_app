class Budget:
    def __init__(self, budget_id, user_id, category_id, amount, start_date, end_date):
        self.budget_id = budget_id
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date