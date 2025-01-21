import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=headers)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }

    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions'][0:1][0]
        emotions = emotion['emotion']
        anger_score = emotion['emotion']['anger']
        disgust_score = emotion['emotion']['disgust']
        fear_score = emotion['emotion']['fear']
        joy_score = emotion['emotion']['joy']
        sadness_score = emotion['emotion']['sadness']
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }