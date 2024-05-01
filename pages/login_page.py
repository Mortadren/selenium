from pages.base_page import BasePage
from selenium.webdriver.common.by import By

sign_field_selector = (By.ID, 'sign')
password_field_selector = (By.ID, 'password')
button_sign_selector = (By.ID, 'signbutton')

class Login_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # def open(self):


    def sign_field(self):
        return self.find(sign_field_selector)
    
    def password_field(self):
        return self.find(password_field_selector)

    def button_sign(self):
        return self.find(button_sign_selector)