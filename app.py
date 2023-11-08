from flask import Flask, render_template, request, jsonify
import joblib
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import re

app = Flask(__name__)

# Load the trained classifier and vectorizer
classifier = joblib.load('models/trained_classifier.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def preprocess_text(text):
    # Tokenize, remove stopwords, and perform basic text cleaning
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words('english')]
    cleaned_text = ' '.join(words)
    return cleaned_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        text = request.form['email_text']
        text = preprocess_text(text)
        text_vectorized = vectorizer.transform([text])
        result = classifier.predict(text_vectorized)[0]
        if result == 1:
            result_text = "SPAM: It is an illegitimate email!!!"
        else:
            result_text = "HAM: It is a legitimate email."
        return jsonify({'result': result_text})

if __name__ == '__main__':
    app.run(debug=True)

