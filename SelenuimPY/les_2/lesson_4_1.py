from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return math.log(abs(12 * math.sin(int(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    find_button = browser.find_element(By.ID, 'book')
    find_button.click()

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