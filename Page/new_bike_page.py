# new_bike_page.py
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text

class NewBikePage:
    def __init__(self, driver):
        self.driver = driver

    def open_new_bikes(self):
        safe_click(self.driver, (By.XPATH, "//a[contains(text(),'New Bikes')]"))

    def apply_filters_and_view_all(self):
        safe_click(self.driver, (By.XPATH, "//button[contains(text(),'Filter')]"))
        safe_click(self.driver, (By.XPATH, "//button[contains(text(),'Search')]"))
        #safe_click(self.driver, (By.XPATH, "//a[contains(text(),'View All New Bikes')]"))

    def explore_bike_sections(self, locator_list):
        for locator in locator_list:
            for _ in range(5):
                safe_click(self.driver, locator)

    def get_top_brands_text(self):
        return safe_get_text(self.driver, (By.XPATH, "//h2[contains(text(),'Top Brands')]") or (By.XPATH, "//div[@class='top-brands']"))
