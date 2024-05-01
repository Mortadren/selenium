from pages.base_page import BasePage
from selenium.webdriver.common.by import By


button_sign_in_selector = (By.CSS_SELECTOR, '[data-ga-stats-name="auth_block_login"]')

class Main_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.drom.ru/')
        
    def button_sign_in(self):
        return self.find(button_sign_in_selector)