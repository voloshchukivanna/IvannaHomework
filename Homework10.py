from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


'''Task1 Выбор из выпадающего мекню'''
dr = webdriver.Chrome()
dr.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")

dropdown = dr.find_element(By.TAG_NAME, 'select')
dropdown.click()
time.sleep(2)

dropdown.find_element(By.XPATH, './option[3]')
dropdown.click()
time.sleep(2)

# '''Task2 Выбор из выпадающего меню (Select)'''
# dr = webdriver.Chrome()
# dr.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
#
# select = Select(dr.find_element(By.ID, 'components'))
# time.sleep(2)
# select.select_by_value('Build config')
# time.sleep(2)
#
# '''Task3 Checkbox ?????? (не разобралась до конца)'''
# dr = webdriver.Chrome()
# dr.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
#
# checkboxes = dr.find_elements_by_xpath('//*[@id="radio2"]')
# for checkbox in checkboxes:
#     if checkbox.is_Selected():
#         checkbox.click()
#
# '''Task4 Action'''
# dr = webdriver.Chrome()
# actions = webdriver.ActionChains(dr)
# dr.get("https://novaposhta.ua/")
#
#
# dropdown = dr.find_element(By.XPATH, '//*[@id="top_menu"]/li[3]/a')
# sub_menu = dr.find_element(By.XPATH, '//*[@id="top_menu"]/li[3]/ul/li[3]/a')
#
# actions.move_to_element(dropdown).perform()
# actions.move_to_element(sub_menu).perform()
# actions.click(sub_menu)
# actions.perform()