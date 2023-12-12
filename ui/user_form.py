import tkinter as tk
from tkinter import ttk
from db import Database

class UserForm:
    def __init__(self, parent):
        db = Database('household_budget.db')
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # ユーザー名の入力フィールド
        ttk.Label(self.frame, text="ユーザー名:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.username = ttk.Entry(self.frame)
        self.username.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        # メールアドレスの入力フィールド
        ttk.Label(self.frame, text="メールアドレス:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.email = ttk.Entry(self.frame)
        self.email.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        # メールアドレスの入力フィールド
        ttk.Label(self.frame, text="パスワード").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.password = ttk.Entry(self.frame)
        self.password.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        # 保存ボタン
        self.save_button = ttk.Button(self.frame, text="保存", command=self.on_submit)
        self.save_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

    def on_submit(self):
        db = Database('household_budget.db')
        # フォームデータの取得とデータベースへの保存処理
        username = self.username.get()
        email = self.email.get()
        password_hash = self.password.get()
        db.create_user(username, email, password_hash)
