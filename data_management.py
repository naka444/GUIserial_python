import tkinter as tk
from tkinter import scrolledtext, messagebox
import csv
from datetime import datetime

class DataManager:
    def __init__(self, master, data_comm):
        self.data_comm = data_comm  # DataCommunicationインスタンスへの参照
        self.frame = tk.Frame(master)  # このモジュールのためのフレーム
        self.frame.grid(row=1, padx=10, pady=10)

        # 受信データを表示するスクロールテキストウィジェット
        self.data_text = scrolledtext.ScrolledText(self.frame, height=10, width=50)
        self.data_text.pack()

        # CSVに保存ボタン
        self.save_button = tk.Button(self.frame, text="Save to CSV", command=self.save_to_csv)
        self.save_button.pack()

        # 受信データを監視し、GUIに表示する
        # この機能を実装するには、DataCommunicationからデータを受け取る方法が必要です。
        # 例えば、DataCommunicationにコールバック関数を登録し、新しいデータがあるたびにこの関数を呼び出すようにすることができます。

    def display_data(self, data):
        """受信データをテキストエリアに表示する"""
        self.data_text.insert(tk.END, data + '\n')  # データの末尾に改行を追加
        self.data_text.see(tk.END)  # 最新のデータにスクロール

    def save_to_csv(self):
        """テキストエリアの内容をCSVファイルに保存する"""
        # ファイル名は現在の日時に基づいて自動生成
        filename = datetime.now().strftime("data_%Y-%m-%d_%H-%M-%S.csv")
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                # テキストエリアからすべての行を取得
                lines = self.data_text.get('1.0', tk.END).split('\n')
                for line in lines:
                    if line:  # 空の行は無視
                        writer.writerow([line])
            messagebox.showinfo("Success", f"Data saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")
