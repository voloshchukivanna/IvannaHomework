from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

'''мне нужно ввести свой email - нажать Next, потом ввести пароль - нажать Sign in'''
'''если корректно залогинилась, то должна прийти телефонная верификация на мобильный: как это сделать?'''

driver = webdriver.Chrome()
driver.get("https://web.yammer.com/main/feed")

# email = driver.find_element(By.NAME, "loginfmt").send_keys("********")
# button_next = driver.find_element(By.ID, "idSIButton9")
# password = driver.find_element(By.NAME, "passwd").send_keys("********")
# button_sign_in = driver.find_element(By.ID, "idSIButton9")
#
# button_next.click()
# button_sign_in.click()



def is_button_present(by, value):
    try:
        button = driver.find_element(by, value)
        return button
    except NoSuchElementException:
        return False

email = is_button_present(By.NAME, "loginfmt")
email.send_keys("********")
button_next = is_button_present(By.ID, "idSIButton9")
button_next.click()
password = is_button_present(By.NAME, "passwd")
password.send_keys("********")
button_sign_in = is_button_present(By.ID, "idSIButton9")
button_sign_in.click()

driver.quit()
driver.close()

