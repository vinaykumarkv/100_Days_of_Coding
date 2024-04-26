import requests
import datetime
MY_LAT = 0
MY_LONG = 0
PLACE_NAME = ""
API_KEY = "662c2b2409cb8978799087akme44644"
FORMAT = "json"
def get_coordinates_of_ISS():
    global MY_LAT
    global MY_LONG
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    MY_LONG = (data['iss_position']['longitude'])
    MY_LAT = (data['iss_position']['latitude'])
def get_location_name():
    global PLACE_NAME
    response = requests.get(f"https://geocode.maps.co/reverse?lat={MY_LAT}&lon={MY_LONG}&format={FORMAT}&api_key={API_KEY}")
    response.raise_for_status()
    data = response.json()
    try:
        PLACE_NAME = (data['display_name'])
    except:
        PLACE_NAME = "Not Found"

get_coordinates_of_ISS()
get_location_name()
response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}&formatted=0")
response.raise_for_status()
data = response.json()
sunrise = ((((data['results']['sunrise']).split('T'))[1]).split(':')[0])
sunset = ((((data['results']['sunset']).split('T'))[1]).split(':')[0])
print(f"sunrise is {sunrise}Hrs UTC & sunset is {sunset}Hrs UTC for Lat {MY_LAT} and Long {MY_LONG} and location name is: {PLACE_NAME}")
