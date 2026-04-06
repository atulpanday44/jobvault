import os

class Config:
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///default.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis settings
    REDIS_URL = os.getenv('REDIS_URL') or 'redis://localhost:6379/0'

    # SMTP settings
    SMTP_SERVER = os.getenv('SMTP_SERVER') or 'smtp.example.com'
    SMTP_PORT = int(os.getenv('SMTP_PORT') or 587)
    SMTP_USE_TLS = os.getenv('SMTP_USE_TLS') in ['true', '1', 'True']
    SMTP_USERNAME = os.getenv('SMTP_USERNAME') or 'user@example.com'
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD') or 'password'

    # Celery settings
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') or REDIS_URL
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') or REDIS_URL