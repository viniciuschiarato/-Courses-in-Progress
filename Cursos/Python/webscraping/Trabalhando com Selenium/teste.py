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

browser.get('https://www.google.com.br/')

input_place = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_place.clear()
input_place.send_keys('feel good')
input_place.submit()

sleep(30)


