import spacy

nlp = spacy.load('en_core_web_sm')

def analyze_sentiment(data):
    sentiments = []
    for article in data:
        doc = nlp(article['text'])
        sentiment = doc.sentiment
        sentiments.append({'article_id': article['_id'], 'sentiment': sentiment})
    return sentiments
