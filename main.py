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
    print("4. Delete emails")
    print("5. Clean up by sender")
    print("0. Exit")

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
        print("Deleting emails...")
        
        to_trash = [e for e in emails if e.is_newsletter][:10]

        if not to_trash:
            print("No newsletters to trash.")
        else:
            print(f"\nThe following {len(to_trash)} emails will be moved to Trash:")
            for e in to_trash:
                print(f"  - {e.sender_name}: {e.subject}")

            # confirmation
            confirm = input("\nTrash these? Type 'yes' to confirm: ")

            if confirm.lower() == "yes":
                ids = [e.id for e in to_trash]
                gmail.trash(ids)
                emails = gmail.get_emails(10)
            else:
                print("Cancelled. Nothing was trashed.")

    elif choice == "5":
        sender_counts = analytics.get_sender_counts(emails)

        # print the senders and the number of emails from them in descending order
        print()
        sender_num = 1
        for sender, count in sender_counts.most_common():
            print(f"{sender_num}. {sender}: {count}")
            sender_num+=1

        raw = input("Enter the number of sender you want to work with: ")

        if not raw.isdigit():
            print("That's not a number. Try again.")
            continue   

        num = int(raw)

        if num < 1 or num > len(senders):
            print("That number isn't in the list. Try again.")
            continue

        curr_sender = sender_counts.most_common()[num-1]
        curr_sender_email = sender_counts.most_common()[num-1][0]
        print("\nWorking with", curr_sender[0])

        print("Select what you would like to do with the emails from this sender:\n")
        print("1. Read")
        print("2. Archive")
        print("3. Trash")
        print("4. Back")

        raw_action = input("\nChoose an action: ")

        if raw_action not in ("1", "2", "3", "4"):
            print("Invalid action. Try again.")
            continue

        if raw_action == "4":
            continue   

        action = int(raw_action)

        curr_sender_emails = [e for e in emails if e.sender_email == curr_sender_email]

        if action == 1:
            ids = [e.id for e in curr_sender_emails]
            gmail.mark_as_read(ids)
            emails = gmail.get_emails(10)

        elif action == 2:
            ids = [e.id for e in curr_sender_emails]
            gmail.archive(ids)
            emails = gmail.get_emails(10)

        elif action == 3:
            to_trash = [e for e in curr_sender_emails]

            if not to_trash:
                print("No newsletters to trash.")
            else:
                print(f"\nThe following {len(to_trash)} emails will be moved to Trash:")
                for e in to_trash:
                    print(f"  - {e.sender_name}: {e.subject}")

                # confirmation
                confirm = input("\nTrash these? Type 'yes' to confirm: ")

                if confirm.lower() == "yes":
                    ids = [e.id for e in to_trash]
                    gmail.trash(ids)
                    emails = gmail.get_emails(10)
                else:
                    print("Cancelled. Nothing was trashed.")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")