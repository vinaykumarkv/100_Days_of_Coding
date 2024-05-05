from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://secure-retreat-92358.herokuapp.com/")
firstname = driver.find_element(By.XPATH, value='/html/body/form/input[1]')
firstname.send_keys("Python")
lastname = driver.find_element(By.XPATH, value='/html/body/form/input[2]')
lastname.send_keys("K V")
emailaddress = driver.find_element(By.XPATH, value='/html/body/form/input[3]')
emailaddress.send_keys("sample@gmail.com")
signup = driver.find_element(By.XPATH, value='/html/body/form/button')
signup.click()

