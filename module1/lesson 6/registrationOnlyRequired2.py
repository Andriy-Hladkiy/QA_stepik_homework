from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "//Input[@placeholder='Input your first name']")
    first_name.send_keys("Hladkyi")
    last_name = browser.find_element(By.XPATH, "//Input[@placeholder='Input your last name']")
    last_name.send_keys("Andriy")
    email = browser.find_element(By.XPATH, "//Input[@placeholder='Input your email']")
    email.send_keys('test1@test.ua')

    submit_button = browser.find_element(By.XPATH, "//Button[@type='submit']")
    submit_button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text



finally:
    time.sleep(10)
    browser.quit()
