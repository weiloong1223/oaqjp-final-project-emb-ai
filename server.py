from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def emo_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input! Please try again!"
    
    else:
        return (
            "For the given statement, the system response is 'anger': {anger_score}, "
            "'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, "
            "and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
            ).format(
                anger_score=anger_score,
                disgust_score=disgust_score,
                fear_score=fear_score,
                joy_score=joy_score,
                sadness_score=sadness_score,
                dominant_emotion=dominant_emotion
                )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)