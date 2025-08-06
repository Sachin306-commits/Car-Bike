from webbrowser import driver

from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text




class social_media:
    def __init__(self,driver):
        self.driver = driver

    def scroll_button(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

    def youtube(self):
        safe_click(self.driver, (By.XPATH, "(//img[@alt='car&bike Youtube'])"))

    def scroll(self):
        self.driver.switch_to.window(driver.window_handles[0])

    def Twitter(self):
        safe_click(self.driver, (By.XPATH,"(//img[@alt='car&bike Twitter'])"))

    def scroll1(self):
        self.driver.switch_to.window(driver.window_handles[0])

    def Instagram(self):
        safe_click(self.driver, (By.XPATH, "(//img[@alt='car&bike Instagram'])"))

    def scroll2(self):
        self.driver.switch_to.window(driver.window_handles[0])

    def facebook(self):
        safe_click(self.driver, (By.XPATH, "(//img[@alt='car&bike Facebook'])"))

    def scroll3(self):
        self.driver.switch_to.window(driver.window_handles[0])
    def Linkedin(self):
        safe_click(self.driver, (By.XPATH, "(//img[@alt='car&bike Facebook'])"))

    def scroll4(self):
        self.driver.switch_to.window(driver.window_handles[0])
    def whatsup(self):
        safe_click(self.driver, (By.XPATH, "(//img[@alt='car&bike WhatsApp'])"))

    def scroll5(self):
        self.driver.switch_to.window(driver.window_handles[0])