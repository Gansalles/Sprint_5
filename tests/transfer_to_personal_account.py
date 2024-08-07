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
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_burgers_login).send_keys(*Data.AUTH_EMAIL)
        driver.find_element(*LocatorsBurgers.stellar_burgers_password).send_keys(*Data.AUTH_PASSWORD)
        driver.find_element(*LocatorsBurgers.stellar_burgers_button_enter_enter).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//a[text()='Профиль']")))
        time.sleep(1)
        assert driver.find_element(By.XPATH, ".//a[contains(@href, 'profile')]").text == 'Профиль'
        driver.quit()