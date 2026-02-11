from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))
    

link = 'https://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_x = browser.find_element(By.ID, 'input_value')
    x = find_x.text
    y = calc(x)
    
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)

    find_button = browser.find_element(By.XPATH, '//button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", find_button)

    find_check_box = browser.find_element(By.XPATH, '//div[2]/input[1]')
    find_check_box.click()

    find_radio_button = browser.find_element(By.ID, 'robotsRule')
    find_radio_button.click()


    find_button.click()

finally:
    time.sleep(7)
    browser.quit()