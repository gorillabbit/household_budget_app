import sqlite3

class Database:
    def __init__(self, db_path):
        """ データベースへの接続を初期化する """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_user(self, username, email, password_hash, date_created):
        """ 新しいユーザーを作成する """
        sql = '''INSERT INTO Users (UserName, Email, PasswordHash, DateCreated) VALUES (?, ?, ?, ?)'''
        self.cursor.execute(sql, (username, email, password_hash, date_created))
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

    # 他の必要なメソッド（例: カテゴリの追加、予算の設定など）をここに追加します。

    def close(self):
        """ データベース接続を閉じる """
        self.conn.close()