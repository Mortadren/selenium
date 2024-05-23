from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
