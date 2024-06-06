import numpy as np
import librosa
from tensorflow.keras.models import load_model  # type: ignore
from sklearn.preprocessing import StandardScaler
import os
from flask import Flask, request, jsonify
import logging
from pydub import AudioSegment

# Loglama ayarları
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Model ve ölçekleyiciyi yükleme
MODEL_PATH = 'C:/Users/Oztur/OneDrive/Desktop/website/sesmodeli2.keras'
model = load_model(MODEL_PATH)
scaler = StandardScaler()

# Örnek veri ile scaler'ı başlatma
sample_data = np.random.rand(100, 40)  # Rastgele MFCC benzeri veri oluşturma
scaler.fit(sample_data)

# Ses önişleme
def preprocess_audio(file_path, scaler, max_len=174):
    try:
        logging.debug(f"Ses dosyası yükleniyor: {file_path}")
        y, sr = librosa.load(file_path, sr=None)
        y = y.astype(np.float32)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)  # n_mfcc'i 40 olarak değiştirdik
        pad_width = max_len - mfccs.shape[1]
        if pad_width > 0:
            mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
        else:
            mfccs = mfccs[:, :max_len]
        mfccs_scaled = scaler.transform(mfccs.T)
        mfccs_scaled = mfccs_scaled.T  # Transpose to match the shape
        mfccs_scaled = mfccs_scaled[..., np.newaxis]  # (40, 174) -> (40, 174, 1)
        mfccs_scaled = np.expand_dims(mfccs_scaled, axis=0)  # (40, 174, 1) -> (1, 40, 174, 1)
        return mfccs_scaled
    except Exception as e:
        logging.exception("Ses ön işleme sırasında hata oluştu:")
        return None

# Duygu tahmini
def predict_emotion(file_path):
    processed_audio = preprocess_audio(file_path, scaler)
    if processed_audio is not None:
        prediction = model.predict(processed_audio)
        emotion = np.argmax(prediction)
        return emotion
    else:
        return None

# WAV formatına dönüştürme
def convert_to_wav(input_file, output_file):
    try:
        logging.debug(f"{input_file} dosyası WAV formatına dönüştürülüyor: {output_file}")
        audio = AudioSegment.from_file(input_file)
        audio = audio.set_channels(1)  # Mono kanal ayarlama
        audio.export(output_file, format="wav")
    except Exception as e:
        logging.exception("WAV dönüştürme sırasında hata oluştu:")
        raise e  # Hatanın yeniden iletilmesi

# HTTP POST isteği işleme
@app.route('/predict_voice', methods=['POST'])
def predict_voice():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Dosya sağlanmadı'}), 400
        file = request.files['file']

        # Yüklenen dosyanın geçerli olup olmadığını kontrol etme
        if file.filename == '':
            return jsonify({'error': 'Dosya seçilmedi'}), 400

        # Dosya yükleme ve gerekirse dönüştürme
        file_path = 'C:/Users/Oztur/OneDrive/Desktop/website/temp_audio.wav'
        if not file.filename.endswith('.wav'):
            temp_path = 'temp_audio.tmp'
            file.save(temp_path)
            convert_to_wav(temp_path, file_path)
            os.remove(temp_path)  # Geçici dosyayı silme
        else:
            file.save(file_path)

        # Duygu tahmini
        predicted_emotion = predict_emotion(file_path)
        if predicted_emotion is not None:
            emotion_labels = ['angry', 'disgust', 'fearful', 'happy', 'neutral', 'sad', 'suprised']
            result = emotion_labels[predicted_emotion]
            logging.info(f"Tahmin edilen duygu: {result}")

            # Geçici dosyanın varlığını kontrol et ve varsa sil
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({'emotion': result}), 200
        else:
            # Geçici dosyanın varlığını kontrol et ve varsa sil
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({'error': 'Ses ön işleme başarısız oldu'}), 500
    except Exception as e:
        logging.exception("Tahmin sırasında hata oluştu:")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)