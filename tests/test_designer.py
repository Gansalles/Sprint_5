import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LocatorsBurgers

##### Раздел «Конструктор» #####

# Проверь, что работают переходы к разделам:
# «Булки»,
# «Соусы»,
# «Начинки»
# Дополнительно решил проверить, что при переключении разделов, блок с продуктами скролится

class TestDesigner:

    def test_design(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1")))
        driver.find_element(*LocatorsBurgers.stellar_bugrers_botton_sauces).click()
        print(driver.find_element(By.XPATH, "//h2[text()='Соусы']").location)
        time.sleep(1)
        assert (driver.find_element(By.XPATH, ".//main//div[2][contains(@class, 'current')]") and
                driver.find_element(By.XPATH, ".//h2[text() = 'Соусы']").location == {'x': 332, 'y': 244})
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_fillings).click()
        print(driver.find_element(By.XPATH, "//h2[text()='Начинки']").location)
        time.sleep(1)
        assert (driver.find_element(By.XPATH, ".//main//div[3][contains(@class, 'current')]") and
                driver.find_element(By.XPATH, "//h2[text() = 'Начинки']").location == {'x': 332, 'y': 244})
        driver.find_element(*LocatorsBurgers.stellar_bugrers_button_rolls).click()
        print(driver.find_element(By.XPATH, "//h2[text()='Булки']").location)
        time.sleep(1)
        assert (driver.find_element(By.XPATH, ".//main//div[1][contains(@class, 'current')]") and
                driver.find_element(By.XPATH, ".//h2[text() = 'Булки']").location == {'x': 332, 'y': 244})
        driver.quit()
