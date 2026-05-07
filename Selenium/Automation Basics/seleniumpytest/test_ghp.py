
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check




@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google', 'Google Home Page Not Loaded'

def test_imagespageload(driver):
    from selenium.webdriver.common.by import By
    driver.find_element(By.LINK_TEXT, 'Images').click()
    pagetitle = driver.title
    assert pagetitle =='Google Images', 'Images Page Not Loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT, 'Business').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains('Business'))
    #assert 'Business' in driver.title, 'Business Page Not Loaded - title Check'
    #assert 'business' in  driver.current_url, 'Business Page Not Loaded - URL Check'
    check.is_in( 'Business', driver.title,'Business Page Not Loaded - title Check')
    check.is_in("business", driver.current_url, 'Business Page Not Loaded - URL Check' )