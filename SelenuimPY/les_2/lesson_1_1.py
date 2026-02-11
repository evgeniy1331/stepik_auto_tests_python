from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//div[1]/form/div/label/span[2]")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)

    find_check_box = browser.find_element(By.XPATH, '//div[2]/input[1]')
    find_check_box.click()

    find_radio_button = browser.find_element(By.ID, 'robotsRule')
    find_radio_button.click()

    find_button = browser.find_element(By.XPATH, '//button')
    find_button.click()
finally:
    time.sleep(5)
    browser.quit()
