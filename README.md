# Spam Email Classifier

This repository contains code for a spam email classifier. It includes both the web application for classifying emails and the machine learning model for email classification. The code is divided into two main parts: the front end (HTML and JavaScript) for user interaction and the back end (Python) for email classification.

## Web Application

### HTML and JavaScript (Front End)
- `index.html`: The main HTML page that provides a web form for users to input email text and view the classification result.

### JavaScript (Front End)
- `app.js`: Handles user interactions and communicates with the server to classify emails.

## Server-Side (Python)

### Machine Learning Model
- `spam_classifier.py`: The Python script responsible for training and evaluating multiple machine learning classifiers for spam email classification. The best-performing classifier is saved for future use.

### Data Preparation
- The script loads the email dataset from a CSV file, preprocesses the text data, and splits it into training and testing sets.

### Machine Learning Classifiers
- The following classifiers are evaluated and tested: Naive Bayes, Random Forest, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Logistic Regression, and Decision Tree.

### Evaluation and Results
- The script performs k-fold cross-validation to assess classifier performance.
- The best-performing classifier, SVM, is selected based on test data accuracy.
- A confusion matrix and classification report are generated to evaluate the model's performance.

### Model Saving
- The trained SVM classifier and TF-IDF vectorizer are saved as .pkl files for future use.

## Getting Started

1. Clone the repository to your local machine.
2. Install the required Python libraries using `pip install -r requirements.txt`.
3. Run the `spam_classifier.py` script to train and evaluate the classifiers.
4. Start the web application using `python app.py`.

## Usage

1. Access the web application in your browser by navigating to the provided URL.
2. Enter email text in the web form and click the "Classify" button.
3. The web application will display whether the email is classified as spam or ham.

## License

This code is provided under an open-source license. See the LICENSE file for details.

## Acknowledgments

- This project was created as a demonstration of email classification and web development.
- The dataset used for training and evaluation is not included in this repository and should be obtained separately.

Feel free to customize and extend the code for your specific needs or integrate it into your projects.
