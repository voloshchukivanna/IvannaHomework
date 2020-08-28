from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()
dr.get("https://novaposhta.ua/")

dropdown = dr.find_element(By.XPATH, '//*[@id="top_menu"]/li[1]/a')
dropdown.click()
time.sleep(2)




