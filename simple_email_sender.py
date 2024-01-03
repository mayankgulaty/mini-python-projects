import smtplib
from email.message import EmailMessage
from getpass import getpass

def send_email(smtp_server, port, sender_email, password, recipient, subject, body, attachment=None):
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    if attachment:
        with open(attachment, 'rb') as file:
            file_data = file.read()
            file_name = file.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.send_message(msg)

    print("Email sent successfully!")

def main():
    smtp_server = input("Enter SMTP server address: ")
    port = int(input("Enter SMTP server port (usually 465 for SSL): "))
    sender_email = input("Enter your email address: ")
    password = getpass("Enter your email password: ")
    recipient = input("Enter recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")
    attachment = input("Enter the path of the attachment (or leave blank for none): ")

    send_email(smtp_server, port, sender_email, password, recipient, subject, body, attachment if attachment else None)

if __name__ == "__main__":
    main()
