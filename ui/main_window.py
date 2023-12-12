import tkinter as tk
from tkinter import ttk
from .account_form import AccountForm  # AccountFormのインポート
from .user_form import UserForm
from .transaction_form import TransactionForm
from .recurring_transaction_form import RecurringTransactionForm
from db import Database

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.initialize_ui()

         # タブコントロールの作成
        self.tab_control = ttk.Notebook(root)
        self.account_tab = ttk.Frame(self.tab_control)
        self.transaction_tab = ttk.Frame(self.tab_control)
        self.category_tab = ttk.Frame(self.tab_control)
        self.recurring_tab = ttk.Frame(self.tab_control)
        self.user_tab = ttk.Frame(self.tab_control)

        # 各タブ内にTreeviewを配置
        self.setup_account_tree()
        self.setup_transaction_tree()
        self.setup_category_tree()
        self.setup_recurring_tree()
        self.setup_user_tree()

        self.tab_control.add(self.account_tab, text='口座管理')
        self.tab_control.add(self.transaction_tab, text='取引')
        self.tab_control.pack(expand=1, fill="both")

        self.tab_control.add(self.account_tab, text='口座')
        self.tab_control.add(self.transaction_tab, text='取引')
        self.tab_control.add(self.category_tab, text='カテゴリ')
        self.tab_control.add(self.recurring_tab, text='定期取引')
        self.tab_control.add(self.user_tab, text='ユーザー')
        self.tab_control.pack(expand=1, fill="both")

        # 口座管理フォームの追加
        self.account_form = AccountForm(self.account_tab)
        self.user_form = UserForm(self.user_tab)
        self.transaction_form = UserForm(self.transaction_tab)
        self.recurring_transaction_form = UserForm(self.recurring_tab)

        self.load_data()

    def setup_account_tree(self):
        # アカウント一覧のTreeviewを作成
        self.account_tree = ttk.Treeview(self.account_tab, columns=('AccountName', 'AccountType', 'Balance', 'Currency'))
        self.account_tree.heading('#0', text='Account ID')
        self.account_tree.heading('AccountName', text='Account Name')
        self.account_tree.heading('AccountType', text='Account Type')
        self.account_tree.heading('Balance', text='Balance')
        self.account_tree.column('#0', width=100)
        self.account_tree.column('AccountName', width=120)
        self.account_tree.column('AccountType', width=100)
        self.account_tree.column('Balance', width=100)
        self.account_tree.pack(fill=tk.BOTH, expand=True)
        # アカウントデータの読み込み（ダミーデータ）
        self.load_account_data()
    
    def load_account_data(self):
        # データベースからアカウントデータを読み込み、TreeViewに追加
        # ここでは、デモンストレーションのためのダミーデータを使用
        accounts = [
            (1, 'Checking Account', 'Checking', 1000.00),
            (2, 'Savings Account', 'Savings', 5000.00)
        ]
        for acc in accounts:
            self.account_tree.insert('', tk.END, text=acc[0], values=(acc[1], acc[2], acc[3]))

    def setup_transaction_tree(self):
        # 取引一覧のTreeviewを作成
        self.transaction_tree = ttk.Treeview(self.transaction_tab, columns=('Date', 'Type', 'Amount', 'Category'))
        self.transaction_tree.heading('#0', text='Transaction ID')
        self.transaction_tree.heading('Date', text='Date')
        self.transaction_tree.heading('Type', text='Type')
        self.transaction_tree.heading('Amount', text='Amount')
        self.transaction_tree.heading('Category', text='Category')
        self.transaction_tree.column('#0', width=100)
        self.transaction_tree.column('Date', width=100)
        self.transaction_tree.column('Type', width=100)
        self.transaction_tree.column('Amount', width=100)
        self.transaction_tree.column('Category', width=100)
        self.transaction_tree.pack(fill=tk.BOTH, expand=True)
        # 取引データの読み込み（ダミーデータ）
        self.load_transaction_data()
    
    def load_transaction_data(self):
        # データベースから取引データを読み込み、TreeViewに追加
        # ここでは、デモンストレーションのためのダミーデータを使用
        transactions = [
            (1, '2021-01-01', 'Income', 1000.00, 'Salary'),
            (2, '2021-01-02', 'Expense', 100.00, 'Groceries')
        ]
        for txn in transactions:
            self.transaction_tree.insert('', tk.END, text=txn[0], values=(txn[1], txn[2], txn[3], txn[4]))
        
    def setup_category_tree(self):
        self.category_tree = ttk.Treeview(self.category_tab)
        # カテゴリのTreeviewの設定
        # ...

    def setup_recurring_tree(self):
        self.recurring_tree = ttk.Treeview(self.recurring_tab)
        # 定期取引のTreeviewの設定
        # ...

    def setup_user_tree(self):
        # ユーザーのTreeviewの設定
        self.user_tree = ttk.Treeview(self.user_tab, columns=('Username', 'Email', 'Password_hash', 'Date_created'))
        self.user_tree.heading('#0', text='User ID')
        self.user_tree.heading('Username', text='Username')
        self.user_tree.heading('Email', text='Email')
        self.user_tree.heading('Password_hash', text='Password_hash')
        self.user_tree.heading('Date_created', text='Date_created')
        self.user_tree.column('#0', width=100)
        self.user_tree.column('Username', width=100)
        self.user_tree.column('Email', width=100)
        self.user_tree.column('Password_hash', width=100)
        self.user_tree.column('Date_created', width=100)
        self.user_tree.pack(fill=tk.BOTH, expand=True)

    def initialize_ui(self):
        # UIコンポーネントの初期化と配置
        pass

    def load_data(self):
        # Databaseインスタンスの初期化（データベースファイルのパスを指定）
        db = Database('household_budget.db')

        # アカウントデータの読み込み
        accounts = db.get_all_tables('Accounts')
        for account in accounts:
            self.account_tree.insert('', tk.END, text=account[0], values=(account[1], account[2], account[3], account[4]))

        # 取引データの読み込み
        transactions = db.get_all_tables('Transactions')
        for transaction in transactions:
            self.transaction_tree.insert('', tk.END, text=transaction[0])
        # 取引データをTreeviewに追加...

        users = db.get_all_tables('Users')
        for user in users:
            self.user_tree.insert('', tk.END, text=user[0], values=(user[1], user[2], user[3], user[4]))    