from celery import Celery


def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['RESULT_BACKEND'], broker=app.config['BROKER_URL'])
    celery.conf.update(app.config)
    return celery


app = Celery('jobvault')
app.config_from_object('your_config_module')

# Example of periodic task configuration
app.conf.beat_schedule = {
    'task-name': {
        'task': 'module.task_name',
        'schedule': 10.0,
    },
}