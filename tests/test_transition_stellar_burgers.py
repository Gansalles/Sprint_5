from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from data import Data
from locators import LocatorsBurgers

##### Переход  #####
class TestTransitionfordesigner:

    # Переход по клику на «Конструктор» и на логотип Stellar Burgers
    def test_transition_click_desingner_and_logo(self, driver):
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
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_designer).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1")))
        time.sleep(1)
        assert driver.find_element(By.XPATH, ".//h1").text == 'Соберите бургер'
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//a[text()='Профиль']")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_logo).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1")))
        time.sleep(1)
        assert driver.find_element(By.XPATH, ".//h1").text == 'Соберите бургер'
        driver.quit()