class Account:
    def __init__(self, account_id, user_id, account_name, account_type, balance, currency):
        self.account_id = account_id      # 口座ID
        self.user_id = user_id            # ユーザーID
        self.account_name = account_name  # 口座名
        self.account_type = account_type  # 口座の種類（例：普通預金、貯蓄預金など）
        self.balance = balance            # 現在の残高
        self.currency = currency          # 通貨タイプ

    # このモデルに対する他のメソッド（例：口座残高を更新するメソッドなど）をここに追加できます。
