from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyse = request.args.get('textToAnalyse')
    response = emotion_detector(text_to_analyse)

    emotions = response['anger']['disgust']['fear']['joy']['sadness']
    dominant_emotion = response['dominant_emotion']
    # Return a formatted string with the sentiment label and score
    return "For the given statement, the system response is {}. The dominant emotion is {}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)