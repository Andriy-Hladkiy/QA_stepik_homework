from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    i_want_button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    i_want_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value = browser.find_element(By.ID, "input_value").text

    y = calc(value)

    form_control = browser.find_element(By.ID, "answer")
    form_control.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
    



finally:
    time.sleep(10)
    browser.quit()
