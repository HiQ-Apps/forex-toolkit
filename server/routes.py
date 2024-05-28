from flask import request, jsonify
from .app import app, db

@app.route('/api/news', methods=['GET'])
def get_news():
    news = db.news.find()
    return jsonify([article for article in news])

@app.route('/api/sentiment', methods=['GET'])
def get_sentiment():
    sentiments = db.sentiments.find()
    return jsonify([sentiment for sentiment in sentiments])
