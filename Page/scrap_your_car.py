import time

from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
    def self_service_main(self):
        safe_click(self.driver, (By.XPATH, "(//span[text()='Car services'])[1]"))
    def scrap_your_car(self):
        safe_click(self.driver,(By.XPATH,"(//span[text()='Scrap Your Car'])[1]"))
        time.sleep(10)