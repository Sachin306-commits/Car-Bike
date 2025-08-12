
from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text




class First_Look:
    def __init__(self, driver):
        self.driver = driver

    def first(self):
        safe_click(self.driver, (By.XPATH, "(//span[text()='Videos'])[1]"))
    def first_look(self):
        safe_click(self.driver,"(//span[text()='First Look'])[1]")
    def arrow_1(self):
        safe_click(self.driver,"//div[@class='arrowRight']")
    def categories(self):
        return safe_get_text(self.driver,"//div[@class='listContainer grid card  ']")


