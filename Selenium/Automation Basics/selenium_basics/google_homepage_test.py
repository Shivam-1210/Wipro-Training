from time import sleep

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#browser  = input('What browser do you want to use? ')

'''match (browser.lower()):
    case 'chrome':
        driver =  webdriver.Chrome(service = Service('../resource/chromedriver.exe'))

    case ('edge'):
        driver = webdriver.Edge(service=Service('../resource/msedgedriver.exe'))

    case _:
        print('Unknown browser - Not available. \n Executing with default edge browser.')
        driver = webdriver.Edge(service=Service('../resource/msedgedriver.exe'))'''






driver = webdriver.Edge() #(service = Service('../resource/msedgedriver.exe'))   #service = Service(EdgeChromiumDriverManager().install()))

driver.get("https://www.google.com")





pagetitle = driver.title

if pagetitle == 'Google':
    print("Google Homepage Loaded  -  Pass")
else:
    print("Google Homepage Loaded  -  Fail")

sleep(3)

driver.quit()


