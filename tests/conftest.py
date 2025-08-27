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
    emailpassword = [email, password]
    return emailpassword
    

@pytest.fixture(scope="function")
def my_fixture():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def driver(email_password, my_fixture):
    
    my_fixture.get("https://stellarburgers.nomoreparties.site/register")
        
    WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//button[text() = 'Зарегистрироваться']"))) 
        
    my_fixture.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys('Alexey')
    my_fixture.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys(email_password[0])
    my_fixture.find_elements(By.XPATH, "html//fieldset//input[@class = 'text input__textfield text_type_main-default']")[2].send_keys(email_password[1])
    my_fixture.find_element(By.XPATH, "html//button[text() = 'Зарегистрироваться']").click()

    WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, "html//h2[text() = 'Вход']")))
    
    my_fixture.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[0].send_keys(email_password[0])
    my_fixture.find_elements(By.XPATH, "html//input[@class = 'text input__textfield text_type_main-default']")[1].send_keys(email_password[1])
    my_fixture.find_element(By.XPATH, "html//form//button[text() = 'Войти']").click()
    return my_fixture




