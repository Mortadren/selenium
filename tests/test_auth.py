from selenium.webdriver.common.by import By
from pages.login_page import Login_page
from pages.main_page import Main_page



def test_opening(browser):
    mane_page = Main_page(browser)
    login_page = Login_page(browser)
    mane_page.open()
    # assert mane_page.asdas() 
    mane_page.button_click()
    login_page.insert_login()
    login_page.insert_pass()
    login_page.click_button_sign()
    assert mane_page.find_icon_for_asset()
    
    # assert mane_page.button_sign_in


# def test_button_sign_in(browser):
#     mane_page = Main_page(browser)
#     mane_page.button_sign_in.click()