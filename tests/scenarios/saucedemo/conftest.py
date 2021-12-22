import pytest
from selenium import webdriver
from driver.config import Config


@pytest.fixture
def driver():
    driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH)
    driver.maximize_window()
    yield driver
    driver.quit()

