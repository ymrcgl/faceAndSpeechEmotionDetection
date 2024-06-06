from flask import Flask, request, jsonify
from Live_FER import video_detect as fer_video_detect, image_detect as fer_image_detect
from live_Voice import predict_voice as voice_predict
from FER_Camera import VideoCamera, image_predict as fer_image_predict

app = Flask(__name__)

def combine_predictions(image_emotion, audio_emotion):
    try:
        weighted_emotions = {
            'Angry': 0,
            'Disgust': 0,
            'Fear': 0,
            'Happy': 0,
            'Sad': 0,
            'Surprise': 0,
            'Neutral': 0
        }
        
        for emotion in image_emotion:
            weighted_emotions[emotion] += 0.7
        
        for emotion in audio_emotion:
            weighted_emotions[emotion] += 0.3
        
        combined_emotion = max(weighted_emotions, key=weighted_emotions.get)
        
        return {emotion: weighted_emotions[emotion] for emotion in weighted_emotions if weighted_emotions[emotion] > 0}
    except Exception as e:
        return str(e)

@app.route('/predict_combined', methods=['POST'])
def predict_combined():
    try:
        if 'image' not in request.files or 'audio' not in request.files:
            return jsonify({'error': 'Dosyalar sağlanmadı'}), 400
        
        image_file = request.files['image']
        audio_file = request.files['audio']

        if image_file.filename == '' or audio_file.filename == '':
            return jsonify({'error': 'Dosyalar seçilmedi'}), 400

        image_emotion = fer_image_predict(image_file)
        audio_emotion = voice_predict(audio_file)

        combined_emotion = combine_predictions(image_emotion, audio_emotion)
        return jsonify({'emotions': combined_emotion}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
