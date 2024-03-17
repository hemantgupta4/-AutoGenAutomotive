import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email_declaration = {
    "name": "send_mail",
    "description": "Sends an email using SMTP with a specified subject, body, and recipient.",
    "parameters": {
        "type": "object",
        "properties": {
            "subject": {
                "type": "string",
                "description": "The subject of the email"
            },
            "body": {
                "type": "string",
                "description": "The body content of the email"
            },
            "to_email": {
                "type": "string",
                "description": "The recipient's email address"
            }
        },
        "required": ["subject", "body", "to_email"]
    },
}


def send_mail(sender_email, recipient_email, subject, message):
    smtp_server = 'sandbox.smtp.mailtrap.io'
    smtp_port = 2525  
    smtp_username = '7469d377770dfb'
    smtp_password = '******'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(smtp_username, smtp_password)  
        server.send_message(msg)

        server.quit()

        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False

# # Example usage:
# sender_email = 'your_sender_email@example.com'
# recipient_email = 'recipient_email@example.com'
# subject = 'Test Email'
# message = 'This is a test email.'

# send_mail(sender_email, recipient_email, subject, message)
