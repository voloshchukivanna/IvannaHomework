from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 5)
driver.get("https://dou.ua/")

# button = driver.find_element_by_name("q").send_keys('Python')
# button = driver.find_element(By.NAME, "q").send_keys('Python')
# button = driver.find_element_by_css_selector("#txtGlobalSearch").send_keys('Python')
# button = driver.find_element(By.CSS_SELECTOR, "#txtGlobalSearch").send_keys('Python')
# button = driver.find_element_by_id("txtGlobalSearch").send_keys('Python')
# button = driver.find_element(By.ID, "txtGlobalSearch").send_keys('Python')
# button = driver.find_element_by_xpath("//*[@id="txtGlobalSearch"]").send_keys('Python')
# button = driver.find_element(By.XPATH, "//*[@id="txtGlobalSearch"]").send_keys('Python')

# def is_button_present(value):
def is_button_present(by, value):
    try:
        # button = driver.find_element_by_name(value)
        button = driver.find_element(by, value)
        return button
        # print("Found element")
    except NoSuchElementException:
        return False
        # print("No element")

# search_button = is_button_present("q")
search_button = is_button_present(By.NAME, "q")
search_button.send_keys("Python")
time.sleep(5)
search_button.send_keys(Keys.ENTER)

# button = wait.until(EC.element_to_be_clickable(By.ID, )
# button.click()
# time.sleep(5)

links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Online")
print(len(links))

driver.quit()
driver.close()

