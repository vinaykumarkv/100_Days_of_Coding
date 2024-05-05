from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
event_details = events.text
temp_list = event_details.split("\n")
date_list =[]
event_name_list = []
dicts = {}
for i in range(len(temp_list)):
	if i%2 ==0:
		date_list.append(temp_list[i])
	else:
		event_name_list.append((temp_list[i]))
#instead of above code we can also use findelements function to get tags based on CSS selector
dicts ={i:{date_list[i] : event_name_list[i]} for i in range(len(date_list))}
print(dicts)
driver.quit()