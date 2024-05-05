from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
time.sleep(2)
login = driver.find_element(By.XPATH, value='//*[@id="q-856107901"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(2)
glogin = driver.find_element(By.XPATH, value='//*[@id="q1710478319"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
glogin.click()
time.sleep(2)
new_window = driver.window_handles[-1]
driver.switch_to.window(new_window)
try:
	allow_cookies = driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span')
except:
	allow_cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]')
allow_cookies.click()
username = driver.find_element(By.XPATH, value='//*[@id="email"]')
username.send_keys("")

password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password.send_keys("", Keys.ENTER)

time.sleep(2)
continue_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span')
continue_button.click()

mobilenumber = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/input')
mobilenumber.send_keys("", Keys.ENTER)


# Unfortunately Tinder is not allowing bots, I would have to stop my scripting here. but I am confident I can complete the remaining script since I just need to search for elements for direction and create delayed loops and condition to swipe left and right.


