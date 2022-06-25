from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


browser = webdriver.Chrome()  # método

browser.get('https://www.google.com.br/')

sleep(2)

browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
    'tears for fears everybody wants to rule the world')

browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
    Keys.ENTER)


