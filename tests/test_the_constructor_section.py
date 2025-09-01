import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *


class TestTheConstructorSection:
    def test_buns_section(self, my_fixture):
        WebDriverWait(my_fixture, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, button_sauces))) # дождаться видимости кнопки "Соусы" и нажать на неё
        buns = my_fixture.find_element(By.XPATH, button_buns_class).get_attribute('class') # получить атрибут class (неактивен)
        my_fixture.find_element(By.XPATH, button_buns).click()
        buns_active = my_fixture.find_element(By.XPATH, button_buns_class).get_attribute('class') # получить атрибут class (активен)
        assert 'tab_tab_type_current__2BEPc' not in buns
        assert 'tab_tab_type_current__2BEPc' in buns_active
        

    def test_sauces_section(self, driver, my_fixture):
        WebDriverWait(my_fixture, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, button_sauces))) # дождаться видимости кнопки "Соусы"
        sauces = my_fixture.find_element(By.XPATH, button_sauces_class).get_attribute('class') # получить атрибут class (неактивен)
        my_fixture.find_element(By.XPATH, button_sauces).click()
        sauces_active = my_fixture.find_element(By.XPATH, button_sauces_class).get_attribute('class') # получить атрибут class (активен)
        assert 'tab_tab_type_current__2BEPc' not in sauces
        assert 'tab_tab_type_current__2BEPc' in sauces_active
        


    def test_fillings_section(self, driver, my_fixture):
        WebDriverWait(my_fixture, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, button_fillings))) # дождаться видимости кнопки "Начинки
        fillings = my_fixture.find_element(By.XPATH, button_fillings_class).get_attribute('class') # получить атрибут class (неактивен)
        my_fixture.find_element(By.XPATH, button_fillings).click()
        fillings_active = my_fixture.find_element(By.XPATH, button_fillings_class).get_attribute('class') # получить атрибут class (активен)
        assert 'tab_tab_type_current__2BEPc' not in fillings
        assert 'tab_tab_type_current__2BEPc' in fillings_active
        
        
        