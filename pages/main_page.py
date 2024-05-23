from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from ui_selectors import HomePageSelectors



# TODO: решить проблему с неймингом


class Main_page(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.drom.ru/')

    def button_sign_in(self):
        return self.find(HomePageSelectors.button_sign_in_selector)

    def button_click(self):
        sign_in_button = self.button_sign_in()
        sign_in_button.click()

    def find_icon_for_asset(self):
        return self.find(HomePageSelectors.icon_selector)
