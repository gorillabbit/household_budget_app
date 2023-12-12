import sqlite3

class Database:
    def __init__(self, db_path):
        """ データベースへの接続を初期化する """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_all_tables(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()

    def create_user(self, username, email, password_hash):
        """ 新しいユーザーを作成する """
        sql = '''INSERT INTO Users (UserName, Email, PasswordHash) VALUES (?, ?, ?)'''
        self.cursor.execute(sql, (username, email, password_hash))
        self.conn.commit()

    def add_transaction(self, user_id, type, amount, category_id, date, description):
        """ 新しい取引を追加する """
        sql = '''INSERT INTO Transactions (UserID, Type, Amount, CategoryID, Date, Description) VALUES (?, ?, ?, ?, ?, ?)'''
        self.cursor.execute(sql, (user_id, type, amount, category_id, date, description))
        self.conn.commit()

    def get_transactions_by_user(self, user_id):
        """ 特定のユーザーの取引を取得する """
        sql = '''SELECT * FROM Transactions WHERE UserID = ?'''
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchall()

    def create_account(self, user_id, account_name, account_type=None, balance=0, currency='JPY'):
        """ 新しい口座を作成する """
        sql = '''INSERT INTO Accounts (UserID, AccountName, AccountType, Balance, Currency) VALUES (?, ?, ?, ?, ?)'''
        self.cursor.execute(sql, (user_id, account_name, account_type, balance, currency))
        self.conn.commit()

    def update_account_balance(self, account_id, new_balance):
        """ 口座の残高を更新する """
        sql = '''UPDATE Accounts SET Balance = ? WHERE AccountID = ?'''
        self.cursor.execute(sql, (new_balance, account_id))
        self.conn.commit()

    def delete_account(self, account_id):
        """ 口座を削除する """
        sql = '''DELETE FROM Accounts WHERE AccountID = ?'''
        self.cursor.execute(sql, (account_id,))
        self.conn.commit()

    def add_transaction(self, user_id, type, amount, category_id, date, description, account_id=None):
        """ 新しい取引を追加し、関連する口座の残高を更新する """
        self.cursor.execute('''INSERT INTO Transactions (UserID, Type, Amount, CategoryID, Date, Description) VALUES (?, ?, ?, ?, ?, ?)''',
                            (user_id, type, amount, category_id, date, description))

        # 口座IDが指定されている場合、残高を更新
        if account_id is not None:
            # 現在の残高を取得
            self.cursor.execute('''SELECT Balance FROM Accounts WHERE AccountID = ?''', (account_id,))
            current_balance = self.cursor.fetchone()[0]

            # 残高を更新
            new_balance = current_balance + amount if type == 'income' else current_balance - amount
            self.update_account_balance(account_id, new_balance)

    # 他の必要なメソッド（例: カテゴリの追加、予算の設定など）をここに追加します。

    def close(self):
        """ データベース接続を閉じる """
        self.conn.close()