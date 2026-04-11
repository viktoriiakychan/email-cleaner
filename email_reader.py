from imap_tools import MailBox, AND, MailMessageFlags
from dotenv import load_dotenv
from datetime import datetime, timedelta

import os

load_dotenv() # loads .env

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
imap_server = os.getenv("IMAP_SERVER")


def get_unread_olderThan_n_emails(days=30):
    date_limit = (datetime.now() - timedelta(days=days)).date()
    with MailBox(imap_server).login(email, password) as mailbox:
        #emails = mailbox.fetch(AND(seen = False, date_lt = date_limit), limit = 10, reverse=True, bulk=True) # emails whose date is before this date
        # for e in emails:
        #     print(e.subject)
        uids = mailbox.uids(AND(date_lt=date_limit, seen = False))
        return uids
        #return [msg.uid for msg in emails] # returns the id of the emails

def get_emails_last_n_days(days=30):
    date_limit = (datetime.now() - timedelta(days=days)).date()

    with MailBox(imap_server).login(email, password) as mailbox:
        uids = mailbox.uids(AND(date_gte=date_limit, seen = False))
        #return [msg.uid for msg in emails]
        return uids

def mark_emails_as_read(uids):
    with MailBox(imap_server).login(email, password) as mailbox:
        mailbox.flag(uids, MailMessageFlags.SEEN, True) # mark the unread messages read

def read_unread_emails(days):
    uids = get_old_unread_emails(days)
    mark_emails_as_read(uids)