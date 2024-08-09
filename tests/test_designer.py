from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatorsBurgers


##### Раздел «Конструктор» #####

# Проверь, что работают переходы к разделам:
# «Булки»,
# «Соусы»,
# «Начинки»

class TestDesigner:

    def test_design(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            ((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_SAUCES).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            ((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_ACTIVE_BUTTON_SAUCES)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_FILLINGS).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            ((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_ACTIVE_BUTTON_FILLINGS)
        driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_BUTTON_ROLLS).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located
            ((LocatorsBurgers.STELLAR_BURGERS_TITLE_ASSEMBLE_THE_BURGER)))
        assert driver.find_element(*LocatorsBurgers.STELLAR_BURGERS_ACTIVE_BUTTON_ROLLS)
