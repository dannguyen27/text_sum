from flask import Flask, request, render_template, jsonify
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the homepage (assuming you have an index.html template)

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    # Check if the request contains JSON
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Extract the 'text' field from the incoming JSON request
    text = request.json.get('text')

    # Check if text is provided
    if not text:
        return jsonify({"error": "No text provided"}), 400  # Return error if no text is sent

    # Process the text with spaCy
    doc = nlp(text)

    # Extract all sentences from the text
    sentences = [sent.text for sent in doc.sents]

    # Summarize: select the first 3 sentences or fewer if the text is short
    summary = " ".join(sentences[:3]) if len(sentences) >= 3 else " ".join(sentences)

    # Return the summary as JSON response
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
