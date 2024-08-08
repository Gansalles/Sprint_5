from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from data import Data
from locators import LocatorsBurgers

##Проверь переход по клику на «Личный кабинет».

class Test_transfer_to_personal_account:
    # Переход по клику на «Личный кабинет».
    def test_transition_personal_account(self, driver):
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
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE).text == 'Профиль'
