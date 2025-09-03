
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text, safe_select


class city_location:
    def __init__(self, driver):
        self.driver = driver
    def location_select(self,city):
        safe_click(self.driver,(By.XPATH,"//button[@class='headerBtn gridAc flex caps selectedCity']"))
        safe_click(self.driver,(By.XPATH,"//input[@type='type here to search']"))
        safe_select(self.driver,(By.XPATH,"//input[@type='type here to search']"),city)
        safe_click(self.driver,(By.XPATH,"//div[@class='cities active']"))
