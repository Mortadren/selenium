from selenium.webdriver.common.by import By


class LoginPageSelectors:
    sign_field_selector = (By.ID, 'sign')
    password_field_selector = (By.ID, 'password')
    button_sign_selector = (By.ID, 'signbutton')

# TODO: заменить поиск селектора 
class HomePageSelectors:
    button_sign_in_selector = (By.CSS_SELECTOR, '[data-ga-stats-name="auth_block_login"]')
    icon_selector = (By.CLASS_NAME, '_1tlqpaw1 _15r2d5o1')

