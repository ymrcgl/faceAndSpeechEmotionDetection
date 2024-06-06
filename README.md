# Face and Speech Emotion Detection

Bu proje, video ve ses verilerini kullanarak duygu tanıma işlemi gerçekleştiren bir web uygulamasıdır. Uygulama, Flask web çerçevesi ile geliştirilmiştir ve TensorFlow tabanlı derin öğrenme modelleri kullanmaktadır.

## Yüz Duygu Modeli ve Verileri İndirme

Uygulamayı çalıştırmadan önce yüz duygu modelini ve verileri indirmeniz daha sonra proje dosyasına eklemeniz gerek. Aşağıdaki linkten gerekli dosyalara ulaşabilirsiniz.

[Model ve Veriler](https://drive.google.com/drive/folders/1fpA61sHVDgsUFGKSu4rQBaN8iHJJQ87S?usp=sharing)

## Projeyi Açarken

Projeyi açarken Anaconda üzerinden açınız.
## Gerekli Python Kütüphaneleri

```plaintext
Flask==2.0.3
tensorflow==2.8.0
opencv-python-headless==4.5.5.64
numpy==1.21.5
librosa==0.8.1
scikit-learn==1.0.2
pydub==0.25.1
```

## Gerekli Kütüphaneleri Yükleme

```sh
pip install -r requirements.txt
```

## Ek Bağımlılıklar

ffmpeg: pydub kütüphanesi tarafından ses dosyalarını işlemek için kullanılır. ffmpeg'i sisteminize yüklemeniz gerekecektir.

### ffmpeg Yükleme

#### Linux:
```sh
sudo apt-get install ffmpeg
```

#### MacOS:
```sh
brew install ffmpeg
```

#### Windows:
[Bu adresten indirin](https://ffmpeg.org/download.html)







## Uygulamayı Çalıştırma

Uygulamayı başlatmak için ana Python dosyasını çalıştırın:

```sh
python app.py
```

---

Bu talimatları izleyerek, proje için gerekli tüm bağımlılıkları kurabilir ve uygulamayı çalıştırabilirsiniz. Uygulama, video ve ses verilerini işleyerek duygu tanıma işlemlerini gerçekleştirecektir.
