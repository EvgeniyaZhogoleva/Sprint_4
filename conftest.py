import pytest
from selenium import webdriver
from data import Data


@pytest.fixture
def driver():

    driver = webdriver.Firefox()
    driver.get(Data.URL_SCOOTER)
    yield driver
    driver.quit()