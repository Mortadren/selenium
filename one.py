import unittest
from selenium import webdriver

class AuthTestMethods(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Edge()


    def test_name(self):
        driver = self.driver
        driver.get('https://www.drom.ru/')
        self.assertIn('Дром - цены на машины', driver.title)

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()