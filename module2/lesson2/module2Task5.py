from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element(By.ID, "input_value").text

    y = calc(value)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_radio_button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio_button)
    robot_radio_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type = submit]")
    submit_button.click()



finally:
    time.sleep(5)
    browser.quit()
