import sqlite3

def query_database(db_path):
    # データベースに接続
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 確認したいテーブル名のリスト
    tables = ['Users', 'Transactions', 'Categories', 'Budgets', 'RecurringTransactions']

    for table in tables:
        print(f"Table: {table}")
        # テーブルの内容を取得
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        # 結果を出力
        for row in rows:
            print(row)
        print("\n")

    # データベース接続を閉じる
    conn.close()

# データベースファイルのパスを指定
db_path = 'household_budget.db'
query_database(db_path)