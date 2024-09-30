from transformers import pipeline
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Use Hugging Face summarizer
    summary = summarizer(text, max_length=200, min_length=30, do_sample=False)

    # Return the summary
    return jsonify({"summary": summary[0]['summary_text']})

if __name__ == '__main__':
    app.run(debug=True)
