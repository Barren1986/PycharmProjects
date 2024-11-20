# This program is used to automate the process of unsubscribing from unwanted emails.
# Steps to be followed:
# 1. Open the email account. How do we connect to gmail via this program?
# 2. Search for the emails from the sender you want to unsubscribe. How do we read through email?
# 3. Click on the unsubscribe link. How do we find unsubscribe link? And how do we unsubscribe?
# 4. Confirm the subscription.
# 5. Close the browser.

# Imports\
from dotenv import load_dotenv
import imaplib
import email
import os
from bs4 import BeautifulSoup
load_dotenv()

username = os.getenv('EMAIL')
password = os.getenv("PASSWORD")

# Open the email account
def connect_to_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")
    return mail

def extract_link_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = [link["href"] for link in soup.find_all("a", hred = True) if "unsubscribe" in link.text.lower()]
    return links

def search_for_emails():
    mail = connect_to_mail()
    _, search_data = mail.search(None, '(BODY "unsubscribe")')
    data = search_data[0].split()

    links = []

    for num in data:
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    html_context = part.get_payload(decode=True).decode()
                    print(html_context)
        else:
            content_type = msg.get_content_type()
            content = msg.get_payload(decode=True).decode()

            if content_type == "text/html":
                print(content)

    mail.logout()

search_for_emails()


