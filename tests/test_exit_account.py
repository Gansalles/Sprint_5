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
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_burgers_login).send_keys(*Data.AUTH_EMAIL)
        driver.find_element(*LocatorsBurgers.stellar_burgers_password).send_keys(*Data.AUTH_PASSWORD)
        driver.find_element(*LocatorsBurgers.stellar_burgers_button_enter_enter).click()
        WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[contains(@class, 'main')]")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//a[contains(@href, 'profile')]")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_exit).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        time.sleep(1)
        assert driver.find_element(By.XPATH, ".//h2").text == 'Вход'
        driver.quit()