import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *

class TestTransferToYourPersonalAccount:
    def test_button_transfer_to_your_personal_account(self, driver, my_fixture):
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_profile))) # найти и дождаться видимости кнопки "Профиль" перед сравнением URL
        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        


    def test_transfer_from_personal_account_in_constructor(self, driver, my_fixture):
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_constructor))).click() # дождаться видимости кнопки "Конструктор" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_order))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL
        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/'
        


    def test_transfer_in_constructor_and_Stellar_Burgers_logo(self, driver, my_fixture):
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_constructor))).click() # дождаться видимости кнопки "Конструктор" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, logo_stellar_burgers))).click() # дождаться видимости логотипа "Stellar Burgers" и нажать на него
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_order)))# найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL
        assert my_fixture.current_url == 'https://stellarburgers.nomoreparties.site/'