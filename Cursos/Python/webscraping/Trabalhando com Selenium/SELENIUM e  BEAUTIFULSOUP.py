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

browser.get('https://www.airbnb.com.br')

sleep(3)

button = browser.find_element(By.XPATH, '//*[@id="site-content"]/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div/div/div[1]/button')

sleep(3)

button.click()

sleep(3)

input_place = browser.find_element(By.XPATH, '//*[@id="/homes-1-input"]')
input_place.send_keys('São Paulo')
input_place.submit()

sleep(60)

adthrjaed
