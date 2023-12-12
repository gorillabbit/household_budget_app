import tkinter as tk
from tkinter import ttk
from db import Database

class RecurringTransactionForm:
    def __init__(self, parent):
        self.db = Database('household_budget.db')
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # 定期取引タイプの選択
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

        # 開始日の入力フィールド
        ttk.Label(self.frame, text="開始日:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.start_date = ttk.Entry(self.frame)
        self.start_date.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        # 終了日の入力フィールド（オプショナル）
        ttk.Label(self.frame, text="終了日:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.end_date = ttk.Entry(self.frame)
        self.end_date.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)

        # 頻度の入力フィールド
        ttk.Label(self.frame, text="頻度:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.frequency = ttk.Entry(self.frame)
        self.frequency.grid(row=5, column=1, padx=5, pady=5, sticky=tk.EW)

        # 保存ボタン
        self.save_button = ttk.Button(self.frame, text="保存", command=self.on_submit)
        self.save_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.E)

    def on_submit(self):
        # フォームデータの取得
        transaction_type = self.transaction_type.get()
        amount = self.amount.get()
        category = self.category.get()
        start_date = self.start_date.get()
        end_date = self.end_date.get()
        frequency = self.frequency.get()

        # データベースに定期取引を保存
        # ここではデータベースへの保存方法は省略しています
        # 実際には、self.db.add_recurring_transaction(...) のようにデータベース操作を行う
        print(f"保存される定期取引: {transaction_type}, {amount}, {category}, {start_date}, {end_date}, {frequency}")
