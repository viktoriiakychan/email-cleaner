from collections import Counter

def get_unread_emails(emails):
    count = 0

    for email in emails:
        if email.unread:
            count += 1

    return count

def get_sender_counts(emails):
    counter = Counter()

    for email in emails:
        counter[email.sender_email] += 1
    
    return counter

def get_newsletter_count(emails):

    count = 0

    for email in emails:
        if email.is_newsletter:
            count += 1

    return count