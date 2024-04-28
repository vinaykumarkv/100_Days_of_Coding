import requests
import datetime as date
from data import stock_data
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='cad58f38ca4a45749e302c1dde4d55be')

servicePlanId = "24c7d4ef922d4dc08f38f7ba8ccd2a0e"
apiToken = "89aa6042a4f04be7b38ed368c8645309"
sinchNumber = "+447520652649"
toNumber = "+447424696464"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_SECRET = ""
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                          sources='bbc-news,the-verge',
                                          language='en')

today = date.datetime.now()
yesterday = today - date.timedelta(days=1)
daybeforeyesterday = today - date.timedelta(days=2)
TODAY = (str(today)).split(" ")[0]
YESTERDAY = (str(yesterday)).split(" ")[0]
DAYBEFOREYESTERDAY = (str(daybeforeyesterday)).split(" ")[0]
print(DAYBEFOREYESTERDAY)


def back_date():
	global today
	global yesterday
	global daybeforeyesterday
	global TODAY
	global YESTERDAY
	global DAYBEFOREYESTERDAY
	today = today - date.timedelta(days=1)
	yesterday = today - date.timedelta(days=1)
	daybeforeyesterday = today - date.timedelta(days=2)
	TODAY = (str(today)).split(" ")[0]
	YESTERDAY = (str(yesterday)).split(" ")[0]
	DAYBEFOREYESTERDAY = (str(daybeforeyesterday)).split(" ")[0]


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
#

# send sms program
def send_sms():
	region = "us"
	url = "https://" + region + ".sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

	payload = {
		"from": sinchNumber,
		"to": [
			toNumber
		],
		"body": f"{STOCK}{p}{round(percentage_changed)}\n{top_headlines}",
		"delivery_report": "none",
		"type": "mt_text"
		# this message can be modified by holding on the to the data and reformatting based on percentage
		# increase/decrease, I will again come back and reformat once I complete 100 days, during revision
	}
	headers = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {apiToken}"
	}
	smsresponse = requests.post(url, json=payload, headers=headers)
	smsdata = smsresponse.json()
	print(smsdata)


def arrow_check(percentage_changed):
	if percentage_changed > 0:
		return "🔺"
	else:
		return "🔻"


stock_response = requests.get(
	f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_SECRET}')
# faced limitation of data response to 25/day in api so sourcing data from file now.
counter = 5
while counter != 0:
	try:
		print("trying")
		yesterday_price = float(stock_data['Time Series (Daily)'][f'{YESTERDAY}']['4. close'])
		before_price = float(stock_data['Time Series (Daily)'][f'{DAYBEFOREYESTERDAY}']['4. close'])
		percentage_changed = ((yesterday_price - before_price) / yesterday_price) * 100
		counter -= 1
		counter = 0
		print(round(percentage_changed))
		if -1 >= round(percentage_changed) or round(percentage_changed) >= 1:
			p = arrow_check(percentage_changed)
			send_sms()
			print("sms sent!")
			counter = 0
	except:
		back_date()
		counter -= 1
		print("retrying")

#
#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds 
and prominent investors are required to file by the SEC The 13F filings show 
the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds 
and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, 
near the height of the coronavirus market crash.
"""
