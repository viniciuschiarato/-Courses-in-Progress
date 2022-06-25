import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=400,800')

browser = webdriver.Chrome(options=options)

browser.get('https://www.youtube.com/')

sleep(2)

input_place = browser.find_element(By.XPATH,'//*[@id="search"]')

input_place.send_keys('feel good')

input_place.submit()








# site = BeautifulSoup(browser.page_source, "html.parser")

# print(site.prettify())

# sleep(30)
