import tkinter as tk
from tkinter import ttk
from db import Database

class AccountForm:
    def __init__(self, parent):
        db = Database('household_budget.db')
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # ユーザーの入力フィールド
        ttk.Label(self.frame, text="ユーザー:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.user = ttk.Combobox(self.frame, values=db.get_all_tables('Users'))
        self.user.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        # 口座名の入力フィールド
        ttk.Label(self.frame, text="口座名:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.account_name = ttk.Entry(self.frame)
        self.account_name.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        # 口座種類の選択
        ttk.Label(self.frame, text="口座種類:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.account_type = ttk.Combobox(self.frame, values=["普通預金", "貯蓄預金", "その他"])
        self.account_type.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        # 初期残高の入力フィールド
        ttk.Label(self.frame, text="初期残高:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.initial_balance = ttk.Entry(self.frame)
        self.initial_balance.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        # 保存ボタン
        self.save_button = ttk.Button(self.frame, text="保存", command=self.on_submit)
        self.save_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)

        # 各種ウィジェットの構成を設定
        self.frame.columnconfigure(1, weight=1)
        
    def on_submit(self):
        user = self.user.get()
        account_name = self.account_name.get()
        account_type = self.account_type.get()
        initial_balance = self.initial_balance.get()
        db.create_account(user, account_name, account_type, initial_balance)