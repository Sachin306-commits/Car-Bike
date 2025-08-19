from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text


class bike_service:
    def __init__(self, driver):
        self.driver = driver
    def bike_service(self):
        safe_click(self.driver,(By.XPATH,"//a[@title='New Bikes' and contains(@href, '/new-bikes')]"))
        safe_click(self.driver,(By.XPATH,"//span[text()='Find Bike Service Centers']"))
    def service_center_data(self):
        return safe_get_text(self.driver,(By.XPATH,"//span[@class='amContent']"))