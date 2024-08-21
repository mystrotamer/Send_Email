
from email.mime.base import MIMEBase
from email import encoders
import os

class EmailAttachment:
    def __init__(self, report_path):
        self.report_path = report_path

    def attach_to_email(self, msg):
        attachment = open(self.report_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(self.report_path)}")
        msg.attach(part)
