import requests, json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {
        "raw_document": {"text": text_to_analyse}
    }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(
        url, json=myobj, headers=header
    )  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    dominant_emotion = "anger"
    dominant_emotion_score = anger_score
    if disgust_score > dominant_emotion_score:
        dominant_emotion = "disgust"
        dominant_emotion_score = disgust_score
    if fear_score > dominant_emotion_score:
        dominant_emotion = "fear"
        dominant_emotion_score = fear_score
    if joy_score > dominant_emotion_score:
        dominant_emotion = "joy"
        dominant_emotion_score = joy_score
    if sadness_score > dominant_emotion_score:
        dominant_emotion = "sadness"
        dominant_emotion_score = sadness_score
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }
