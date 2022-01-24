from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number_one = browser.find_element(By.ID, "num1")
    number_two = browser.find_element(By.ID, "num2")

    sum = str(int(number_one.text) + int(number_two.text))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    submit_button.click()


finally:
    time.sleep(10)
    browser.quit()
