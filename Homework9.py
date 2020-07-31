from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
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
search_button.click() # у меня почему-то в строке поиске пишет Python, но не кликает

links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Online")
print(len(links)) #из-за того, что не кликает с строки 33, то неправильно считает количество "Online"

# driver.quit()
# driver.close()

