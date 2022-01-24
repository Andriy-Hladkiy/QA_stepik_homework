from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    book_button = browser.find_element(By.ID, "book")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    book_button.click()

    input_value = browser.find_element(By.ID, "input_value").text

    y = calc(input_value)

    answer = browser.find_element(By.ID, "answer")

    submit_button = browser.find_element(By.ID, "solve")

    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    answer.send_keys(y)
    submit_button.click()






finally:
    time.sleep(10)
    browser.quit()