import pytest
from selenium import webdriver
from data import Data

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.Stellar_Burgers_URL)
    chrome_driver.set_window_size(1920, 1080)
    return chrome_driver
