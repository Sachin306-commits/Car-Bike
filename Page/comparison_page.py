
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text

class ComparisonPage:
    def __init__(self, driver):
        self.driver = driver

    def get_comparison_card_text(self):
        return safe_get_text(self.driver, (By.XPATH, "//div[contains(text(),'Compare')]"))

    def go_to_comparison_page(self):
        safe_click(self.driver, (By.XPATH, "//a[contains(text(),'View All Comparison')]"))

    def select_car(self, car_make, model_option, variant_option):
        safe_click(self.driver, (By.XPATH, f"//div[contains(text(),'{car_make}')]") )
        safe_click(self.driver, (By.XPATH, f"//option[contains(text(),'{model_option}')]"))
        safe_click(self.driver, (By.XPATH, f"//option[contains(text(),'{variant_option}')]"))

    def select_all_three_cars(self):
        self.select_car("Land Rover", "Range Rover Evoque", "2.0 S")
        self.select_car("Land Rover", "Discovery Sport", "2.0 SE")
        self.select_car("Land Rover", "Velar", "2.0 R-Dynamic")

    def click_compare(self):
        safe_click(self.driver, (By.XPATH, "//button[contains(text(),'Compare') or contains(text(),'COMPARE')]") )

    def get_compare_result_text(self):
        return safe_get_text(self.driver, (By.XPATH, "//div[contains(@class,'compare-results')]"))
