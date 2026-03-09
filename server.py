"""Flask application for emotion detection.

This module provides a web interface for analyzing emotions in text
using the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """Analyze emotions in the provided text.

    Returns:
        str: Formatted response with emotion scores or error message
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': \
    {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The \
    dominant emotion is {response['dominant_emotion']}."


@app.route("/")
def render_index_page():
    """Render the main index page.

    Returns:
        str: Rendered HTML template
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
