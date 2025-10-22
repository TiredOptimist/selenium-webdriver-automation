from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    # Инициализация драйвера
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение полей с использованием найденных селекторов
    # value1 (By.TAG_NAME) = "input" - будет найден первый input
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    
    # value2 (By.NAME) = "last_name"
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    
    # value3 (By.CLASS_NAME) = "city"
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    
    # value4 (By.ID) = "country"
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Нажатие кнопки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код из всплывающего окна
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# не забываем оставить пустую строку в конце файла