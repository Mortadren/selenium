from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        try:
            return self.browser.find_element(*args)
        except NoSuchElementException:
            print(f"No element found with locator: {args}")
            return None
