from celery import Celery


app = Celery('sheduler',
              broker='redis://redis:6379/0',
              backend='redis://redis:6379/0',
              include=['src.task'])

app.conf.update(
    result_expires=3600,
    task_serializer='json',
    accept_content=['application/json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

if __name__ == '__main__':
    app.start()