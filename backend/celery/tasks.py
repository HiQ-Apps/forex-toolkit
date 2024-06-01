from backend.app import celery, db

@celery.task
def some_task():
    pass
