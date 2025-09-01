import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# test_entranse
login_account = (".//button[text() = 'Войти в аккаунт']") # кнопка "Войти в аккаунт" 
email_log = (".//input[@type='text']") # поле "Email" в форме входа
password_log = ("//input[@type='password']") # поле "Пароль" в форме входа
button_login = (".//button[text() = 'Войти']") # кнопка "Войти"
button_order = (".//div//button[text() = 'Оформить заказ']") # кнопка "Оформить заказ"
personal_account = (".//div//a[@class = 'AppHeader_header__link__3D_hX' and @href = '/account']") # кнопка "Личный кабинет" 
button_registration = (".//div//a[text() = 'Зарегистрироваться']") # кнопка "Зарегистрироваться" в форме входа в аккаунт
button_login_in_registration_form = (".//a[text() = 'Войти']") # кнопка "Войти" в форме регистрации
button_recover_password = ".//div//a[text() = 'Восстановить пароль']" # кнопка "Восстановить пароль" в форме регистрации

# test_log_out_of_your_account and test_registration
button_exit = (".//button[text() = 'Выход']") # кнопка "Выйти" из личного кабинета
name_in_registration_form = (".//label[text()='Имя']/following-sibling::input") # поле "Имя" в форме регистрации
email_in_registration_form = (".//label[text()='Email']/following-sibling::input") # поле "Email" в форме регистрации
password_field = (".//div[@class = 'input pr-6 pl-6 input_type_password input_size_default']//input") # поле "Пароль" в форме регистрации
text_of_the_error = (".//p[text() = 'Некорректный пароль']") # текст сообщения об ошибке "Некорректный пароль" в форме регистрации
button_registration_in_form_registration = (".//div//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка "Зарегистрироваться" в форме регистрации

# test_the_constructor_section
button_buns = (".//span[text()='Булки']") # поле "Булки"
button_buns_class = ("//span[text()='Булки']/parent::div") # получить значение clsass для поля "Булки"
button_sauces = (".//span[text()='Соусы']") # поле "Соусы"
button_sauces_class = ("//span[text()='Соусы']/parent::div") # получить значение clsass для поля "Соусы"
button_fillings = (".//span[text()='Начинки']") # поле "Начинки"
button_fillings_class = ("//span[text()='Начинки']/parent::div") # получить значение clsass для поля "Начинки"

# test_transfer_to_your_personal_account
button_profile = (".//a[text() = 'Профиль']") # кнопка "Профиль"
button_constructor = (".//p[text() = 'Конструктор']") # кнопка "Конструктор"
logo_stellar_burgers = ('svg') # логотип "Stellar Burgers"

