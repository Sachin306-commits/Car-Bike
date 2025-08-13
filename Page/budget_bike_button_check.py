from webbrowser import driver

from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text



class budget_bike_button_check:

    def __init__(self):
        self.driver = driver

    def New_bike_budget(self):
        safe_click(self.driver,By.XPATH,"(//span[@class='uppercase'])[5]")
    def New_bike_budget_button(self):
        safe_click(self.driver,By.XPATH,"(//span[@class='nListTitle'])[14]")
    def New_bike_budget_button_price(self):
        safe_click(self.driver,By.XPATH,"(//button[@type='button'])[4]")
    def New_bike_budget_button_type(self):
        safe_click(self.driver,By.XPATH,"(//button[@type='button'])[8]")
    def New_bike_budget_button_search(self):
        safe_click(self.driver,By.XPATH,"(//button[text()='Search'])[1]")
        print("All the buttons are working and we take you to the selected page ")
    def Key_highlights(self):
        return safe_get_text(self.driver,By.XPATH,"(//div[@class='card toggleSlide '])[1]")
    def faq(self):
        return safe_get_text(self.driver,By.XPATH,"(//div[@id='faqs'])[1]")




