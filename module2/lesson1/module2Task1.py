from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input_element = browser.find_element(By.ID, "answer")
    input_element.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    submit_button.click()



finally:

    time.sleep(20)
    browser.quit()