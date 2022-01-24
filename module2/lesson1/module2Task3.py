from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_id = browser.find_element(By.ID, "treasure")
    atribute = x_id.get_attribute("valuex")
    #print(atribute)
    y = calc(atribute)
    input_element = browser.find_element(By.ID, "answer")
    input_element.send_keys(y)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()
