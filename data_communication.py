import serial
import threading

class DataCommunication:
    def __init__(self, config_panel):
        # コンフィグパネルから設定を読み込む
        self.config_panel = config_panel
        self.serial_port = None
        self.is_connected = False
        # 接続ボタンにこのクラスのconnectメソッドを紐付ける
        self.config_panel.apply_button.config(command=self.connect)
        self.receive_thread = None  # 受信データ用のスレッド

    def connect(self):
        # シリアルポートに接続するメソッド
        if not self.is_connected:
            try:
                self.serial_port = serial.Serial(
                    self.config_panel.port_combo.get(),  # ポート
                    self.config_panel.baudrate_combo.get(),  # ボーレート
                    timeout=1  # タイムアウト
                )
                self.is_connected = True
                self.receive_thread = threading.Thread(target=self.receive_data)
                self.receive_thread.daemon = True
                self.receive_thread.start()
                print("接続しました")
            except Exception as e:
                print(f"接続に失敗しました: {e}")
        else:
            # 既に接続している場合、接続を閉じる
            self.disconnect()

    def disconnect(self):
        if self.is_connected:
            self.serial_port.close()
            self.is_connected = False
            print("接続を閉じました")

    def send_data(self, data):
        # データをシリアルポート経由で送信するメソッド
        if self.is_connected:
            self.serial_port.write(data.encode())

    def receive_data(self):
        # データを非同期に受信するメソッド
        while self.is_connected:
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline().decode().strip()
                print(f"受信データ: {data}")
                # TODO: ここで受信データを他のモジュールに渡すなどの処理を行う
