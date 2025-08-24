import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTransferToYourPersonalAccount:
    def test_button_transfer_to_your_personal_account(self, driver):
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//p[text() = 'Личный Кабинет']"))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//a[text() = 'Профиль']"))) # найти и дождаться видимости кнопки "Профиль" перед сравнением URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        driver.quit()


    def test_transfer_from_personal_account_in_constructor(self, driver):
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//p[text() = 'Личный Кабинет']"))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//p[text() = 'Конструктор']"))).click() # дождаться видимости кнопки "Конструктор" и нажать на неё
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Оформить заказ']"))) # найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()


    def test_transfer_in_constructor_and_Stellar_Burgers_logo(self, driver):
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//p[text() = 'Личный Кабинет']"))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//p[text() = 'Конструктор']"))).click() # дождаться видимости кнопки "Конструктор" и нажать на неё

        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//p[text() = 'Личный Кабинет']"))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'svg'))).click() # дождаться видимости логотипа "Stellar Burgers" и нажать на него
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Оформить заказ']")))# найти и дождаться видимости кнопки "Оформить заказ" перед сравнением URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()