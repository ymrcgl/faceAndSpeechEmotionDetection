# faceAndSpeechEmotionDetection

Gerekli Python Kütüphaneleri
Flask==2.0.3
tensorflow==2.8.0
opencv-python-headless==4.5.5.64
numpy==1.21.5
librosa==0.8.1
scikit-learn==1.0.2
pydub==0.25.1

Ek Bağımlılıklar
ffmpeg: pydub kütüphanesi tarafından ses dosyalarını işlemek için kullanılır. ffmpeg'i sisteminize yüklemeniz gerekecektir.

Projeyi açarken Anaconda üzerinden açınız.

Gerekli Kütüphaneleri Yükleme

pip install -r requirements.txt

ffmpeg Yükleme

ffmpeg, ses dosyalarını işlemek için gereklidir. ffmpeg'i sisteminize yükleyin:
Linux:
sudo apt-get install ffmpeg

MacOS:
brew install ffmpeg

Windows:
https://ffmpeg.org/download.html bu adresten indirin.

Uygulamayı Çalıştırmadan önce yüz duygu modelini ve verileri indirmek ve proje dosyasına eklemeniz gerek. Aşağıdaki linkten gerekli dosyalara ulaşabilirsiniz.
https://drive.google.com/drive/folders/1fpA61sHVDgsUFGKSu4rQBaN8iHJJQ87S?usp=sharing

Uygulamayı Çalıştırma

Uygulamayı başlatmak için ana Python dosyasını çalıştırın.
python app.py



