from server.app import celery, db
from server.sentiment import analyze_sentiment

@celery.task
def some_task():
    pass
