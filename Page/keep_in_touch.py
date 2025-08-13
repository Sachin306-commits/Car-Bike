from webbrowser import driver

from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text



class Keep_in_touch:



    def __init__(self):
        self.driver = driver

    def scroll_button_last(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

    def address(self):
        return safe_get_text(self.driver,By.XPATH,"//div[@class='fAddr']")
    def contact(self):
        return safe_get_text(self.driver,By.XPATH,"//div[@class='fTel flex gridAc mb10']")
    def email(self):
        return safe_get_text(self.driver,By.XPATH,"//div[@class='fTel flex gridAc']")
    def copyright(self):
        return safe_get_text(self.driver,By.XPATH,"(//div[@class='fAddr'])[2]")