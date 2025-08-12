import time

from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_send_keys, safe_get_text

class Scrap_your_car:
    def __init__(self, driver):
        self.driver = driver
    def self_service_main(self):
        safe_click(self.driver, (By.XPATH, "(//span[text()='Car services'])[1]"))
    def scrap_your_car(self):
        safe_click(self.driver,(By.XPATH,"(//span[text()='Scrap Your Car'])[1]"))
        time.sleep(10)
    def window_scroll(self):
        self.driver.execute_script("window.scrollBy(0, 500);")
    def scrap_your_car_steps(self):
        print(safe_get_text(self.driver,(By.XPATH,"//div[@data-widget ='ImageScroller']")))
    def why_choose_car(self):
        print(safe_get_text(self.driver,(By.XPATH,"(//div[@class='wrapper'])[8]")))

