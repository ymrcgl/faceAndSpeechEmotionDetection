
# Face and Speech Emotion Detection in Real-time

This project is a web application that performs emotion recognition using video and audio data. The application is developed with the Flask web framework and utilizes TensorFlow-based deep learning models.

## Download Face Emotion Model and Data

Before running the application, you need to download the face emotion model and data, then add them to the project folder. You can access the necessary files from the link below.

[Model and Data](https://drive.google.com/drive/folders/1fpA61sHVDgsUFGKSu4rQBaN8iHJJQ87S?usp=sharing)

## Opening the Project

Please open the project through Anaconda.

## Required Python Libraries

```plaintext
Flask==2.0.3
tensorflow==2.8.0
opencv-python-headless==4.5.5.64
numpy==1.21.5
librosa==0.8.1
scikit-learn==1.0.2
pydub==0.25.1
```

## Installing Required Libraries

```sh
pip install -r requirements.txt
```

## Additional Dependencies

ffmpeg: Used by the pydub library to process audio files. You will need to install ffmpeg on your system.

### Installing ffmpeg

#### Linux:
```sh
sudo apt-get install ffmpeg
```

#### MacOS:
```sh
brew install ffmpeg
```

#### Windows:
[Download from this link](https://ffmpeg.org/download.html)

## Running the Application

To start the application, run the main Python file:

```sh
python app.py
```

---

By following these instructions, you can set up all the necessary dependencies for the project and run the application. The application will perform emotion recognition using video and audio data.



# Turkish Version
# Face and Speech Emotion Detection in Real-time

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
