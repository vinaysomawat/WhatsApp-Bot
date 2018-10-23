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


group_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.RLfQR")))

time.sleep(5)
for person in driver.find_elements_by_class_name('_2wP_Y'):
    title = person.find_element_by_xpath('div/div/div[2]/div[1]/div[1]/span').text
    #company = person.find_element_by_xpath('.//div[@class="company"]/a').text
    print(title)



