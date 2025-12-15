import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
import os

class AIEngine:
    def __init__(self, model_path="data/model.pkl", data_path="data/system_logs.csv"):
        self.model_path = model_path
        self.data_path = data_path
        self.model = None
        self.load_model()

    def train(self):
        """
        Geçmiş verileri okur ve modeli eğitir.
        """
        if not os.path.exists(self.data_path):
            print("[AI] Hata: Veri dosyası bulunamadı.")
            return False

        try:
            # CSV'yi oku
            df = pd.read_csv(self.data_path)
            
            if len(df) < 10: # Test için sınır
                print(f"[AI] Yetersiz veri ({len(df)}). Biraz daha veri toplayın.")
                return False

            # Sadece eğitim verilerini al
            training_data = df[['cpu', 'ram', 'disk']]

            print("[AI] Model eğitiliyor...")
            self.model = IsolationForest(contamination=0.1, random_state=42)
            # Modeli Sütun İsimleriyle (DataFrame) eğitiyoruz
            self.model.fit(training_data)

            # Kaydet
            joblib.dump(self.model, self.model_path)
            print("[AI] Model eğitildi ve kaydedildi.")
            return True
        except Exception as e:
            print(f"[AI] Eğitim Hatası: {e}")
            return False

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)

    def detect_anomaly(self, cpu, ram, disk):
        """
        Anlık analiz yapar.
        """
        if self.model is None:
            return 1 
        
        # Veriyi Pandas DataFrame'e çeviriyoruz ki model sütun isimlerini görsün
        data_point = pd.DataFrame([[cpu, ram, disk]], columns=['cpu', 'ram', 'disk'])
        
        # Uyarıları bastırmak için (opsiyonel ama temiz log için iyi)
        import warnings
        warnings.filterwarnings("ignore", category=UserWarning)
        
        prediction = self.model.predict(data_point)
        return prediction[0]
