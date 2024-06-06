from flask import Flask, render_template, Response, request, jsonify
from FER_Camera import VideoCamera
from live_Voice import predict_voice
from Live_FER import video_detect as fer_video_detect

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
        
        return combined_emotion
    except Exception as e:
        return str(e)
    
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

def generate(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(generate(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/video")
def video():
    return render_template("video.html")

@app.route("/predict_voice", methods=['POST'])
def predict_voice_endpoint():
    return predict_voice()

@app.route("/predict_combined", methods=['POST'])
def predict_combined():
    if request.method == 'POST':
        try:
            if 'audio' not in request.files:
                return jsonify({'error': 'Ses dosyası sağlanmadı'}), 400
            
            audio_file = request.files['audio']

            if audio_file.filename == '':
                return jsonify({'error': 'Ses dosyası seçilmedi'}), 400

            audio_emotion = predict_voice(audio_file)

            video_emotion = fer_video_detect()  # Video duygu tahmini al

            combined_emotion = combine_predictions(video_emotion, audio_emotion)
            return jsonify({'emotion': combined_emotion}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Yalnızca POST istekleri kabul edilmektedir'}), 405

if __name__ == '__main__':
    app.run(debug=True)
