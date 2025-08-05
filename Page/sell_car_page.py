# sell_car_page.py
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_send_keys

class SellCarPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_sell_car(self):
        safe_click(self.driver, (By.XPATH, "//a[contains(text(),'Sell Car')]"))

    def enter_seller_details(self, name, mobile):
        safe_send_keys(self.driver, (By.ID, "name"), name)
        safe_send_keys(self.driver, (By.ID, "mobile"), mobile)

    def submit_form(self):
        safe_click(self.driver, (By.XPATH, "//button[contains(text(),'Submit')]"))
