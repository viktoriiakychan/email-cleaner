import email_reader
import menu

def main():
    while True:
        menu.show_menu()
        choice = input("Enter option [1-4]: ").strip()

        if choice == "1":
            print("You chose the option \"[1] - Read emails from the last N days\"\n")

            days = int(input("Enter number of days: "))
            uids = email_reader.get_emails_last_n_days(days)
            menu.loading_bar()
            email_reader.mark_emails_as_read(uids)
            #print("Emails found:", uids)

        elif choice == "2":
            days = int(input("Enter number of days: "))
            uids = email_reader.get_old_unread_emails(days)
            print("Emails found:", uids)

        elif choice == "3":
            sender = input("Enter sender email: ")
            email_reader.delete_by_sender(sender)

        elif choice == "4":
            print("Exiting Email Cleaner. Goodbye")
            break

        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()