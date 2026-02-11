from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def total(a, b):
    return str(int(a) + int(b))

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_num1 = browser.find_element(By.ID, 'num1')
    find_num2 = browser.find_element(By.ID, 'num2')
    num1 = find_num1.text
    num2 = find_num2.text
    s = total(num1, num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s) 

    find_buttom = browser.find_element(By.TAG_NAME, 'button')
    find_buttom.click()

finally:
    time.sleep(7)
    browser.quit()    