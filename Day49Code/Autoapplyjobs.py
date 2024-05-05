import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/")
login_name = driver.find_element(By.XPATH, value='//*[@id="session_key"]')
login_name.send_keys("email id here")
login_password = driver.find_element(By.XPATH, value='//*[@id="session_password"]')
login_password.send_keys("password here")
submit_cred = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
submit_cred.click()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3867474900&f_AL=true&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
searchbox = driver.find_element(By.XPATH, value='//*[@id="jobs-search-box-keyword-id-ember28"]')
searchbox.send_keys("Python Developer", Keys.ENTER)

driver.get("https://www.linkedin.com/jobs/view/3867474900/?alternateChannel=search&refId=jC2NUslid1Yq6GDfKbuLzg%3D%3D&trackingId=Bspan%2F8DtdMiQq%2BEMi0RhA%3D%3D")
time.sleep(5)
select_job = driver.find_element(By.CLASS_NAME, value='data-job-id="3899654724"')



select_job.click()
#URL keeps changing, too many challenges in this project. I will comback to this again to revise and resolve after completeing the course.


