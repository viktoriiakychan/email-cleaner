from imap_tools import MailBox, AND, MailMessageFlags
from dotenv import load_dotenv
from datetime import datetime, timedelta

import os

load_dotenv() # loads .env

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
imap_server = os.getenv("IMAP_SERVER")


def get_old_unread_emails(days=30):
    date_limit = (datetime.now() - timedelta(days=days)).date()
    with MailBox(imap_server).login(email, password) as mailbox:
        emails = mailbox.fetch(AND(seen = False, date_lt= date_limit), limit = 10, reverse=True)
        # for e in emails:
        #     print(e.subject)
        return [msg.uid for msg in emails] # returns the id of the emails

def mark_emails_as_read(uids):
    with MailBox(imap_server).login(email, password) as mailbox:
        mailbox.flag(uids, MailMessageFlags.SEEN, True) # mark the unread messages read

def read_unread_emails(days):
    uids = get_old_unread_emails(days)
    mark_emails_as_read(uids)