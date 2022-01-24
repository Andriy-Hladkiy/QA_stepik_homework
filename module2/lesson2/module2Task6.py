from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Andrii")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Hladkyi")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test1@test.com")

    file_input = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    file_input.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    submit_button.click()


finally:
    time.sleep(15)
    browser.quit()
