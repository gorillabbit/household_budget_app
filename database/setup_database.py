import sqlite3

def create_database(db_path):
    # データベースに接続（ファイルが存在しない場合は新規作成される）
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Users テーブルの作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserName TEXT NOT NULL,
        Email TEXT NOT NULL,
        PasswordHash TEXT NOT NULL,
        DateCreated TEXT NOT NULL
    )
    ''')

    # Transactions テーブルの作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        Type TEXT NOT NULL,
        Amount REAL NOT NULL,
        CategoryID INTEGER,
        Date TEXT NOT NULL,
        Description TEXT,
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    )
    ''')

    # Categories テーブルの作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Type TEXT NOT NULL
    )
    ''')

    # Budgets テーブルの作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Budgets (
        BudgetID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        CategoryID INTEGER NOT NULL,
        Amount REAL NOT NULL,
        StartDate TEXT NOT NULL,
        EndDate TEXT NOT NULL,
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    )
    ''')

    # RecurringTransactions テーブルの作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS RecurringTransactions (
        RecurringTransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        Type TEXT NOT NULL,
        Amount REAL NOT NULL,
        CategoryID INTEGER,
        Frequency TEXT NOT NULL,
        StartDate TEXT NOT NULL,
        EndDate TEXT,
        Description TEXT,
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    )
    ''')

    # Accounts テーブルの作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Accounts (
    AccountID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    AccountName TEXT NOT NULL,
    AccountType TEXT,
    Balance REAL NOT NULL,
    Currency TEXT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
    )
    ''')
    
    # コミットして変更を保存
    conn.commit()

    # データベース接続を閉じる
    conn.close()

if __name__ == "__main__":
    db_path = 'household_budget.db'  # データベースファイルのパス
    create_database(db_path)