import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from locators import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
class TestEntranceInStellarBurgers:
    def test_button_login_to_account(self, my_fixture):
        my_fixture.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, login_account))).click() # дождаться видимости кнопки "Войти в аккаунт" и нажать на неё
        
        my_fixture.find_element(By.XPATH, email_log).send_keys(email) # найти и заполнить поле "Email" валидными данными для входа
        my_fixture.find_element(By.XPATH, password_log).send_keys(password) # найти и заполнить поле "Пароль" валидными данными дял входа
        my_fixture.find_element(By.XPATH, button_login).click() # найти и нажать кнопку "Войти"
        
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_order))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL

        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/'
        

    def test_log_in_using_the_button_personal_account(self, my_fixture):
        my_fixture.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account))).click() # дождаться видимости кнопки "Личный кабинет" и нажать на неё
        
        my_fixture.find_element(By.XPATH, email_log).send_keys(email) # найти и заполнить поле "Email" валидными данными для входа
        my_fixture.find_element(By.XPATH, password_log).send_keys(password) # найти и заполнить поле "Пароль" валидными данными дял входа
        my_fixture.find_element(By.XPATH, button_login).click() # найти и нажать кнопку "Войти"


        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_order))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL
        
        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/'
    

    def test_log_in_using_the_button_in_the_registration_form(self, my_fixture):
        my_fixture.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, login_account))).click() # дождаться видимости кнопки "Войти в аккаунт" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_registration))).click() # дождаться видимости кнопки "Зарегистрироваться" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_registration_form))).click() # дождаться видимости кнопки "Войти" и нажать на неё

        my_fixture.find_element(By.XPATH, email_log).send_keys(email) # найти и заполнить поле "Email" валидными данными для входа
        my_fixture.find_element(By.XPATH, password_log).send_keys(password) # найти и заполнить поле "Пароль" валидными данными дял входа
        my_fixture.find_element(By.XPATH, button_login).click() # найти и нажать кнопку "Войти"
        
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_order))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL

        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/'
        


    def test_login_using_the_button_in_the_password_recovery_form(self, my_fixture):
        my_fixture.get("https://stellarburgers.nomoreparties.site/")
        
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, login_account))).click() # дождаться видимости кнопки "Войти в аккаунт" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_recover_password))).click() # дождаться видимости кнопки "Восстановить пароль" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login_in_registration_form))).click() # дождаться видимости кнопки "Войти" и нажать на неё

        my_fixture.find_element(By.XPATH, email_log).send_keys(email) # найти и заполнить поле "Email" валидными данными для входа
        my_fixture.find_element(By.XPATH, password_log).send_keys(password) # найти и заполнить поле "Пароль" валидными данными дял входа
        my_fixture.find_element(By.XPATH, button_login).click() # найти и нажать кнопку "Войти"
        
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_order))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL

        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/'
        