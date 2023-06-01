# Message for user to select using symbols

usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

#An Email Simulation

# Creating an empty list of emails

class Email:
    emails = []
    has_been_read = False # Set has_been_read to False

    is_spam = False # Set is_spam to False


# Create class email ____init____

    def __init__(self,from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents

# Define string method and attach each self. object      
      
    def __str__(self):

        return f"""
        
From Address : {self.from_address}
Subject      : {self.subject_line}
Email message : {self.email_contents}
Read Status   : {self.has_been_read}
Spam Status   : {self.is_spam}               
        
        """

# Create mark_as_read method
      
    def mark_as_read(self):
        
        self.has_been_read = True    


# Create mark_as_spam method

    def mark_as_spam(self):
        
        self.is_spam = True  

# Create output and call Email class

email1 = Email("louise.gmail.com", "Hello all the people in the world", "Working out OOP is complex")
print(email1)

email1.mark_as_read()
print(email1)


# Create Inbox Class

class Inbox:
    inbox = [] # creating an empty list of emails

    has_been_read = False # Set has_been_read to False

    is_spam = False # Set is_spam to False


# Create class Inbox ____init____

    def __init__(self,from_address, subject_line, email_contents, index):

        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        self.index = index


# Create add_email method

    def add_email(self):
        return "{} {} {}".format(self.from_address, self.subject_line, self.email_contents)
     

# Create list_messages_from_sender method

    def list_messages_from_sender(self, sender_address):
        self.sender_address = sender_address    


# Create string from_subject_line   
     
    def __str__(self):
        return f"""

        Number : {self.subject_line}
         
        """
        
# Create get_email method

    def get_email(self,sender_address, index):
        self.sender_address = sender_address 
        self.index = index
        self.has_been_read = True 

        
# Create mark_as_spam method

    def mark_as_spam(self,sender_address, index):
        self.sender_address = sender_address 
        self.index = index
        self.is_spam = True 


# Create method get_unread_emails and return string of Spam Emails

    def get_unread_emails(self):
        return f"""

        Unread : {self.has_been_read}
        Number : {self.subject_line}
         
        """

# Create method get_spam_emails and return string of Spam Emails

    def get_spam_emails(self):
        return f"""

        Spam Emails : {self.is_spam}
        Number : {self.subject_line}
         
        """
    

# Create method to delete email from Inbox

    def delete(self, sender_address, index):
        self.sender_address = sender_address 
        self.index = index   
    


user_choice = ""

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")

        # Now add the email to the Inbox
        Inbox.add_email()

        # Print a success message
        print("Email has been added to inbox.")

        pass
    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")

        # Now list all emails from this sender
        Inbox.list_messages_from_sender
        

        pass
    elif user_choice == "r":
        # Read an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        Inbox.list_messages_from_sender

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email that you would like to read\n:"))

        # Step 4: display the email
        Inbox.get_email

        pass
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        Inbox.list_messages_from_sender

        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be marked as spam\n:"))

        # Step 4: mark the email as spam
        Inbox.mark_as_spam

        # Step 5: print a success message
        print("Email has been marked as spam")

        pass
    elif user_choice == "gu":
        # List all unread emails
        pass
    elif user_choice == "gs":
        # List all spam emails
        pass
    elif user_choice == "e":
        print("Goodbye")
        break
    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)

        Inbox.list_messages_from_sender
        
        # Step 3: ask the user for the index of the email
        email_index = int(input("Please enter the index of the email to be deleted\n:"))

        # Step 4: delete the email
        Inbox.delete

        # Step 5: print a success message
        print("Email has been deleted")

        pass
    else:
        print("Oops - incorrect input")
