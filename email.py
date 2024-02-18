### --- OOP Email Simulator --- ###

pattern = "-" * 50

# --- Email Class --- #
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  

    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
inbox = []  

# --- Functions --- #
def populate_inbox():
    email1 = Email("sender1@example.com", "Subject 1", "Hello, this is the first email.")
    inbox.append(email1)

    email2 = Email("sender2@example.com", "Subject 2", "Hello, this is the second email.")
    inbox.append(email2)

    email3 = Email("sender3@example.com", "Subject 3", "Hello, this is the third email.")
    inbox.append(email3)

def list_emails():
    for index, email in enumerate(inbox):
        print(f"\n{index + 1}. {email.subject_line} - {'Read' if email.has_been_read else 'Unread'}")

def read_email(index):
    if 1 <= index <= len(inbox):
        email = inbox[index - 1]
        print(f"\n{pattern}\n\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print("Content:")
        print(email.email_content)
        email.mark_as_read()
        print("\n*Email marked as read*")
    else:
        print("Invalid email index.")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
while True:
    print(f"\n{pattern}\n\nInbox: {len(inbox)}")
    user_choice = int(input('''\nPlease select from the following options: \n
    1. Read an email 
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        index = int(input("\nEnter the number of the email you want to read: "))
        read_email(index)

    elif user_choice == 2:
        list_emails()

    elif user_choice == 3:
        print("\nExiting the application")
        break

    else:
        print("\nOops - incorrect input.")