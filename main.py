import tkinter as tk
from serial_config import SerialConfigPanel
from data_communication import DataCommunication
from data_management import DataManager

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("Serial Communication App")

        # シリアルポート設定パネル
        self.serial_config_panel = SerialConfigPanel(master)
        
        # データ通信管理
        self.data_comm = DataCommunication(self.serial_config_panel)
        
        # データ管理
        self.data_manager = DataManager(master, self.data_comm)

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
