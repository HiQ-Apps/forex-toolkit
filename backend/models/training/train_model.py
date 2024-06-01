import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import json
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from backend.models.parsers.processing import preprocess_text, vectorize_text


def load_data(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def prepare_data(data):
    texts = [item['content'] for item in data]
    labels = [1 if 'positive' in item['title'].lower() else 0 for item in data]  # Example labeling logic
    preprocessed_texts = [preprocess_text(text) for text in texts]
    return preprocessed_texts, labels

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    return model

def main():
    json_file = 'services/json/reuters_article.json'
    data = load_data(json_file)
    texts, labels = prepare_data(data)
    X, vectorizer = vectorize_text(texts)
    model = train_model(X, labels)
    # Save the model and vectorizer
    import pickle
    with open('sentiment_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    with open('vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)

if __name__ == "__main__":
    main()
