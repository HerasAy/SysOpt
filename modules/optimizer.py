import os
import subprocess

class Optimizer:
    def clear_ram_cache(self):
        """
        Linux PageCache, dentries ve inodes temizler.
        Bellek (RAM) şiştiğinde sistemi rahatlatır.
        """
        print("[OPT] RAM Önbelleği temizleniyor...")
        try:
            # Bu komut root yetkisi gerektirir.
            # 'sync' verilerin diske yazılmasını sağlar, veri kaybını önler.
            os.system("sync; echo 3 > /proc/sys/vm/drop_caches")
            print("[OPT] RAM temizliği başarılı.")
        except Exception as e:
            print(f"[OPT] Hata: {e}")

    def clean_package_cache(self):
        """
        Gereksiz apt paketlerini temizler (Disk temizliği).
        """
        print("[OPT] Paket önbelleği temizleniyor...")
        try:
            subprocess.run(['apt-get', 'clean'], stdout=subprocess.DEVNULL)
            subprocess.run(['apt-get', 'autoremove', '-y'], stdout=subprocess.DEVNULL)
            print("[OPT] Paket temizliği tamamlandı.")
        except Exception as e:
            print(f"[OPT] Hata: {e}")

# Detaylı Açıklama:
# echo 3 > /proc/sys/vm/drop_caches: Bu Linux'un sihirli komutudur.
# Sistem tarafından tamponlanan ama şu an kullanılmayan RAM'i serbest bırakır.
