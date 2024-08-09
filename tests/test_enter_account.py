from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import LocatorsBurgers



class TestEnterAccount:

##### Вход #####


# вход по кнопке «Войти в аккаунт» на главной

    def test_enter_account_start_window(self, driver):
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_START_WINDOW_ENTER).click()
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

# вход через кнопку «Личный кабинет»

    def test_enter_accout_button_personal_account(self, driver):
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_LOGIN).send_keys(*Data.AUTH_EMAIL)
        driver.find_element(*LocatorsBurgers.STELLAE_BURGERS_PASSWORD).send_keys(*Data.AUTH_PASSWORD)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_ENTER_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE)))
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE).text == 'Профиль'

# вход через кнопку в форме регистрации

    def test_enter_account_register_form(self, driver):
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_REGISTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_BUTTON_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_LOGIN).send_keys(*Data.AUTH_EMAIL)
        driver.find_element(*LocatorsBurgers.STELLAE_BURGERS_PASSWORD).send_keys(*Data.AUTH_PASSWORD)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_ENTER_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE)))
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_TITLE_PROFILE).text == 'Профиль'

# вход через кнопку в форме восстановления пароля

    def test_enter_account_password_recovery_form(self, driver):
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((LocatorsBurgers.STELLAR_BURGERS_TITLE_ENTER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_PASSWORD_RECOVERY).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            ((LocatorsBurgers.STELLAR_BURGERS_TITLE_RECOVERY_PASSWORD)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_ENTER_RECOVERY_FORM).click()
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
