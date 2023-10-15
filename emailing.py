import constants
import imghdr
import os
import smtplib, ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

host = "smtp.gmail.com"
port = 465
username = "connord79@gmail.com"
password = constants.password
From = "connord79@gmail.com"
receiver = "connord79@gmail.com"


def sendemail(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected"
    email_message.set_content("There has been some motion detected")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    sendemail(image_path="images/6.png")


