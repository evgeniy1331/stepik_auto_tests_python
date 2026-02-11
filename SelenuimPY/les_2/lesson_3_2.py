from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_button_1 = browser.find_element(By.XPATH, "//button")
    find_button_1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text    
    y = calc(x)

    find_input = browser.find_element(By.ID, "answer")
    find_input.send_keys(y)

    find_button_2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    find_button_2.click()
finally:
    time.sleep(7)
    browser.quit()