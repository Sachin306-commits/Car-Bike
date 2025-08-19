from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text,safe_send_keys




class used_cars:
    def __init__(self, driver):
        self.driver = driver
    def used_cars_button(self):
        safe_click(self.driver,(By.XPATH,"(//span[text()='Used Cars'])[1]"))
        safe_click(self.driver,(By.XPATH,"(//span[text()='Used Cars Under ₹ 3 Lakh'])[1]"))
        #safe_click(self.driver,(By.XPATH,"(//span[@class='accordionArrow relative'])[1]"))
        #safe_click(self.driver,(By.XPATH,"(//button[text()='Below 3 Lakh'])[1]"))
        safe_click(self.driver,(By.XPATH,"(//button[text()='3 to 6 Lakh'])[1]"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='6 to 9 Lakh'])[1]"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='9 to 12 Lakh'])[1]"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='12 to 18 Lakh'])[1]"))
        safe_click(self.driver,(By.XPATH,"(//button[text()='Above 25 Lakh'])[1]"))


    def body_type(self):
        safe_click(self.driver,(By.XPATH,"(//span[@class='accordionArrow relative'])[25]"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='Hatchback'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='SUV'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='Sedan'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='MUV'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='Crossover'])"))
    def show_only(self):
        safe_click(self.driver,(By.XPATH,"(//span[@class='accordionArrow relative'])[26]"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='Rated 8.0+'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='Warranty Available'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='Financing Available'])"))
        safe_click(self.driver, (By.XPATH, "(// button[text() = 'Discounted Price'])"))
        safe_click(self.driver,(By.XPATH,"(//button[text()='Great Deals'])"))
    def Manufactured_Year(self):
        safe_click(self.driver, (By.XPATH, "(//span[@class='accordionArrow relative'])[27]"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='2015 And Newer'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='2016 And Newer'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='2017 And Newer'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='2018 And Newer'])"))
        safe_click(self.driver, (By.XPATH, "(//button[text()='2019 And Newer'])"))
        safe_click(self.driver,(By.XPATH,"(//button[text()='2020 And Newer'])"))





