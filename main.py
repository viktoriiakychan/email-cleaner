from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from gmail_client import GmailClient
import analytics

gmail = GmailClient()

emails = gmail.get_emails(100)

# for email in emails:
#     print(email)

sender_counts = analytics.get_sender_counts(emails)
for sender, count in sender_counts.most_common():
    print(sender, count)

unread_count = analytics.get_unread_emails(emails)
print("Unread count:", unread_count)

newsletter_count = analytics.get_newsletter_count(emails)
print("Newsletter count: ", newsletter_count)