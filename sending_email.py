import smtplib
from email.mime.text import MIMEText
import email
import imaplib
import getpass
import sys
import re
from Speech import chat_speak
from pprint import pprint as pp
smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465

SEARCH_FOLDER = '"[Gmail]/All Mail"'
found = 0
count = 0
DEFAULT_MAIL_SERVER = 'imap.gmail.com'
ADDR_PATTERN = re.compile('<(.*?)>')
target =[]
username = 'naik.sushma12345@gmail.com'  # input("Full email address: ")
password = 'sreegayatri'  # input('Password: ')

def sending(target_mail):
        print(target_mail)
        chat_speak("Message content")
        content = input('Message content: ')
        msg = MIMEText(content)
        chat_speak("Subject")
        msg['Subject'] = input('Subject: ')
        msg['From'] = username
        msg['To'] = ', '.join(target)
        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(username, target, msg.as_string())
        chat_speak("Mail sent")
        print('Mail sent')
        server.quit()
        return
def connect(user, pwd, server=DEFAULT_MAIL_SERVER):
    """Connect to [the specified] mail server. Return an open connection"""
    conn = imaplib.IMAP4_SSL(server)
    try:
        conn.login(user, pwd)
    except imaplib.IMAP4.error:
        chat_speak("Failed to login, try again")
        print ("Failed to login")
        sys.exit(1)
    return conn

def get_folder(conn, folder_name):
    """Fetch a specific folder (or label) from server"""
    if conn.state == "SELECTED":
        # Explicitly close any previously opened folders; may not be necessary
        conn.close()

    rv, data = conn.select(folder_name)
    if rv != 'OK':
        print ("Could not open specified folder. Known labels:")
        print_folders(conn)
    return conn


def get_email_ids(conn, query='ALL'):
    """Get the numeric IDs for all emails in a given folder"""
    if conn.state != "SELECTED":
        raise imaplib.IMAP4.error("Cannot search without selecting a folder")

    rv, data = conn.uid('search', None, query)
    if rv != 'OK':
        print ("Could not fetch email ids")  # for some reason...
        return []

    return data[0].split()

def print_folders(conn):
    """Print a list of open mailbox folders"""
    for f in conn.list():
        print ("\t", f)

def fetch_message(conn, msg_uid ):
    """
    Fetch a specific message uid (not sequential id!) from the given folder;
    return the parsed message. User must ensure that specified
    message ID exists in that folder.
    """
    # TODO: Could we fetch just the envelope of the response to save bandwidth?
    rv, data = conn.uid('fetch', msg_uid, "(RFC822)")
    if rv != 'OK':
        print ("ERROR fetching message #", msg_uid)
        return {}

    return email.message_from_bytes(data[0][1])  # dict-like object


def get_recipients(msg_parsed):
    """Given a parsed message, extract and return recipient list"""
    recipients = []
    addr_fields = ['From', 'To', 'Cc', 'Bcc']

    for f in addr_fields:
        rfield = msg_parsed.get(f, "") # Empty string if field not present
        rlist = re.findall(ADDR_PATTERN, rfield)
        recipients.extend(rlist)

    return recipients

def send_initiate():
    target.clear()
    username = 'naik.sushma12345@gmail.com'  # input("Full email address: ")
    password = 'sreegayatri'  # input('Password: ')
    # Connect
    mail_conn = connect(username, password)

    # Open a specific folder and get list of email message uids
    mail_conn = get_folder(mail_conn, SEARCH_FOLDER)
    msg_uid_list = get_email_ids(mail_conn)

    # Fetch a list of recipients
    all_recipients = []
    user_list = []
    for msg_uid in msg_uid_list:
        # msg = fetch_message(mail_conn, msg_uid)
        msg = fetch_message(mail_conn, msg_uid)
        recip_list = get_recipients(msg)
        all_recipients.extend(recip_list)

    print("List of all recipients:")
    print("------------")
    all_recipients = list(set(all_recipients))
    try:
        with open('contact_list.txt', 'r') as f:
            user_list = [line.rstrip('\n') for line in f]
    except IOError:
        f = open('contact_list.txt', 'w')
    user_list.extend(all_recipients)
    user_list = list(set(user_list))
    for i, s in enumerate(user_list):
        print((i + 1))
        print(s)
        print()
    chat_speak("Who do you want to connect to ?")
    choice = int(input('Who do you want to connect to (0 for new contact): '))
    for i, s in enumerate(user_list):
        if choice == (i + 1):
            target.append(s)
            found = 1
            sending(target)
        else:
            continue
    if choice ==0:
        #print('Could not find the corresponding email_id...!\n')
        chat_speak("Enter the complete email address of the recipient")
        new_email = input('Enter the complete email address of recipient: ')
        target.append(new_email)
        user_list.append(new_email)
        sending(target)
        with open('contact_list.txt', 'w') as f1:
            for s in user_list:
                f1.write(s + '\n')
            f1.close()
    try:
        mail_conn.close()  # Close currently selected folder (if any)
    finally:
        mail_conn.logout()
    f.close()
