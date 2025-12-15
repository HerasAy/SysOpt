import argparse
import time
import os
import sys
from modules.monitor import SystemMonitor
from modules.ai_engine import AIEngine
from modules.optimizer import Optimizer

def main():
    # 1. Komut satırı argümanlarını tanımla
    parser = argparse.ArgumentParser(description="SysOpt: Ubuntu Akıllı Sistem Yöneticisi")
    parser.add_argument('--mode', choices=['live', 'train', 'optimize'], required=True, help="Çalışma modu: live (izleme), train (eğitim), optimize (temizlik)")
    args = parser.parse_args()

    # 2. Modülleri başlat
    monitor = SystemMonitor()
    ai = AIEngine()
    optimizer = Optimizer()

    # Root kontrolü (Linux'ta sistem dosyalarına müdahale için şart)
    if os.geteuid() != 0:
        print("UYARI: Bu araç tam performans için 'sudo' ile çalıştırılmalıdır.")
        # Programı kapatmıyoruz ama kullanıcıyı uyarıyoruz.

    # --- MOD 1: EĞİTİM ---
    if args.mode == 'train':
        print("--- AI Eğitim Modu ---")
        success = ai.train()
        if not success:
            print("İpucu: Önce '--mode live' ile biraz veri toplayın.")

    # --- MOD 2: MANUEL OPTİMİZASYON ---
    elif args.mode == 'optimize':
        print("--- Manuel Optimizasyon Modu ---")
        optimizer.clear_ram_cache()
        optimizer.clean_package_cache()

    # --- MOD 3: CANLI İZLEME (LIVE) ---
    elif args.mode == 'live':
        print("--- Canlı İzleme ve Koruma Modu ---")
        print("Durdurmak için CTRL+C yapın.")
        
        try:
            while True:
                # Veriyi çek
                metrics = monitor.get_metrics()
                
                # Veriyi kaydet (gelecekteki eğitimler için)
                monitor.save_to_history(metrics)

                # Anomali kontrolü
                prediction = ai.detect_anomaly(metrics['cpu'], metrics['ram'], metrics['disk'])
                
                status = "\033[92mNORMAL\033[0m" # Yeşil renk
                if prediction == -1:
                    status = "\033[91mANOMALİ!\033[0m" # Kırmızı renk

                # Ekrana yaz
                output = (f"[{metrics['timestamp']}] "
                          f"CPU: %{metrics['cpu']} | "
                          f"RAM: %{metrics['ram']} | "
                          f"Disk: %{metrics['disk']} -> {status}")
                print(output)

                # OTO MÜDAHALE SENARYOSU
                # Eğer yapay zeka anomali dediyse VE RAM %85'in üstündeyse
                if prediction == -1 and metrics['ram'] > 85:
                    print(">>> KRİTİK DURUM: Otomatik temizlik başlatılıyor...")
                    optimizer.clear_ram_cache()

                time.sleep(2) # 2 saniyede bir döngü

        except KeyboardInterrupt:
            print("\nİzleme sonlandırıldı.")

if __name__ == "__main__":
    main()
