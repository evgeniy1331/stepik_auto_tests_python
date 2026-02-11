import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_input_name = browser.find_element(
        By.CSS_SELECTOR, 'input[placeholder="Enter first name"]'
    )
    find_input_name.send_keys("Yana")

    find_input_lastname = browser.find_element(
        By.CSS_SELECTOR, 'input[placeholder="Enter last name"]'
    )
    find_input_lastname.send_keys("Lox")

    find_email = browser.find_element(
        By.CSS_SELECTOR, 'input[placeholder="Enter email"]'
    )
    find_email.send_keys("qwerty123@mail.ru")

    find_select_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "text.txt")
    find_select_file.send_keys(file_path)

    find_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    find_button.click()
finally:
    time.sleep(7)
    browser.quit()
