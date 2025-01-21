import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=headers)

    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['fear']
    joy_score = formatted_response['emotionPredictions'][0]['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['sadness']

    dominant_emotion = max(formatted_response, key=formatted_response.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }