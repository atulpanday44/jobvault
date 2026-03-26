import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotificationService:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        # Create a multipart email
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        try:
            # Configure and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(self.username, self.password)
                server.send_message(msg)
                print('Email sent successfully!')
        except Exception as e:
            print(f'Failed to send email: {e}')