import tkinter as tk
from tkinter import ttk
from db import Database

class TransactionForm:
    def __init__(self, parent):
        self.db = Database('household_budget.db')
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # 取引タイプの選択
        ttk.Label(self.frame, text="取引タイプ:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.transaction_type = ttk.Combobox(self.frame, values=["収入", "支出"])
        self.transaction_type.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        # 金額の入力フィールド
        ttk.Label(self.frame, text="金額:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.amount = ttk.Entry(self.frame)
        self.amount.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        # カテゴリの入力フィールド
        ttk.Label(self.frame, text="カテゴリ:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.category = ttk.Entry(self.frame)
        self.category.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        # 説明の入力フィールド
        ttk.Label(self.frame, text="説明:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.description = ttk.Entry(self.frame)
        self.description.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        # 保存ボタン
        self.save_button = ttk.Button(self.frame, text="保存", command=self.on_submit)
        self.save_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)

    def on_submit(self):
        # フォームデータの取得
        transaction_type = self.transaction_type.get()
        amount = self.amount.get()
        category = self.category.get()
        description = self.description.get()

        # データベースに取引を保存
        # ここではデータベースへの保存方法は省略しています
        # 実際には、self.db.add_transaction(...) のようにデータベース操作を行う
        print(f"保存される取引: {transaction_type}, {amount}, {category}, {description}")
