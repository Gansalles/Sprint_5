from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from data import Data
from locators import LocatorsBurgers


class TestExit:
##### Выход из аккаунта #####

# Выход по кнопке «Выйти» в личном кабинете

    def test_exit_account(self, driver):
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_LOGIN).send_keys(*Data.AUTH_EMAIL)
        driver.find_element(*LocatorsBurgers.STELLAE_BURGERS_PASSWORD).send_keys(*Data.AUTH_PASSWORD)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_ENTER_ENTER).click()
        WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located
        ((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_EXIT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER).text == 'Вход'
