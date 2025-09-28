from pygments import highlight
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text
from Utils.locators import Locators

class articles:
    def __init__(self, driver):
        self.driver = driver


    def get_about_us1(self):
        safe_click(self.driver,Locators.About_us)





