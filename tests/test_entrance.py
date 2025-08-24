import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestEntranceInStellarBurgers:
    def test_button_login_to_account(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Войти в аккаунт']"))).click() # дождаться видимости кнопки "Войти в аккаунт" и нажать на неё
        
        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexeev123@ya.ru') # найти и заполнить поле "Имя" валидными данными для входа
        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys('123467') # найти и заполнить поле "Пароль" валидными данными дял входа
        driver.find_element(By.XPATH, "html//form//button[text() = 'Войти']").click() # найти и нажать кнопку "Войти"
        
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//button[text() = 'Оформить заказ']"))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    def test_log_in_using_the_button_personal_account(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//a[@class = 'AppHeader_header__link__3D_hX' and @href = '/account']"))).click() # дождаться видимости кнопки "Личный кабинет" и нажать на неё
        
        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexeev123@ya.ru') # найти и заполнить поле "Имя" валидными данными для входа
        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys('123467') # найти и заполнить поле "Пароль" валидными данными дял входа
        driver.find_element(By.XPATH, "html//form//button[text() = 'Войти']").click() # найти и нажать кнопку "Войти"


        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//button[text() = 'Оформить заказ']"))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL
        
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
    

    def test_log_in_using_the_button_in_the_registration_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Войти в аккаунт']"))).click() # дождаться видимости кнопки "Войти в аккаунт" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//a[text() = 'Зарегистрироваться']"))).click() # дождаться видимости кнопки "Зарегистрироваться" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//a[text() = 'Войти']"))).click() # дождаться видимости кнопки "Войти" и нажать на неё

        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexeev123@ya.ru') # найти и заполнить поле "Имя" валидными данными для входа
        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys('123467') # найти и заполнить поле "Пароль" валидными данными дял входа
        driver.find_element(By.XPATH, "html//form//button[text() = 'Войти']").click() # найти и нажать кнопку "Войти"
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//button[text() = 'Оформить заказ']"))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()


    def test_login_using_the_button_in_the_password_recovery_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Войти в аккаунт']"))).click() # дождаться видимости кнопки "Войти в аккаунт" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//a[text() = 'Восстановить пароль']"))).click() # дождаться видимости кнопки "Восстановить пароль" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//a[text() = 'Войти']"))).click() # дождаться видимости кнопки "Войти" и нажать на неё

        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexeev123@ya.ru') # найти и заполнить поле "Имя" валидными данными для входа
        driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys('123467') # найти и заполнить поле "Пароль" валидными данными дял входа
        driver.find_element(By.XPATH, "html//form//button[text() = 'Войти']").click() # найти и нажать кнопку "Войти"
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//button[text() = 'Оформить заказ']"))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()