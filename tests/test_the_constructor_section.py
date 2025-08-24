import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestTheConstructorSection:
    def test_buns_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Соусы']"))).click() # дождаться видимости кнопки "Соусы" и нажать на неё

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Булки']"))).click() # дождаться видимости кнопки "Булки" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"))).click() # дождаться видимости кнопки "Флюоресцентная булка R2-D3" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Детали ингредиента']"))) # найти и дождаться видимости надписи "Детали ингредиента" перед сравнением URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d'
        driver.quit()


    def test_sauces_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Соусы']"))).click() # дождаться видимости кнопки "Соусы" и нажать на неё
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Соус Spicy-X']"))).click() # дождаться видимости кнопки "Соус Spicy-X" и нажать на неё
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Детали ингредиента']"))) # найти и дождаться видимости надписи "Детали ингредиента" перед сравнением URL
        
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa72'
        driver.quit()


    def test_fillings_section(self, driver):
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Начинки']"))).click() # дождаться видимости кнопки "Начинки" и нажать на неё

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']"))).click() # дождаться видимости кнопки "Мясо бессмертных моллюсков Protostomia" и нажать на неё
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Детали ингредиента']"))) # найти и дождаться видимости надписи "Детали ингредиента" перед сравнением URL
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6f'