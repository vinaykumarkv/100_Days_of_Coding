import requests
import sys
from datetime import datetime
sys.path.insert(1, '/Users/vinay/PycharmProjects')
import creds
app_ID = creds.app_ID
app_key = creds.app_Key
sheetly_endpoint_url = creds.sheetly_endpoint_url
sheetly_key = creds.sheetly_key
today = datetime.today().now()
formatted_date = today.strftime('%d/%m/%Y')
formatted_time = today.strftime('%H:%M')
# print(formatted_date, formatted_time)

headers = {
	"x-app-id": app_ID,
	"x-app-key": app_key,
	"x-remote-user-id": "0"
}
# query = "I Ran for 11 Kms today"
# weight = "95"
# height = "175"
# age = "35"
query = input("How was your workout today? : ")
weight = input("what is your weight? in KG : ")
height = input("what is your height? in Cms : ")
age = input("what is your Age? in Years : ")
json_query = {
	"query": query,
	"weight_kg": weight,
	"height_cm": height,
	"age": age,
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=json_query, headers=headers)
data = response.json()
for exercise in data["exercises"]:
	duration = exercise['duration_min']
	calories = exercise['nf_calories']
	name_exercise = exercise['name']
	# print(duration,calories,name_exercise, formatted_date, formatted_time)
	data_row = {
		"workout": {
			"date": formatted_date,
			"time": formatted_time,
			"exercise": name_exercise,
			"duration": duration,
			"calories": calories,
		}
	}
	response1 = requests.post(url=sheetly_endpoint_url, json=data_row)
	# print(response1.text)



