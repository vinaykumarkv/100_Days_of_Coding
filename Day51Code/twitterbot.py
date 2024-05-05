from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

sys.path.insert(1, '/Users/vinay/PycharmProjects')
import creds

twitter_username = creds.twiter_username
twitter_password = creds.twitter_pass
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.speedtest.net/")
time.sleep(2)
accept_cookies = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]')
accept_cookies.click()
time.sleep(2)
speed_test = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
speed_test.click()
time.sleep(60)
close_pop = driver.find_element(By.XPATH,
                                '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
close_pop.click()
time.sleep(2)
download_speed = driver.find_element(By.XPATH,
                                     '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download = download_speed.text
upload_speed = driver.find_element(By.XPATH,
                                   '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload = upload_speed.text

driver.get("https://twitter.com/i/flow/login")
time.sleep(5)
user_name = driver.find_element(By.XPATH,
                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
user_name.send_keys(twitter_username, Keys.ENTER)
time.sleep(3)
password = driver.find_element(By.XPATH,
                               '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys(twitter_password, Keys.ENTER)
time.sleep(4)
twitter_post = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
twitter_post.send_keys(
	f"Dear Internet Provider, please help in bettering my Internet connection, my current internet speed is {download}/{upload}")
post_button = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
post_button.click()

time.sleep(5)
driver.quit()
