import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



@pytest.fixture
def email():
    num = random.randint(100, 999)
    email = f'Alexey_Razumov_28+29_{num}@ya.ru'
    return email


@pytest.fixture
def email_password(email):
    num = random.randint(100, 999)
    password = f'2457{num}'
    slov = [email, password]
    return slov

@pytest.fixture
def driver(email_password):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
        
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Зарегистрироваться']"))) 
        
    driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexey')
    driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys(email_password[0])
    driver.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[2].send_keys(email_password[1])
    driver.find_element(By.XPATH, "html//button[text() = 'Зарегистрироваться']").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//h2[text() = 'Вход']")))
    
    driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys(email_password[0])
    driver.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys(email_password[1])
    driver.find_element(By.XPATH, "html//form//button[text() = 'Войти']").click()
    return driver



