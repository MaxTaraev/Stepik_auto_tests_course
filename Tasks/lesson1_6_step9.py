from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

if __name__ == '__main__':

    link = "http://suninjuly.github.io/registration1.html"
   
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        input1.send_keys('TEXT')

        input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        input2.send_keys('TEXT TEXT')

        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
        input3.send_keys('TEXT TEXT TEXT')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
