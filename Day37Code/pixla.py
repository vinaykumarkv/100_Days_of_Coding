import requests
from datetime import datetime
today = datetime.today().date()
formatted_date = today.strftime('%Y%m%d')
# formatted_date = "20240427"
username = ""
token = ""
graph_id = "graph1"
#Endpoint URL
endpoint = "https://pixe.la/v1/users"
#
#
# user_params = {
# 	"token": token,
# 	"username": username,
# 	"agreeTermsOfService": "yes",
# 	"notMinor": "yes",
# }
# response = requests.post(url=endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{endpoint}/{username}/graphs"
# graph_config = {
# 	"id": graph_id,
# 	"name": "running",
# 	"unit": "Km",
# 	"type": "float",
# 	"color": "ajisai",
# }
headers = {
	"X-USER-TOKEN": token,

}
# response1 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response1.text)
kms = "25"
graph1_endpoint = f"{graph_endpoint}/{graph_id}"
graph1_update = {
	"date": formatted_date,
	"quantity": kms,
}
update_endpoint = f"{graph1_endpoint}/{formatted_date}"
graph_prop = {
	"quantity": "30",
}
# response = requests.post(url=graph1_endpoint, json=graph1_update, headers=headers)
# response = requests.put(url=update_endpoint, json=graph_prop, headers=headers)
response = requests.delete(url=update_endpoint, json=graph_prop, headers=headers)
print(response.text)
