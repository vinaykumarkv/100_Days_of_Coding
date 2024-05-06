from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

google_form = "https://forms.gle/aAWPyqijF7bx2wFW7"
zillow_link = "https://appbrewery.github.io/Zillow-Clone/"


#get values for required feilds
response = requests.get(zillow_link)
zillow_data = response.text
soup = BeautifulSoup(zillow_data, "html.parser")
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
addresses = soup.find_all(name="address")
links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
link=[]
for i in links:
	link.append(i['href'])
length_of_values = len(prices)
print("got all values")
#fill the form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(google_form)
time.sleep(3)
for i in range(length_of_values):
	address_of_property = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
	address_of_property.send_keys((addresses[i].text).replace("                                  ",""))
	price_of_property = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
	price_of_property.send_keys(prices[i].text)
	link_of_property = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
	link_of_property.send_keys(link[i])
	submit_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
	submit_button.click()
	time.sleep(2)
	submit_another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
	submit_another_response.click()
	time.sleep(2)
print("All job done!")
driver.quit()
