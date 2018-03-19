import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('email_id', 'password')
mail.list()
mail.select('inbox')
result, data = mail.uid('search', None, 'UNSEEN')
i = len(data[0].split())
for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    for response_part in email_data:
        if isinstance(response_part, tuple):
            response = response_part[1].decode('utf-8')
            original = email.message_from_string(response)
            sender = original['From']
            print(sender)
            data = original['Subject']
            print(data)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":  # ignore attachments/html
            body = part.get_payload(decode=True)
            body = body.decode('utf-8')
            print (body)
        else:
            continue
