
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailDetails:
    def __init__(self, sender_email, recipient_email, subject, body):
        self.sender_email = sender_email
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body
        self.msg = MIMEMultipart()
        self._prepare_email()

    def _prepare_email(self):
        self.msg['From'] = self.sender_email
        self.msg['To'] = self.recipient_email
        self.msg['Subject'] = self.subject
        self.msg.attach(MIMEText(self.body, 'plain'))

    def get_message(self):
        return self.msg
