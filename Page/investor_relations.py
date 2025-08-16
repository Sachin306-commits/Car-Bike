from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text

class Investor_Relations:


    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
    def Investor(self):
        safe_click(self.driver, (By.XPATH, "//a[@title ='Investor Relations']"))
    def content_wrap(self):
        return safe_get_text(self.driver,(By.XPATH,"//div[@class ='contentWrap']"))
    def investor_contact(self):
        return safe_get_text(self.driver(By.XPATH,"//div[@class ='undefined card ']"))
    def download_date(self):
        return safe_click(self.driver,(By.XPATH,"(//button[text() ='Download'])[1]"))
