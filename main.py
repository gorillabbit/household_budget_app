import tkinter as tk
from ui.main_window import MainWindow

def main():
    # メインアプリケーションウィンドウを作成
    root = tk.Tk()
    root.title("家計簿アプリ")

    # MainWindowクラスのインスタンスを作成
    main_window = MainWindow(root)

    # アプリケーションのメインループを開始
    root.mainloop()

if __name__ == "__main__":
    main()