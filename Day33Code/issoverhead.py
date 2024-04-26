import time

import requests
import datetime
import smtplib
my_lat = 51 # my location
my_long = 0 #my location
MY_LAT = 0 #initiate ISS location
MY_LONG = 0 #initiate ISS location
sunrise = 0
sunset = 0
currenttime = 0
#get cordinates of ISS
def get_coordinates_of_ISS():
    global MY_LAT
    global MY_LONG
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    MY_LONG = (data['iss_position']['longitude'])
    MY_LAT = (data['iss_position']['latitude'])

get_coordinates_of_ISS()

#get sunrise and sunset
def get_sunrise_sunset():
    global sunset
    global sunrise
    global currenttime
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={my_lat}&lng={my_long}&formatted=0")
    response.raise_for_status()
    data = response.json()
    sunrise = int((((data['results']['sunrise']).split('T'))[1]).split(':')[0])
    print(sunrise)
    sunset = int((((data['results']['sunset']).split('T'))[1]).split(':')[0])
    print(sunset)
    now = datetime.datetime.now()
    currenttime = int(now.strftime("%H"))
    print(currenttime)

#send email if ISS is near me and its night
def check_status_of_ISS():
    get_coordinates_of_ISS()
    if ((my_lat-5) < (int(round(float(MY_LAT)))) < (my_lat+5)) & ((my_long-5) < (int(round(float(MY_LONG)))) < (my_long+5)) and (currenttime > sunset or currenttime < sunrise) :
        print("email sent")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="sample@gmail.com", password="password")
            connection.sendmail(from_addr="sample@gmail.com",
                                to_addrs="TO@gmail.com",
                                msg=f"Subject:Alert ISS is above you. loop UP  \n\n Congratulations!!,"
                                    f" you should look overhead to see the ISS.")
while True:
    get_coordinates_of_ISS()
    get_sunrise_sunset()
    check_status_of_ISS()
    print(f"{MY_LAT}, {MY_LONG}")
    time.sleep(60)





