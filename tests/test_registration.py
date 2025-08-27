import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *


class TestRegistrationStellarBurgers:
    def test_successful_registration(self, email_password, my_fixture):
        my_fixture.get("https://stellarburgers.nomoreparties.site/register")
        
        WebDriverWait(my_fixture, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, button_registration_in_form_registration))) # тест продолжит выполняться после загрузки кнопки "Зарегистрироваться"
         
        my_fixture.find_element(By.XPATH, name_in_registration_form).send_keys('Alexey') # найти и заполнить поле "Имя"
        my_fixture.find_element(By.XPATH, email_in_registration_form).send_keys(email_password[0]) # найти и заполнить поле "Email"
        my_fixture.find_element(By.XPATH, password_field).send_keys(email_password[1]) # найти и заполнить поле "Пароль"
        my_fixture.find_element(By.XPATH, button_registration_in_form_registration).click() # найти и нажать на кнопку "Зарегистрироваться"

        WebDriverWait(my_fixture, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login))) # после загрузки кнопки 'Вход' происходит сравнение URL 
        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/login'
        

    def test_with_incorrect_password(self, email_password, my_fixture):
        my_fixture.get("https://stellarburgers.nomoreparties.site/register")
            
        WebDriverWait(my_fixture, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, button_registration_in_form_registration))) # тест продолжит выполняться после загрузки кнопки "Зарегистрироваться"
            
        my_fixture.find_element(By.XPATH, name_in_registration_form).send_keys('Alexey') # найти и заполнить поле "Имя"
        my_fixture.find_element(By.XPATH, email_in_registration_form).send_keys(email_password[0]) # найти и заполнить поле "Email"
        my_fixture.find_element(By.XPATH, password_field).send_keys('123') # найти и заполнить поле "Пароль" невалидными данными
        my_fixture.find_element(By.XPATH, button_registration_in_form_registration).click() # найти и нажать на кнопку "Зарегистрироваться"

        WebDriverWait(my_fixture, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, text_of_the_error))) # найти и сравнить сообщение об ошибке с текстом "Некорректный пароль" с проверкой видимости элемента
        assert my_fixture.find_element(By.XPATH, text_of_the_error).text == 'Некорректный пароль'
        
