from selenium.webdriver.common.by import By
# from pages.login_page import Login_page
from pages.main_page import Main_page



def test_opening(browser):
    mane_page = Main_page(browser)
    mane_page.open()
    assert mane_page.button_sign_in.click()