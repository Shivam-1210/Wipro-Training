
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_basics.google_homepage_test import driver

'''driver = webdriver.Edge(service = Service("../resources/msedgedriver.exe"))

driver.get("https://www.google.com")

driver.implicitly_wait(5)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
googlesearch_button = driver.find_element(By.NAME, "btnK")
googlesearch_button.click()'''

wait = WebDriverWait(driver, 10)

search_box = wait.until(expected_conditions.visibility_of_element_located(By.NAME), "q"))

driver.quit()
