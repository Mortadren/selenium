import os
from dotenv import load_dotenv
from pages.base_page import BasePage
from ui_selectors import LoginPageSelectors


load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


class Login_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_sign_field(self):
        return self.find(LoginPageSelectors.sign_field_selector)

    def insert_login(self):
        sign_field = self.find_sign_field()
        sign_field.send_keys(login)

    def find_pass_field(self):
        return self.find(LoginPageSelectors.password_field_selector)

    def insert_pass(self):
        pass_field = self.find_pass_field()
        pass_field.send_keys(password)

    def find_button_sign(self):
        return self.find(LoginPageSelectors.button_sign_selector)

    def click_button_sign(self):
        button_sign = self.find_button_sign()
        button_sign.click()
