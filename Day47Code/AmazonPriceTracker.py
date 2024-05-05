from smtplib import SMTP_SSL

import requests
from bs4 import BeautifulSoup
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# from googleapiclient.discovery import build
# import base64
# from email.mime.text import MIMEText
# from requests import HTTPError

# from google_auth_oauthlib.flow import InstalledAppFlow

sys.path.insert(1, '/Users/vinay/PycharmProjects')
import creds

user_name = creds.gmailuser
password = creds.gmailpassword
fromemail = creds.fromuseremail
toemail = creds.touseremail

price_to_set = 95
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
prices = soup.find_all(name="span", class_="a-price-whole")
price_list = [a.getText() for a in prices]
price = price_list[1].replace(".", "")
price = int(price)
print(price)

message = MIMEMultipart()
message['From'] = fromemail
message['To'] = toemail
message['Subject'] = 'Amazon Price Alert!!'

# The content of your email
email_content = f"""\
The price has dropped below the {price_to_set} Pounds and is {price} Pounds.\n
 goto: https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1 to buy your product."""

# Attach the email content to the message
message.attach(MIMEText(email_content, 'plain'))


def check_status_of_price():
    if price <= price_to_set:
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
            connection.login(user_name, password)
            connection.sendmail(fromemail, toemail, message.as_string())
            print("email sent")


check_status_of_price()
