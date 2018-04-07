import imaplib
import email
from Speech import chat_speak
def reading():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('', '')
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, 'UNSEEN')
    if data[0]==b'':
        chat_speak("No new mails")
        print("No new mails")
    for num in data[0].split():
        #latest_email_uid = data[j].split()[x]
        results, email_data = mail.uid('fetch', num, '(RFC822)')
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        for response_part in email_data:
            if isinstance(response_part, tuple):
                response = response_part[1].decode('utf-8')
                original = email.message_from_string(response)
                sender = original['From']
                chat_speak("There is a message from")
                chat_speak(sender)
                print("Sender: "+sender)
                data = original['Subject']
                chat_speak("With subject")
                chat_speak(data)
                print("Subject: "+data)
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":  # ignore attachments/html
                body = part.get_payload(decode=True)
                body = body.decode('utf-8')
                chat_speak("The message content is")
                chat_speak(body)
                print ("Message content is: "+body)
            else:
                continue
