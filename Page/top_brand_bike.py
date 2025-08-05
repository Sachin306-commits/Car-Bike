
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text




class Top_Brand:
    def __init__(self, driver):
        self.driver = driver

    def top_brand_bike(self):
        safe_click(self.driver, (By.XPATH, "//img[@title='Royal Enfield Bikes']"))
    def royal_review(self):
        safe_click(self.driver,(By.XPATH,"(//div[text()='Reviews'])[5]"))
    def cross_button(self):
        safe_click(self.driver,(By.XPATH,"//*[name()='path' and contains(@d,'M19 6.41L1')]"))
    def varrient(self):
        safe_click(self.driver,(By.XPATH,"(//div[text()='Variants'])[5]"))
    def cross_button2(self):
        safe_click(self.driver,(By.XPATH,"//*[name()='path' and contains(@d,'M19 6.41L1')]"))
    def compare_royal(self):
        safe_click(self.driver,(By.XPATH,"(//div[text()='Compare'])[5]"))
    def compare_royal1(self):
        safe_click(self.driver,(By.XPATH,"(//input[@type='checkbox'])[2]"))
    def compare_royal2(self):
        safe_click(self.driver,(By.XPATH,"(//input[@type='checkbox'])[3]"))
    def compare_royal3(self):
        safe_click(self.driver,(By.XPATH,"(//input[@type='checkbox'])[4]"))
    def compare_button(self):
        safe_click(self.driver,(By.XPATH,"//button[text()='Compare Now']"))




