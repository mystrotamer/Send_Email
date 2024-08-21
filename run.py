
from emailSender import EmailSender
from emailAttachment import EmailAttachment
from emailDetails import EmailDetails

def main():
    # Email details
    report_path = ""  # Report file path
    recipient_email = ""  # Recipient's email
    sender_email = ""  # Your email
    sender_password = ""  # Your email password

    # Create email details
    email_details = EmailDetails(sender_email, recipient_email,
                                 "Daily Report",
                                 "Please find the attached daily report.")
    
    # Attach the file
    attachment = EmailAttachment(report_path)
    attachment.attach_to_email(email_details.get_message())

    # Send the email
    email_sender = EmailSender(sender_email, sender_password)
    email_sender.send_email(email_details.get_message())

if __name__ == "__main__":
    main()
