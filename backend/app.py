# server/app.py
from flask import Flask
from flask_socketio import SocketIO
from celery import Celery
from pymongo import MongoClient

from backend.celery import tasks

app = Flask(__name__)
app.config.from_object("server.config")
socketio = SocketIO(app)

# Initialize MongoDB
client = MongoClient(app.config["MONGO_URI"])
db = client.get_database()

# Initialize Celery
def make_celery(app):
    celery = Celery('server.app', broker=app.config["CELERY_BROKER_URL"])
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

from backend import routes
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
