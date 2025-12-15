import psutil
import time
import os
import csv
from datetime import datetime

class SystemMonitor:
    def __init__(self, data_file="data/system_logs.csv"):
        self.data_file = data_file
        # Eğer veri dosyası yoksa başlıkları (header) oluştur
        if not os.path.exists(self.data_file):
            with open(self.data_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "cpu", "ram", "disk"])

    def get_metrics(self):
        """
        Anlık sistem verilerini çeker ve döndürür.
        """
        metrics = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cpu": psutil.cpu_percent(interval=1), # 1 saniye ölçüm yapıp ortalamayı alır
            "ram": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
        return metrics

    def save_to_history(self, metrics):
        """
        AI'ın öğrenmesi için verileri CSV dosyasına kaydeder.
        """
        with open(self.data_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([metrics["timestamp"], metrics["cpu"], metrics["ram"], metrics["disk"]])

# Detaylı Açıklama:
# psutil: Linux'un /proc klasöründen donanım bilgilerini okur.
# csv: Verileri Excel benzeri bir formatta saklarız ki AI bunları okuyabilsin.
