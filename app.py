from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load model once when server starts
print("Loading sentiment model...")
sentiment_model = pipeline("sentiment-analysis")
print("Model ready!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    review = data["review"]
    
    if not review.strip():
        return jsonify({"error": "Please enter a review"})
    
    # Run sentiment analysis
    result = sentiment_model(review[:512])[0]
    
    label = "Positive" if result["label"] == "POSITIVE" else "Negative"
    confidence = round(result["score"] * 100, 2)
    emoji = "😊" if label == "Positive" else "😞"
    
    return jsonify({
        "label": label,
        "confidence": confidence,
        "emoji": emoji
    })

if __name__ == "__main__":
    app.run(debug=True)