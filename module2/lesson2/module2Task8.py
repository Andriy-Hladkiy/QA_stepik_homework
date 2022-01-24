from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    troll_submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    troll_submit_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = browser.find_element(By.ID, "input_value").text

    y = calc(value)

    form_control = browser.find_element(By.ID, "answer")
    form_control.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()



finally:
    time.sleep(10)
    browser.quit()