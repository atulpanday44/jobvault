from celery import Celery

# Initialize Celery
app = Celery('notification_worker', broker='pyamqp://guest@localhost//')

@app.task
def send_email_notification(email, subject, message):
    # Simulate sending an email
    print(f'Sending email to: {email}')
    print(f'Subject: {subject}')
    print(f'Message: {message}')