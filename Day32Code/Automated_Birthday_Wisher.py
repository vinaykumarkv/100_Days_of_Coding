##################### Extra Hard Starting Project ######################
import random
import smtplib
mymail = "sample0@gmail.com"
password = "password"

from datetime import datetime as dt
today = dt.now()
today_tuple = (today.month, today.day)


# 1. Update the birthdays.csv
import pandas

DOB_data_frame = pandas.read_csv("birthdays.csv")
DOB_dict = {(row.month, row.day): row for index, row in DOB_data_frame.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in DOB_dict:
    birthday_person = DOB_dict[today_tuple]
    file_path =f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path,'r') as datafile:
        contents = datafile.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        tomailname = birthday_person["name"]
        connection.starttls()
        connection.login(user=mymail, password=password)
        connection.sendmail(from_addr=mymail,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday {tomailname}  \n\n {contents}")






