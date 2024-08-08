import time
from random import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from list import List
from locators import LocatorsBurgers


class TestRegistration:
    ### Регистрация
    def test_correct_registration(self, driver):
        generate_name = List.name()
        generate_mail = List.mail()
        generate_password = List.correct_password()

        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_REGISTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_HOLDER_REGISTER_NAME).send_keys(generate_name)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_HOLDER_REGISTER_MAIL).send_keys(generate_mail)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_HOLDER_REGISTER_PASSWORD).send_keys(generate_password)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_REGISTER_FORM_REGISTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_LOGIN).send_keys(generate_mail)
        driver.find_element(*LocatorsBurgers.STELLAE_BURGERS_PASSWORD).send_keys(generate_password)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_ENTER_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            ((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE)))
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE).text == 'Профиль'


    ### Проверка на неверный пароль

    def test_wrong_password(self, driver):

        generate_name = List.name()
        generate_mail = List.mail()
        generate_wrong_password = List.wrong_password()

        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_REGISTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_HOLDER_REGISTER_NAME).send_keys(generate_name)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_HOLDER_REGISTER_MAIL).send_keys(generate_mail)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_HOLDER_REGISTER_PASSWORD).send_keys(generate_wrong_password)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_REGISTER_FORM_REGISTER).click()
        assert (driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_FORM_REGISTER_WRONG_PASSWORD).text
                == 'Некорректный пароль')
