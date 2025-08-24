import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogOutOfYourAccount:
    def test_log_out_of_your_account(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//div//p[text() = 'Личный Кабинет']"))).click() # дождаться видимости кнопки "Личный Кабинет" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Выход']"))).click() # дождаться видимости кнопки "Выход" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//h2[text() = 'Вход']"))) # найти и дождаться видимости кнопки "Вход" перед сравнением URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()