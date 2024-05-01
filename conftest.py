from selenium import webdriver
import pytest




@pytest.fixture()
def browser():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    return driver

