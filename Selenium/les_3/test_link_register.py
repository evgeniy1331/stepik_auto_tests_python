import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegister(unittest.TestCase):
    def test_work_link(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input_first_name = browser.find_element(By.CLASS_NAME, "form-control.first")
        input_first_name.send_keys("Chelik")

        input_last_name = browser.find_element(By.CLASS_NAME, "form-control.second")
        input_last_name.send_keys("Krytoi")

        input_email = browser.find_element(By.XPATH, "//div[3]/input")
        input_email.send_keys("qwerty@mail.com")

        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Not register",
        )
        browser.quit()

    def test_not_work_link(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input_first_name = browser.find_element(By.CLASS_NAME, "form-control.first")
        input_first_name.send_keys("Chelik")

        input_last_name = browser.find_element(By.CLASS_NAME, "form-control.second")
        input_last_name.send_keys("Krytoi")

        input_email = browser.find_element(By.XPATH, "//div[3]/input")
        input_email.send_keys("qwerty@mail.com")

        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Not register",
        )
        browser.quit()

if __name__ == "__main__":
    unittest.main()
