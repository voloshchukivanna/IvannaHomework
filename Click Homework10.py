from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tsf

dr = webdriver.Chrome()
# dr.implicitly_wait(5)
wait = WebDriverWait(dr, 5)
dr.get("http://google.com")

el = dr.find_element(By.NAME, "q")
el.send_keys("Python")
# el.send_keys(Keys.ENTER)
# time.sleep(5)

# button = dr.find_element(By.CLASS_NAME, 'gNO89b')
# button = dr.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
# print(button.text)

# button = wait.until(EC.element_to_be_clickable(By.NAME, 'btnK'))
button = wait.until(EC.element_to_be_clickable(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'))
print(button.text)
button.click()

# el.click()
# time.sleep(5)

links = wait.until(EC.presence_of_all_elements_located(By.PARTIAL_LINK_TEXT, "программирования"))
print(len(links))
for link in links:
    print(link.text)

# dr.quit()
# dr.close()








