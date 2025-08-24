import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestRegistrationStellarBurgers:
    def test_successful_registration(self, email_password):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Зарегистрироваться']"))) # тест продолжит выполняться после загрузки кнопки "Зарегистрироваться"
         
        driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexey') # найти и заполнить поле "Имя"
        driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys(email_password[0]) # найти и заполнить поле "Email"
        driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[2].send_keys(email_password[1]) # найти и заполнить поле "Пароль"
        driver.find_element(By.XPATH, "html//button[text() = 'Зарегистрироваться']").click() # найти и нажать на кнопку "Зарегистрироваться"

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//h2[text() = 'Вход']"))) # после загрузки кнопки 'Вход' происходит сравнение URL 
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_with_incorrect_password(self, email_password):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
            
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Зарегистрироваться']"))) # тест продолжит выполняться после загрузки кнопки "Зарегистрироваться"
            
        driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexey') # найти и заполнить поле "Имя"
        driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys(email_password[0]) # найти и заполнить поле "Email"
        driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[2].send_keys('123') # найти и заполнить поле "Пароль" невалидными данными
        driver.find_element(By.XPATH, "html//button[text() = 'Зарегистрироваться']").click() # найти и нажать на кнопку "Зарегистрироваться"

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//p[text() = 'Некорректный пароль']"))) # найти и сравнить сообщение об ошибке с текстом "Некорректный пароль" с проверкой видимости элемента
        assert driver.find_element(By.XPATH, "html//p[text() = 'Некорректный пароль']").text == 'Некорректный пароль'
        driver.quit()
