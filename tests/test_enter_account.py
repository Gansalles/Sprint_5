from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Data
from locators import LocatorsBurgers



class TestEnterAccount:

##### Вход #####


# вход по кнопке «Войти в аккаунт» на главной

    def test_enter_account_start_window(self, driver):
        driver.find_element(*LocatorsBurgers.stellar_burgers_button_start_window_enter).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_burgers_login).send_keys(*Data.AUTH_EMAIL)
        driver.find_element(*LocatorsBurgers.stellar_burgers_password).send_keys(*Data.AUTH_PASSWORD)
        driver.find_element(*LocatorsBurgers.stellar_burgers_button_enter_enter).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//a[contains(@href, 'profile')]")))
        assert driver.find_element(By.XPATH, ".//a[contains(@href, 'profile')]").text == 'Профиль'
        driver.quit()



# вход через кнопку «Личный кабинет»

    def test_enter_accout_button_personal_account(self, driver):
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
        assert driver.find_element(By.XPATH, ".//a[contains(@href, 'profile')]").text == 'Профиль'
        driver.quit()

# вход через кнопку в форме регистрации

    def test_enter_account_register_form(self, driver):
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_register).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//a[text()='Войти']")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_enter).click()
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
        assert driver.find_element(By.XPATH, ".//a[contains(@href, 'profile')]").text == 'Профиль'
        driver.quit()
# вход через кнопку в форме восстановления пароля

    def test_enter_account_password_recovery_form(self, driver):
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_password_recovery).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Восстановление пароля']")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_enter_recovery_form).click()
        driver.find_element(*LocatorsBurgers.stellar_burgers_login).send_keys(*Data.AUTH_EMAIL)
        driver.find_element(*LocatorsBurgers.stellar_burgers_password).send_keys(*Data.AUTH_PASSWORD)
        driver.find_element(*LocatorsBurgers.stellar_burgers_button_enter_enter).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[contains(@class, 'main')]")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//a[contains(@href, 'profile')]")))
        assert driver.find_element(By.XPATH, ".//a[contains(@href, 'profile')]").text == 'Профиль'
        driver.quit()