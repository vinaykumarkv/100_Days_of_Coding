import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')





# cursor_bought = False
# grandma_bought = False
# factory_bought = False
# mine_bought = False
# shipment_bought = False
# alchemy_bought = False
# portal_bought = False
# timemachine_bought = False


def fivesec_clicker():
	start_time = time.time()
	while (time.time() - start_time) < 5:
		cookie.click()


def check_highest_button():
	# global cursor_bought
	# global grandma_bought
	# global factory_bought
	# global mine_bought
	# global shipment_bought
	# global alchemy_bought
	# global portal_bought
	# global timemachine_bought
	cookies = driver.find_element(By.XPATH, value='//*[@id="money"]')
	cookie = int(cookies.text.replace(",", ""))
	print(cookies.text)
	if (100 > cookie > 15):
		buycursor = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]')
		buycursor.click()
		# cursor_bought = True
	elif (500 > cookie > 100):
		buygrandma = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]')
		buygrandma.click()
		# grandma_bought = True
	elif (2000 > cookie > 500):
		buyfactory = driver.find_element(By.XPATH, value='//*[@id="buyFactory"]')
		buyfactory.click()
		# factory_bought = True
	elif (7000 > cookie > 2000):
		buymine = driver.find_element(By.XPATH, value='//*[@id="buyMine"]')
		buymine.click()
		# mine_bought = True
	elif (50000 > cookie > 7000):
		buyshipment = driver.find_element(By.XPATH, value='//*[@id="buyShipment"]')
		buyshipment.click()
		# shipment_bought = True
	elif (100000 > cookie > 50000):
		buyalchemylab = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]')
		buyalchemylab.click()
		# alchemy_bought = True
	elif (123456789 > cookie > 100000):
		buyportal = driver.find_element(By.XPATH, value='//*[@id="buyPortal"]')
		buyportal.click()
		# portal_bought = True
	elif cookie > 123456789:
		buytimemachine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]')
		buytimemachine.click()
		# timemachine_bought = True

start_game_time = time.time()

while (time.time() - start_game_time) < 300:
	fivesec_clicker()
	check_highest_button()
cookies = driver.find_element(By.XPATH, value='//*[@id="money"]')
cookie = int(cookies.text.replace(",", ""))
print(cookie)

driver.quit()
