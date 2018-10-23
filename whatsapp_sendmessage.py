from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Tharkie"'

# Replace the below string with your own message
string = "I am sad!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()


message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

for i in range(1000):
	message.send_keys(string + Keys.ENTER)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()

driver.close()

