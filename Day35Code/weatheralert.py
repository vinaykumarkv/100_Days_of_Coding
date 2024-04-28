import requests

servicePlanId = ""
apiToken = ""
sinchNumber = ""
toNumber = ""

APIKEY = ""
LAT = 51.47
LONG = 0.36
CNT = 4


# SMS code downloaded from website

def send_sms():
    region = "us"
    url = "https://" + region + ".sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

    payload = {
        "from": sinchNumber,
        "to": [
            toNumber
        ],
        "body": "Programmers are tools for converting caffeine into code. We just got a new shipment of mugs!"
                " Check them out: https://tinyurl.com/4a6fxce7!",
        "delivery_report": "none",
        "type": "mt_text"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {apiToken}"
    }
    smsresponse = requests.post(url, json=payload, headers=headers)
    smsdata = smsresponse.json()
    print(smsdata)


response = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&cnt={CNT}&appid={APIKEY}")
response.raise_for_status()
data = response.json()
will_rain = False
for i in range(len(data['list'])):
    if data['list'][i]['weather'][0]['id'] < 700:
        will_rain = True
    else:
        continue
if will_rain:
    print("Rain")
    send_sms()
