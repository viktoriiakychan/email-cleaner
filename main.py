from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from gmail_client import GmailClient
import analytics

gmail = GmailClient()

emails = gmail.get_emails(10)

# for email in emails:
#     print(email)

# sender_counts = analytics.get_sender_counts(emails)
# for sender, count in sender_counts.most_common():
#     print(sender, count)

# unread_count = analytics.get_unread_emails(emails)
# print("Unread count:", unread_count)

# newsletter_count = analytics.get_newsletter_count(emails)
# print("Newsletter count: ", newsletter_count)


while True:
    print("\n===== Menu =====")
    print("1. Show newsletter count")
    print("2. Mark emails as read")
    print("3. Archive emails")
    print("4. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        print("Showing newsletter count...")
        newsletter_count = analytics.get_newsletter_counts(emails)
        for sender, count in newsletter_count.most_common():
            print(sender, count)
        

    elif choice == "2":
        print("Marking emails as read...")
        unread_count = analytics.get_unread_emails(emails)
        print("Unread count:", unread_count)

        newsletter_ids = [e.id for e in emails if e.is_newsletter]
        gmail.mark_as_read(newsletter_ids[:10])

        emails = gmail.get_emails(10)

        unread_count = analytics.get_unread_emails(emails)
        print("Unread count:", unread_count)

    elif choice == "3":
        print("Archiving emails...")
        newsletter_ids = [e.id for e in emails if e.is_newsletter]
        gmail.archive(newsletter_ids[:2])   

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")