# 🚀 SysOpt: AI Tabanlı Sistem Optimizasyon Aracı

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Ubuntu%2FLinux-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

**SysOpt**, Ubuntu/Linux sistemlerinin performansını yapay zeka ile izleyen, anomalileri tespit eden ve darboğaz anlarında sistemi otomatik olarak optimize eden akıllı bir araçtır.

Sistem yöneticilerinin (SysAdmin) iş yükünü hafifletmek için tasarlanan SysOpt, kaynak tüketimini (CPU, RAM, Disk) öğrenir ve "normal" dışı davranışlarda (Anomali) önbellek temizliği gibi otomatik müdahaleler gerçekleştirir.

---

## 🌟 Özellikler

*   **📊 Anlık Sistem İzleme:** CPU, RAM ve Disk kullanımını gerçek zamanlı takip eder.
*   **🧠 Yapay Zeka Destekli Analiz:** `Scikit-learn` ve `Isolation Forest` algoritması ile sistemin normal davranışını öğrenir ve sapmaları (anomalileri) tespit eder.
*   **⚡ Otomatik Optimizasyon:** Kritik seviyelerde (örneğin aşırı RAM kullanımı) otomatik olarak önbellek (PageCache, dentries) temizliği yapar.
*   **🔄 Kendi Kendine Öğrenme:** Toplanan log verileriyle modelini sürekli güncelleyebilir.
*   **⚙️ Systemd Entegrasyonu:** Arka planda bir Linux servisi olarak sessizce çalışır.

---

## 📂 Proje Yapısı

| Dosya/Klasör Yolu | Açıklama |
| :--- | :--- |
| `sysopt/` | |
| `├── data/` | Veri setleri ve AI modeli |
| `│   ├── system_logs.csv` | Geçmiş sistem verileri |
| `│   └── model.pkl` | Eğitilmiş Isolation Forest modeli |
| `├── modules/` | Uygulama modülleri |
| `│   ├── monitor.py` | Veri toplama (psutil) |
| `│   ├── ai_engine.py` | Anomali tespiti (ML) |
| `│   └── optimizer.py` | Sistem temizliği (subprocess) |
| `├── main.py` | Ana çalıştırma dosyası |
| `├── requirements.txt` | Gerekli kütüphaneler |
| `└── README.md` | Dokümantasyon |

---

## 🛠️ Kurulum
SysOpt'u sisteminin kurulumu için aşağıdaki adımları izleyin.
1. Gereksinimler 
<br>*Ubuntu/Debian tabanlı bir Linux sistemi
<br>*Python 3.8 veya üzeri
<br>*sudo(Sistem temizliği için gereklidir)
2. Projeyi Klonlama ve Hazırlık 
```bash
# Projeyi indirin (veya oluşturun)
git clone https://github.com/HerasAy/SysOpt.git
cd sysopt

# Sanal ortam oluşturun (Tavsiye edilen)
python3 -m venv venv
source venv/bin/activate

# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt
```

Not: `psutil` yüklenirken hata durumunda sistem geliştirme paketlerini yükleyin: `sudo apt install python3-dev build-essential`

---

## 🚀 Kullanım  
SysOpt üç farklı modda çalışıyor. Tüm modları `main.py`üzerinden yönetebilirsiniz.
1. Canlı İzleme Modu<br>
Sistemi anlık izler, verileri kaydeder ve anomali durumunda müdahale eder.
```bash
sudo ./venv/bin/python3 main.py --mode live
```
2. Eğitim Modu (Tren)<br>
Toplanan verileri `(data/system_logs.csv)` kullanarak yapay zekayı eğitir. İlk kurulumdan sonra veya belirli aralıklarla çalıştırılmalıdır.
```bash
./venv/bin/python3 main.py --mode train
```
3. Manuel Opt<br>
Yapay zekayı beklemeden manuel temizlik yapar.
```bash
sudo ./venv/bin/python3 main.py --mode optimize
```
## 🤖 Arka Planda Çalıştırma (Servis)
SysOpt'un sunucu `systemd` servisi olarak ekleyebilirsiniz.<br>
1. Servis dosyasını oluşturun:`/etc/systemd/system/sysopt.service`<br>
2. Aşağıdaki içeriği dosya yollarını kendinize göre düzenleyerek yapıştırın (`KULLANICI_ADI` kısımlarını değiştirmeyi unutmayın) <br>
```bash
[Unit]
Description=SysOpt - AI Based System Optimizer
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/KULLANICI_ADI/sysopt
ExecStart=/home/KULLANICI_ADI/sysopt/venv/bin/python3 main.py --mode live
Restart=always

[Install]
WantedBy=multi-user.target
```

Servisi etkinleştirin:
```bash
sudo systemctl daemon-reload
sudo systemctl enable sysopt
sudo systemctl start sysopt
```
---

## ⚠️ Bilinen Uyarılar ve Çözümler
* **UserWarning: X does not have valid feature names...**
  * Bu uyarı, model `ai_engine.py` dosyasında verileri `pd.DataFrame` formatına çevirerek bu sorun giderilmiştir.

* **Permission Denied:**
  * Optimizasyon işlemleri (RAM temizliği vb.) root yetkisi gerektirir. Scripti `sudo` ile çalıştırdığınızdan emin olun.


---

Bu proje deneme amacıyla yapılmıiştır. Geliştirmeye ve farklılaştırmaya açıktır.

