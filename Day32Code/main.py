import smtplib
import random
import datetime as dt
mymail = ""
password = ""
toemail = ""
# --------------------------------------------------------read file---------------------

with open("quotes.txt",'r') as datafile:
    list_of_quotes = datafile.readlines()

# ---------------------Mailing code----------------------------
def send_email():

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=mymail, password=password)
        connection.sendmail(from_addr=mymail,
                            to_addrs=toemail,
                            msg=f"Subject:{days[today]} Motivation \n\n {random.choice(list_of_quotes)}")



#--------------------------------Date and time --------------------------------------

now = dt.datetime.now()
today = now.weekday()
print(today)
days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
date_of_birth = dt.datetime(year=1991, month=4, day=30, hour=12)
print(date_of_birth)



# send email
if today == 0:
    send_email()






