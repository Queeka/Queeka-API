from __future__ import absolute_import, unicode_literals
import os
from setup.settings import test_settings
from datetime import timedelta
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings.test_settings')
app = Celery('setup', broker=test_settings.REDIS_URL,
            backend=test_settings.REDIS_URL)


app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.update(
    broker_connection_retry_on_startup=True,
    worker_cancel_long_running_tasks_on_connection_loss=True,
    worker_timeout=300,
)
worker_timeout = timedelta(minutes=5)

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
