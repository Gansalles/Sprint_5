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

        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_register).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Регистрация']")))
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(generate_name)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(generate_mail)
        driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(generate_password)
        driver.find_element(By.XPATH, ".//button[text()= 'Зарегистрироваться']").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_burgers_login).send_keys(generate_mail)
        driver.find_element(*LocatorsBurgers.stellar_burgers_password).send_keys(generate_password)
        driver.find_element(*LocatorsBurgers.stellar_burgers_button_enter_enter).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, ".//a[contains(@href, 'profile')]").text == 'Профиль'
        driver.quit()

    ### Проверка на неверный пароль

    def test_wrong_password(self, driver):

        generate_name = List.name()
        generate_mail = List.mail()
        generate_wrong_password = List.wrong_password()

        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_register).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Регистрация']")))
        driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(generate_name)
        driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(generate_mail)
        driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(generate_wrong_password)
        driver.find_element(By.XPATH, ".//button[text()= 'Зарегистрироваться']").click()
        assert driver.find_element(By.XPATH, ".//p[text() = 'Некорректный пароль']").text
        driver.quit()