import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

class SerialConfigPanel:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, padx=10, pady=10)
        
        # シリアルポート選択
        ttk.Label(self.frame, text="Port:").grid(row=0, column=0)
        self.port_combo = ttk.Combobox(self.frame, values=[port.device for port in serial.tools.list_ports.comports()])
        self.port_combo.grid(row=0, column=1)

        # ボーレート選択
        ttk.Label(self.frame, text="Baudrate:").grid(row=1, column=0)
        self.baudrate_combo = ttk.Combobox(self.frame, values=[9600, 19200, 38400, 57600, 115200])
        self.baudrate_combo.grid(row=1, column=1)

        # 設定適用ボタン
        self.apply_button = ttk.Button(self.frame, text="Apply")
        self.apply_button.grid(row=2, column=0, columnspan=2)
