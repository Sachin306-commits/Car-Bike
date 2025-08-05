from selenium.webdriver.common.by import By
from Utils.selenium_helpers import safe_click, safe_get_text

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self):
        self.driver.get("https://www.carandbike.com/")
        self.driver.maximize_window()

    def scroll_to_cover_story(self):
        self.driver.execute_script("window.scrollBy(0, 720);")

    def get_cover_story_text(self):
        return safe_get_text(self.driver, (By.XPATH, "//h3[contains(text(),'Cover')]"))

    def click_bike_button(self):
        safe_click(self.driver, (By.XPATH, "//a[contains(text(),'New Bikes')]"))
