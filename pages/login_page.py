from pages.base_page import BasePage
from selenium.webdriver.common.by import By

sign_field_selector = (By.ID, 'sign')
password_field_selector = (By.ID, 'password')
button_sign_selector = (By.ID, 'signbutton')

LOGIN = '89994516217'
PASSWORD = 'Artyom#Access!'

class Login_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def find_sign_field(self):
        return self.find(sign_field_selector)
    
    def insert_login(self):
        sign_field = self.find_sign_field()
        sign_field.send_keys(LOGIN)

    def find_pass_field(self):
        return self.find(password_field_selector)

    def insert_pass(self):
        pass_field = self.find_pass_field()
        pass_field.send_keys(PASSWORD)

    def find_button_sign(self):
        return self.find(button_sign_selector)
    
    def click_button_sign(self):
        button_sign = self.find_button_sign()
        button_sign.click()
