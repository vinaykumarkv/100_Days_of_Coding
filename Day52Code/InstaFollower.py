from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

sys.path.insert(1, '/Users/vinay/PycharmProjects')
import creds

instagram_username = creds.instagram_username
instagram_password = creds.instagram_password


class instaFollower:
	def __init__(self, searchname):
		self.account_name = None
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(options=self.chrome_options)
		self.driver.get("https://www.instagram.com/")
		self.login()
		self.find_followers(searchname)
		self.follow()
		# self.driver.quit()

	def login(self):
		time.sleep(5)
		accept_cookies = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
		accept_cookies.click()
		time.sleep(2)
		username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
		username.send_keys(instagram_username)
		password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
		password.send_keys(instagram_password)
		login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
		login_button.click()
		time.sleep(5)

	def find_followers(self, search_name):
		time.sleep(5)
		search_button = self.driver.find_element(By.XPATH,
		                                         '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div')
		search_button.click()
		time.sleep(2)
		search_box = self.driver.find_element(By.XPATH,
		                                      '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
		search_box.send_keys(search_name, Keys.ENTER)
		time.sleep(2)
		first_search_option = self.driver.find_element(By.XPATH,
		                                               '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div')
		first_search_option.click()
		time.sleep(5)
		account = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div/a/h2')
		self.account_name = account.text
		print(self.account_name)

	def follow(self):

		self.driver.get(f"https://www.instagram.com/{self.account_name}/followers/")
		time.sleep(5)
		#Instagram has 50 followers limit to be seen for any celebrity so I have set limit of 50 to follow
		for i in range(1, 50, 1):
			try:
				follow_button = self.driver.find_element(By.XPATH,
				                                         f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[3]/div/button/div/div')
				follow_button.click()
			except:
				cancel_unfollow = self.driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
				cancel_unfollow.click()

			print(i)
			time.sleep(3)

		time.sleep(10)

#add any name of your interest
instaFollower("vidya balan")


