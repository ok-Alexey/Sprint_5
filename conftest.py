import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *

@pytest.fixture(scope="function")
def email():
    num = random.randint(100, 999)
    email = f'Alexey_Razumov_28+29_{num}@ya.ru'
    return email


@pytest.fixture(scope="function")
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
        
    WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_registration_in_form_registration))) 
        
    my_fixture.find_element(By.XPATH, name_in_registration_form).send_keys('Alexey')
    my_fixture.find_element(By.XPATH, email_in_registration_form).send_keys(email_password[0])
    my_fixture.find_element(By.XPATH, password_field).send_keys(email_password[1])
    my_fixture.find_element(By.XPATH, button_login_in_registration_form).click()

    WebDriverWait(my_fixture, 8).until(expected_conditions.visibility_of_element_located((By.XPATH, button_login)))
    
    my_fixture.find_element(By.XPATH, email_in_registration_form).send_keys(email_password[0])
    my_fixture.find_element(By.XPATH, password_field).send_keys(email_password[1])
    my_fixture.find_element(By.XPATH, button_login).click()
    return my_fixture




