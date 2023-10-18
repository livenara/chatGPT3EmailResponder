import openai
import smtplib
import imaplib
import email
from email import policy
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import base64

# API Settings
openApiKey   = 'sk-XXXXXXXXXXXXXXXXXXXXXXX'

# Mail Settings
imapServer   = 'imap.server.jp' # do not support POP3.
smtpServer   = 'smtp.server.jp'
mailAddress  = 'mail@address.com'
mailPassword = 'mailPassword'

sleepTime = 60 # mail check interval


class EmailClient:
    def __init__(self, imap_server, smtp_server, email, password):
        self.imap_server = imap_server
        self.smtp_server = smtp_server
        self.email = email
        self.password = password

    def get_unread_emails(self):
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email, self.password)
        mail.select('inbox')
        status, messages = mail.search(None, 'UNSEEN') # status
        
        emails = []
        for message_id in messages[0].split():
            _, msg = mail.fetch(message_id, '(RFC822)')
            for response_part in msg:
                if isinstance(response_part, tuple):
                    email_message = email.message_from_bytes(response_part[1], policy=policy.default)
                    emails.append(email_message)
        mail.logout()
        return emails

    def send_email(self, to_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP_SSL(self.smtp_server, 465)
        server.login(self.email, self.password)
        server.sendmail(self.email, to_email, msg.as_string())
        server.quit()

openai.api_key = openApiKey

email_client = EmailClient(imapServer, smtpServer, mailAddress, mailPassword)

while True:
    unread_emails = email_client.get_unread_emails()

    for unread_email in unread_emails:
        sender_email = unread_email['from']
        email_body = base64.b64decode(unread_email.get_payload()).decode('utf-8').replace('\n', '')
        # GPTのレスポンスを取得
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=email_body,
            max_tokens=2000
        )
        gpt3_response = response.choices[0].text.strip()
        # レスポンスを元のメールアドレスに返信
        email_client.send_email(
            to_email=sender_email,
            subject='Reply from ChatGPT',
            message=gpt3_response
        )
    
    time.sleep(sleepTime)