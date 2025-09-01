import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *


class TestLogOutOfYourAccount:
    def test_log_out_of_your_account(self, driver, my_fixture):
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_exit))).click() # дождаться видимости кнопки "Выход" и нажать на неё
        WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login))) # найти и дождаться видимости кнопки "Вход" перед сравнением URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        
        