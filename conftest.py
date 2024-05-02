from selenium import webdriver
import pytest




@pytest.fixture()
def browser():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

